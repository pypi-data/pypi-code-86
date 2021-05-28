""" Annotation.

Do not edit this file by hand.
This is generated by parsing api.html service doc.
"""
from ambra_sdk.exceptions.service import InvalidJson
from ambra_sdk.exceptions.service import MissingFields
from ambra_sdk.exceptions.service import NotFound
from ambra_sdk.exceptions.service import NotPermitted
from ambra_sdk.service.query import QueryO

class Annotation:
    """Annotation."""

    def __init__(self, api):
        self._api = api

    
    def list(
        self,
        phi_namespace=None,
        storage_namespace=None,
        study_id=None,
        study_uid=None,
    ):
        """List.
        :param phi_namespace: phi_namespace
        :param storage_namespace: storage_namespace
        :param study_id: study_id
        :param study_uid: study_uid
        """
        request_data = {
           'phi_namespace': phi_namespace,
           'storage_namespace': storage_namespace,
           'study_id': study_id,
           'study_uid': study_uid,
        }
	
        errors_mapping = {}
        errors_mapping[('MISSING_FIELDS', None)] = MissingFields('A required field is missing or does not have data in it. The error_subtype holds a array of all the missing fields')
        errors_mapping[('NOT_FOUND', None)] = NotFound('The study was not found.')
        errors_mapping[('NOT_PERMITTED', None)] = NotPermitted('You are not permitted to view the study of the annotations')
        query_data = {
            'api': self._api,
            'url': '/annotation/list',
            'request_data': request_data,
            'errors_mapping': errors_mapping,
            'required_sid': True,
        }
        return QueryO(**query_data)
    
    def add(
        self,
        frame_number,
        instance_uid,
        series_uid,
        json=None,
        phi_namespace=None,
        stamp=None,
        storage_namespace=None,
        study_id=None,
        study_uid=None,
    ):
        """Add.
        :param frame_number: The frame number
        :param instance_uid: The instance uid
        :param series_uid: The series uid
        :param json: json
        :param phi_namespace: phi_namespace
        :param stamp: stamp
        :param storage_namespace: storage_namespace
        :param study_id: study_id
        :param study_uid: study_uid
        """
        request_data = {
           'frame_number': frame_number,
           'instance_uid': instance_uid,
           'json': json,
           'phi_namespace': phi_namespace,
           'series_uid': series_uid,
           'stamp': stamp,
           'storage_namespace': storage_namespace,
           'study_id': study_id,
           'study_uid': study_uid,
        }
	
        errors_mapping = {}
        errors_mapping[('INVALID_JSON', None)] = InvalidJson('The field is not in valid JSON format. The error_subtype holds the name of the field')
        errors_mapping[('MISSING_FIELDS', None)] = MissingFields('A required field is missing or does not have data in it. The error_subtype holds a array of all the missing fields')
        errors_mapping[('NOT_FOUND', None)] = NotFound('The study was not found.')
        errors_mapping[('NOT_PERMITTED', None)] = NotPermitted('You are not permitted to add annotations to the study')
        query_data = {
            'api': self._api,
            'url': '/annotation/add',
            'request_data': request_data,
            'errors_mapping': errors_mapping,
            'required_sid': True,
        }
        return QueryO(**query_data)
    
    def set(
        self,
        json,
        uuid,
    ):
        """Set.
        :param json: The JSON annotation data structure
        :param uuid: Id of the annotation
        """
        request_data = {
           'json': json,
           'uuid': uuid,
        }
	
        errors_mapping = {}
        errors_mapping[('INVALID_JSON', None)] = InvalidJson('The field is not in valid JSON format. The error_subtype holds the name of the field')
        errors_mapping[('MISSING_FIELDS', None)] = MissingFields('A required field is missing or does not have data in it. The error_subtype holds a array of all the missing fields')
        errors_mapping[('NOT_FOUND', None)] = NotFound('The study was not found.')
        errors_mapping[('NOT_PERMITTED', None)] = NotPermitted('You are not permitted to add annotations to the study')
        query_data = {
            'api': self._api,
            'url': '/annotation/set',
            'request_data': request_data,
            'errors_mapping': errors_mapping,
            'required_sid': True,
        }
        return QueryO(**query_data)
    
    def get(
        self,
        uuid,
    ):
        """Get.
        :param uuid: Id of the annotation
        """
        request_data = {
           'uuid': uuid,
        }
	
        errors_mapping = {}
        errors_mapping[('MISSING_FIELDS', None)] = MissingFields('A required field is missing or does not have data in it. The error_subtype holds a array of all the missing fields')
        errors_mapping[('NOT_FOUND', None)] = NotFound('The annotation  was not found.')
        errors_mapping[('NOT_PERMITTED', None)] = NotPermitted('You are not permitted to view the annotation')
        query_data = {
            'api': self._api,
            'url': '/annotation/get',
            'request_data': request_data,
            'errors_mapping': errors_mapping,
            'required_sid': True,
        }
        return QueryO(**query_data)
    
    def delete(
        self,
        uuid,
    ):
        """Delete.
        :param uuid: Id of the annotation
        """
        request_data = {
           'uuid': uuid,
        }
	
        errors_mapping = {}
        errors_mapping[('MISSING_FIELDS', None)] = MissingFields('A required field is missing or does not have data in it. The error_subtype holds a array of all the missing fields')
        errors_mapping[('NOT_FOUND', None)] = NotFound('The annotation  was not found.')
        errors_mapping[('NOT_PERMITTED', None)] = NotPermitted('You are not permitted to delete the annotation')
        query_data = {
            'api': self._api,
            'url': '/annotation/delete',
            'request_data': request_data,
            'errors_mapping': errors_mapping,
            'required_sid': True,
        }
        return QueryO(**query_data)
    