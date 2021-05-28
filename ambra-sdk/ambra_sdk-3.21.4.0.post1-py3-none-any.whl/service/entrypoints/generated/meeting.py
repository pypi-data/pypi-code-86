""" Meeting.

Do not edit this file by hand.
This is generated by parsing api.html service doc.
"""
from ambra_sdk.exceptions.service import NotAttending
from ambra_sdk.exceptions.service import NotFound
from ambra_sdk.exceptions.service import NotPermitted
from ambra_sdk.service.query import QueryO

class Meeting:
    """Meeting."""

    def __init__(self, api):
        self._api = api

    
    def add(
        self,
        name,
        state,
        phi_namespace=None,
        storage_namespace=None,
        study_id=None,
        study_uid=None,
    ):
        """Add.
        :param name: Title of the meeting
        :param state: State of the meeting
        :param phi_namespace: phi_namespace
        :param storage_namespace: storage_namespace
        :param study_id: study_id
        :param study_uid: study_uid
        """
        request_data = {
           'name': name,
           'phi_namespace': phi_namespace,
           'state': state,
           'storage_namespace': storage_namespace,
           'study_id': study_id,
           'study_uid': study_uid,
        }
	
        errors_mapping = {}
        errors_mapping[('NOT_FOUND', None)] = NotFound('The study can not be found')
        errors_mapping[('NOT_PERMITTED', None)] = NotPermitted('You are not permitted to create a meeting for the study')
        query_data = {
            'api': self._api,
            'url': '/meeting/add',
            'request_data': request_data,
            'errors_mapping': errors_mapping,
            'required_sid': True,
        }
        return QueryO(**query_data)
    
    def set(
        self,
        uuid,
        name=None,
        state=None,
    ):
        """Set.
        :param uuid: UUID of the meeting
        :param name: Title of the meeting (optional)
        :param state: State of the meeting (optional)
        """
        request_data = {
           'name': name,
           'state': state,
           'uuid': uuid,
        }
	
        errors_mapping = {}
        errors_mapping[('NOT_FOUND', None)] = NotFound('The meeting can not be found')
        errors_mapping[('NOT_PERMITTED', None)] = NotPermitted('You are not permitted to modify the meeting')
        query_data = {
            'api': self._api,
            'url': '/meeting/set',
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
        :param uuid: UUID of the meeting
        """
        request_data = {
           'uuid': uuid,
        }
	
        errors_mapping = {}
        errors_mapping[('NOT_FOUND', None)] = NotFound('The meeting can not be found')
        errors_mapping[('NOT_PERMITTED', None)] = NotPermitted('You are not permitted to get the meeting')
        query_data = {
            'api': self._api,
            'url': '/meeting/get',
            'request_data': request_data,
            'errors_mapping': errors_mapping,
            'required_sid': True,
        }
        return QueryO(**query_data)
    
    def join(
        self,
        uuid,
    ):
        """Join.
        :param uuid: UUID of the meeting
        """
        request_data = {
           'uuid': uuid,
        }
	
        errors_mapping = {}
        errors_mapping[('NOT_FOUND', None)] = NotFound('The meeting can not be found')
        errors_mapping[('NOT_PERMITTED', None)] = NotPermitted('You are not permitted to do this')
        query_data = {
            'api': self._api,
            'url': '/meeting/join',
            'request_data': request_data,
            'errors_mapping': errors_mapping,
            'required_sid': True,
        }
        return QueryO(**query_data)
    
    def leave(
        self,
        uuid,
    ):
        """Leave.
        :param uuid: UUID of the meeting
        """
        request_data = {
           'uuid': uuid,
        }
	
        errors_mapping = {}
        query_data = {
            'api': self._api,
            'url': '/meeting/leave',
            'request_data': request_data,
            'errors_mapping': errors_mapping,
            'required_sid': True,
        }
        return QueryO(**query_data)
    
    def roster(
        self,
        uuid,
    ):
        """Roster.
        :param uuid: UUID of the meeting
        """
        request_data = {
           'uuid': uuid,
        }
	
        errors_mapping = {}
        errors_mapping[('NOT_FOUND', None)] = NotFound('The meeting can not be found')
        errors_mapping[('NOT_PERMITTED', None)] = NotPermitted('You are not permitted to do this')
        query_data = {
            'api': self._api,
            'url': '/meeting/roster',
            'request_data': request_data,
            'errors_mapping': errors_mapping,
            'required_sid': True,
        }
        return QueryO(**query_data)
    
    def presenter(
        self,
        user_id,
        uuid,
    ):
        """Presenter.
        :param user_id: UUID of the user to make the presenter
        :param uuid: UUID of the meeting
        """
        request_data = {
           'user_id': user_id,
           'uuid': uuid,
        }
	
        errors_mapping = {}
        errors_mapping[('NOT_ATTENDING', None)] = NotAttending('The user is not attending the meeting')
        errors_mapping[('NOT_FOUND', None)] = NotFound('The meeting can not be found')
        errors_mapping[('NOT_PERMITTED', None)] = NotPermitted('You are not permitted to do this')
        query_data = {
            'api': self._api,
            'url': '/meeting/presenter',
            'request_data': request_data,
            'errors_mapping': errors_mapping,
            'required_sid': True,
        }
        return QueryO(**query_data)
    
    def ping(
        self,
        uuid,
    ):
        """Ping.
        :param uuid: UUID of the meeting
        """
        request_data = {
           'uuid': uuid,
        }
	
        errors_mapping = {}
        errors_mapping[('NOT_FOUND', None)] = NotFound('The meeting can not be found')
        query_data = {
            'api': self._api,
            'url': '/meeting/ping',
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
        :param uuid: UUID of the meeting
        """
        request_data = {
           'uuid': uuid,
        }
	
        errors_mapping = {}
        errors_mapping[('NOT_FOUND', None)] = NotFound('The meeting can not be found')
        errors_mapping[('NOT_PERMITTED', None)] = NotPermitted('You are not permitted to delete the meeting')
        query_data = {
            'api': self._api,
            'url': '/meeting/delete',
            'request_data': request_data,
            'errors_mapping': errors_mapping,
            'required_sid': True,
        }
        return QueryO(**query_data)
    
    def events_add(
        self,
        event,
        uuid,
    ):
        """Events add.
        :param event: Event to send to the meeting
        :param uuid: UUID of the meeting
        """
        request_data = {
           'event': event,
           'uuid': uuid,
        }
	
        errors_mapping = {}
        errors_mapping[('NOT_FOUND', None)] = NotFound('The meeting can not be found')
        errors_mapping[('NOT_PERMITTED', None)] = NotPermitted('You are not permitted to do this')
        query_data = {
            'api': self._api,
            'url': '/meeting/events/add',
            'request_data': request_data,
            'errors_mapping': errors_mapping,
            'required_sid': True,
        }
        return QueryO(**query_data)
    