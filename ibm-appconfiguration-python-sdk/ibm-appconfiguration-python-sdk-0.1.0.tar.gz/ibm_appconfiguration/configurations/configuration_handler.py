# Copyright 2021 IBM All Rights Reserved.
#
# Licensed under the Apache License, Version 2.0 (the "License");
# you may not use this file except in compliance with the License.
# You may obtain a copy of the License at
#
#      http://www.apache.org/licenses/LICENSE-2.0
#
# Unless required by applicable law or agreed to in writing, software
# distributed under the License is distributed on an "AS IS" BASIS,
# WITHOUT WARRANTIES OR CONDITIONS OF ANY KIND, either express or implied.
# See the License for the specific language governing permissions and
# limitations under the License.

from typing import Dict, List, Optional, Any

from .models import Feature
from .models import SegmentRules
from .models import Segment
from .models import Property
from ibm_appconfiguration.core.internal import Logger
from ibm_appconfiguration.core import BaseRequest
from .internal.utils.file_manager import FileManager
from .internal.utils.metering import Metering
from .internal.utils.socket import Socket
from .internal.utils.url_builder import URLBuilder
from threading import Timer, Thread
from ibm_appconfiguration.configurations.internal.common import config_messages, config_constants
from .internal.utils.connectivity import Connectivity

try:
    import thread
except ImportError:
    import _thread as thread


class ConfigurationHandler:
    __instance = None

    @staticmethod
    def get_instance():
        """ Static access method. """
        if ConfigurationHandler.__instance is None:
            return ConfigurationHandler()
        return ConfigurationHandler.__instance

    def __init__(self):
        """ Virtually private constructor. """
        self.__retry_count = 3
        if ConfigurationHandler.__instance is not None:
            raise Exception("ConfigurationHandler " + config_messages.SINGLETON_EXCEPTION)
        else:
            self.__collection_id = ''
            self.__environment_id = ''
            self.__apikey = ''
            self.__guid = ''
            self.__region = ''
            self.__is_initialized = False
            self.__configuration_update_listener = None
            self.__feature_map = dict()
            self.__property_map = dict()
            self.__segment_map = dict()
            self.__live_config_update_enabled = True
            ConfigurationHandler.__instance = self
            self.__retry_count = 3
            self.__retry_interval = 600
            self.__config_file = None
            self.__on_socket_retry = False
            self.__override_server_host = None
            self.__socket = None
            self.__connectivity = None
            self.__is_network_connected = True

    def init(self, apikey: str,
             guid: str,
             region: str,
             override_server_host=str):

        self.__apikey = apikey
        self.__guid = guid
        self.__region = region
        self.__override_server_host = override_server_host

        self.__feature_map = dict()
        self.__property_map = dict()
        self.__segment_map = dict()

    def set_context(self, collection_id: str, environment_id: str,
                    configuration_file: Optional[str] = None,
                    live_config_update_enabled: Optional[bool] = True):

        self.__collection_id = collection_id
        self.__environment_id = environment_id
        URLBuilder.init_with_collection_id(collection_id=collection_id,
                                           guid=self.__guid,
                                           region=self.__region,
                                           environment_id=environment_id,
                                           override_server_host=self.__override_server_host)
        Metering.get_instance().set_metering_url(URLBuilder.get_metering_url(), self.__apikey)
        self.__is_initialized = True

        self.__live_config_update_enabled = live_config_update_enabled
        self.__config_file = configuration_file
        self.__check_network()

    def load_data(self):
        if not self.__is_initialized:
            Logger.error(config_messages.CONFIGURATION_HANDLER_INIT_ERROR)
            return
        if self.__config_file:
            self.__get_file_data(self.__config_file)
        self.__load_configurations()
        if self.__live_config_update_enabled:
            self.__fetch_config_data()
        else:
            if self.__socket:
                self.__socket.cancel()

    def register_configuration_update_listener(self, listener):
        if callable(listener):
            if self.__is_initialized:
                self.__configuration_update_listener = listener
            else:
                Logger.error(config_messages.CONFIGURATION_HANDLER_INIT_ERROR)
        else:
            Logger.error(config_messages.CONFIGURATION_HANDLER_METHOD_ERROR)

    def __check_network(self):
        if self.__live_config_update_enabled:
            if self.__connectivity is None:
                self.__connectivity = Connectivity.get_instance()
                self.__connectivity.add_connectivity_listener(self.__network_listener)
                self.__connectivity.check_connection()
        else:
            self.__connectivity = None

    def __network_listener(self, is_connected: bool):
        if not self.__live_config_update_enabled:
            self.__connectivity = None
            return

        if is_connected:
            if not self.__is_network_connected:
                self.__is_network_connected = True
                self.__fetch_config_data()
        else:
            Logger.debug(config_messages.NO_INTERNET_CONNECTION_ERROR)
            self.__is_network_connected = False

    def get_properties(self) -> Dict[str, Property]:
        return self.__property_map

    def get_property(self, property_id: str):
        if property_id in self.__property_map:
            return self.__property_map.get(property_id)
        else:
            self.__load_configurations()
            if property_id in self.__property_map:
                return self.__property_map.get(property_id)
            else:
                Logger.error(config_messages.PROPERTY_INVALID + property_id)
                return None

    def get_features(self) -> Dict[str, Feature]:
        return self.__feature_map

    def get_feature(self, feature_id: str) -> Feature:
        if feature_id in self.__feature_map:
            return self.__feature_map.get(feature_id)
        else:
            self.__load_configurations()
            if feature_id in self.__feature_map:
                return self.__feature_map.get(feature_id)
            else:
                Logger.error(config_messages.FEATURE_INVALID + feature_id)
                return None

    def __fetch_config_data(self):
        if self.__is_initialized:
            self.__fetch_from_api()
            self.__on_socket_retry = False
            config_thread = Thread(target=self.__start_web_socket, args=())
            config_thread.daemon = True
            config_thread.start()

    def __start_web_socket(self):
        headers = {
            'Authorization': self.__apikey
        }
        if self.__socket:
            self.__socket.cancel()
            self.__socket = None
        self.__socket = Socket()
        self.__socket.setup(
            url=URLBuilder.get_web_socket_url(),
            headers=headers,
            callback=self.__on_web_socket_callback
        )

    def __get_file_data(self, file_path: str):
        data = FileManager.read_files(file_path=file_path)
        if data is not None:
            self.__write_to_file(json=data)

    def __load_configurations(self):
        all_config: dict = FileManager.read_files()
        if all_config:
            if 'features' in all_config:
                self.__feature_map = dict()
                try:
                    all_feature_list: List = all_config.get('features')
                    for i in range(0, len(all_feature_list)):
                        feature: dict = all_feature_list[i]
                        feature_obj = Feature(feature)
                        self.__feature_map[feature_obj.get_feature_id()] = feature_obj
                except Exception as err:
                    Logger.debug(err)

            if 'properties' in all_config:
                self.__property_map = dict()
                try:
                    all_property_list: List = all_config.get('properties')
                    for i in range(0, len(all_property_list)):
                        property_list: dict = all_property_list[i]
                        property_obj = Property(property_list)
                        self.__property_map[property_obj.get_property_id()] = property_obj
                except Exception as err:
                    Logger.debug(err)

            if 'segments' in all_config:
                self.__segment_map = dict()
                try:
                    segment_list: List = all_config.get('segments')
                    for i in range(0, len(segment_list)):
                        segment: dict = segment_list[i]
                        segment_obj = Segment(segment)
                        self.__segment_map[segment_obj.get_segment_id()] = segment_obj
                except Exception as err:
                    Logger.debug(err)

    def record_valuation(self, property_id, feature_id, entity_id, evaluated_segment_id):
        Metering.get_instance().add_metering(
            guid=self.__guid,
            environment_id=self.__environment_id,
            collection_id=self.__collection_id,
            entity_id=entity_id,
            segment_id=evaluated_segment_id,
            feature_id=feature_id,
            property_id=property_id
        )

    def property_evaluation(self, property_obj: Property, entity_id: str, entity_attributes: dict = dict()) -> Any:

        result_dict = {
            'evaluated_segment_id': config_constants.DEFAULT_SEGMENT_ID,
            'value': None
        }

        try:
            if len(entity_attributes) <= 0:
                return property_obj.get_value()

            segment_rules = property_obj.get_segment_rules()
            if len(segment_rules) > 0:
                rules_map = self.__parse_rules(segment_rules)
                result_dict = self.__evaluate_rules(rules_map, entity_attributes, property_obj=property_obj)
                return result_dict['value']
            else:
                return property_obj.get_value()

        finally:
            property_id = property_obj.get_property_id()
            self.record_valuation(property_id=property_id, feature_id=None, entity_id=entity_id,
                                  evaluated_segment_id=result_dict['evaluated_segment_id'])

    def feature_evaluation(self, feature: Feature, entity_id: str, entity_attributes: dict = dict()) -> Any:

        result_dict = {
            'evaluated_segment_id': config_constants.DEFAULT_SEGMENT_ID,
            'value': None
        }
        try:
            if feature.is_enabled():

                if len(entity_attributes) <= 0:
                    return feature.get_enabled_value()

                segment_rules = feature.get_segment_rules()
                if len(segment_rules) > 0:
                    rules_map = self.__parse_rules(segment_rules)
                    result_dict = self.__evaluate_rules(rules_map, entity_attributes, feature=feature)
                    return result_dict['value']
                else:
                    return feature.get_enabled_value()
            else:
                return feature.get_disabled_value()
        finally:
            feature_id = None if feature is None else feature.get_feature_id()
            self.record_valuation(property_id=None, feature_id=feature_id, entity_id=entity_id,
                                  evaluated_segment_id=result_dict['evaluated_segment_id'])

    def __evaluate_rules(self, rules_map: dict,
                         entity_attributes: dict = dict(),
                         feature: Feature = None,
                         property_obj: Property = None) -> dict:
        result_dict = {
            'evaluated_segment_id': config_constants.DEFAULT_SEGMENT_ID,
            'value': None
        }
        for i in range(1, len(rules_map) + 1):
            segment_rule = rules_map[i]
            if not (segment_rule is None):
                for level in range(0, len(segment_rule.get_rules())):
                    try:
                        rule: dict = segment_rule.get_rules()[level]
                        segments: List = rule.get('segments')
                        for inner_level in range(0, len(segments)):
                            segment_key = segments[inner_level]
                            if self.__evaluate_segment(segment_key, entity_attributes):
                                result_dict['evaluated_segment_id'] = segment_key
                                if segment_rule.get_value() == "$default":
                                    result_dict[
                                        'value'] = feature.get_enabled_value() if feature is not None else property_obj.get_value()
                                else:
                                    result_dict['value'] = segment_rule.get_value()
                                return result_dict
                    except Exception as err:
                        Logger.debug(err)

        result_dict['value'] = feature.get_enabled_value() if feature is not None else property_obj.get_value()
        return result_dict

    def __evaluate_segment(self, segment_key: str, entity_attributes: dict) -> bool:
        if segment_key in self.__segment_map:
            segment: Segment = self.__segment_map[segment_key]
            return segment.evaluate_rule(entity_attributes)
        return False

    def __parse_rules(self, segment_rules: List) -> dict:
        rule_map = dict()
        for i in range(0, len(segment_rules)):
            try:
                rules = segment_rules[i]
                rules_obj = SegmentRules(rules)
                rule_map[rules_obj.get_order()] = rules_obj
            except Exception as err:
                Logger.debug(err)
        return rule_map

    def __write_server_file(self, json: dict):
        if self.__live_config_update_enabled:
            self.__write_to_file(json)

    def __write_to_file(self, json: dict):
        FileManager.store_files(json)
        self.__load_configurations()
        if self.__configuration_update_listener and callable(self.__configuration_update_listener):
            self.__configuration_update_listener()

    def __fetch_from_api(self):
        if self.__is_initialized:
            self.__retry_count -= 1
            config_url = URLBuilder.get_config_url()
            service = BaseRequest()
            header = {
                'Authorization': self.__apikey,
                'Content-Type': 'application/json'
            }

            request = service.prepare_request(
                method='GET',
                url=config_url,
                headers=header
            )

            response = service.send(request)
            status_code = response.get_status_code()

            if 200 <= status_code <= 299:
                response_data = response.get_result()
                try:
                    response_data = dict(response_data)
                    if response_data:
                        self.__write_server_file(response_data)
                except:
                    if response_data:
                        self.__write_server_file(response_data)
            else:
                if self.__retry_count > 0:
                    self.__fetch_from_api()
                else:
                    self.__retry_count = 3
                    Logger.error(config_messages.CONFIGURATION_API_ERROR)
                    Timer(self.__retry_interval, lambda: self.__fetch_from_api()).start()
        else:
            Logger.debug(config_messages.CONFIGURATION_HANDLER_INIT_ERROR)

    def __on_web_socket_callback(self, message=None, error_state=None, closed_state=None, open_state=None):
        if message:
            self.__fetch_from_api()
            Logger.debug(f'Received message from socket {message}')
        elif error_state:
            Logger.debug(f'Received error from socket {error_state}')
            Timer(self.__retry_interval, lambda: self.__start_web_socket()).start()
        elif closed_state:
            Logger.debug(f'Received close connection from socket')
            if self.__socket is not None:
                self.__on_socket_retry = True
                Timer(self.__retry_interval, lambda: self.__start_web_socket()).start()
        elif open_state:
            if self.__on_socket_retry:
                self.__on_socket_retry = False
                self.__fetch_from_api()
            Logger.debug(f'Received opened connection from socket')
        else:
            Logger.debug('Unknown Error inside the socket connection')
