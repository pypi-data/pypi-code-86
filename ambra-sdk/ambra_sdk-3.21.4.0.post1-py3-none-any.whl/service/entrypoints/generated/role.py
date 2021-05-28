""" Role.

Do not edit this file by hand.
This is generated by parsing api.html service doc.
"""
from ambra_sdk.exceptions.service import AccountNotFound
from ambra_sdk.exceptions.service import FilterNotFound
from ambra_sdk.exceptions.service import InUse
from ambra_sdk.exceptions.service import InvalidCondition
from ambra_sdk.exceptions.service import InvalidField
from ambra_sdk.exceptions.service import InvalidJson
from ambra_sdk.exceptions.service import InvalidPermission
from ambra_sdk.exceptions.service import InvalidPermissionValue
from ambra_sdk.exceptions.service import InvalidSortField
from ambra_sdk.exceptions.service import InvalidSortOrder
from ambra_sdk.exceptions.service import MissingFields
from ambra_sdk.exceptions.service import NoOtherRoleEdit
from ambra_sdk.exceptions.service import NotFound
from ambra_sdk.exceptions.service import NotPermitted
from ambra_sdk.exceptions.service import ReportError
from ambra_sdk.service.query import QueryO
from ambra_sdk.service.query import QueryOPSF

class Role:
    """Role."""

    def __init__(self, api):
        self._api = api

    
    def list(
        self,
        account_id,
    ):
        """List.
        :param account_id: uuid of the account
        """
        request_data = {
           'account_id': account_id,
        }
	
        errors_mapping = {}
        errors_mapping[('FILTER_NOT_FOUND', None)] = FilterNotFound('The filter can not be found. The error_subtype will hold the filter UUID')
        errors_mapping[('INVALID_CONDITION', None)] = InvalidCondition('The condition is not support. The error_subtype will hold the filter expression this applies to')
        errors_mapping[('INVALID_FIELD', None)] = InvalidField('The field is not valid for this object. The error_subtype will hold the filter expression this applies to')
        errors_mapping[('INVALID_SORT_FIELD', None)] = InvalidSortField('The field is not valid for this object. The error_subtype will hold the field name this applies to')
        errors_mapping[('INVALID_SORT_ORDER', None)] = InvalidSortOrder('The sort order for the field is invalid. The error_subtype will hold the field name this applies to')
        errors_mapping[('MISSING_FIELDS', None)] = MissingFields('A required field is missing or does not have data in it. The error_subtype holds a array of all the missing fields')
        errors_mapping[('NOT_FOUND', None)] = NotFound('The account can not be found')
        errors_mapping[('NOT_PERMITTED', None)] = NotPermitted('You are not permitted to view this list')
        query_data = {
            'api': self._api,
            'url': '/role/list',
            'request_data': request_data,
            'errors_mapping': errors_mapping,
            'required_sid': True,
        }
        query_data['paginated_field'] = 'roles'
        return QueryOPSF(**query_data)
    
    def add(
        self,
        account_id,
        name,
        for_account=None,
        for_group=None,
        for_location=None,
        permissions=None,
        setting_param=None,
        settings=None,
    ):
        """Add.
        :param account_id: uuid of the account
        :param name: Name of the role
        :param for_account: A flag that the role can be used in an account, default is on (optional)
        :param for_group: A flag that the role can be used in a group, default is on (optional)
        :param for_location: A flag that the role can be used in a location, default is on (optional)
        :param permissions: A hash of the role permissions (optional)
        :param setting_param: Set an individual setting. This is an alternative to the settings hash for easier use in the API tester (optional)
        :param settings: A hash of the role settings (optional)
        """
        request_data = {
           'account_id': account_id,
           'for_account': for_account,
           'for_group': for_group,
           'for_location': for_location,
           'name': name,
           'permissions': permissions,
           'settings': settings,
        }
        if setting_param is not None:
            setting_param_dict = {'{prefix}{k}'.format(prefix='setting_', k=k): v for k,v in setting_param.items()}
            request_data.update(setting_param_dict)
	
        errors_mapping = {}
        errors_mapping[('ACCOUNT_NOT_FOUND', None)] = AccountNotFound('The account was not found')
        errors_mapping[('INVALID_JSON', None)] = InvalidJson('The field is not in valid JSON format. The error_subtype holds the name of the field')
        errors_mapping[('INVALID_PERMISSION', None)] = InvalidPermission('Invalid permission flag. The error_subtype holds the name of the permission flag.')
        errors_mapping[('INVALID_PERMISSION_VALUE', None)] = InvalidPermissionValue('The permission flag has an invalid value. The error_subtype holds the name of the permission flag.')
        errors_mapping[('MISSING_FIELDS', None)] = MissingFields('A required field is missing or does not have data in it. The error_subtype holds a array of all the missing fields')
        errors_mapping[('NOT_PERMITTED', None)] = NotPermitted('You are not permitted to add a role to that account')
        query_data = {
            'api': self._api,
            'url': '/role/add',
            'request_data': request_data,
            'errors_mapping': errors_mapping,
            'required_sid': True,
        }
        return QueryO(**query_data)
    
    def set(
        self,
        uuid,
        description=None,
        for_account=None,
        for_group=None,
        for_location=None,
        name=None,
        permission_param=None,
        permissions=None,
        setting_param=None,
        settings=None,
    ):
        """Set.
        :param uuid: The role uuid
        :param description: Description of the role (optional)
        :param for_account: A flag that the role can be used in an account (optional)
        :param for_group: A flag that the role can be used in a group (optional)
        :param for_location: A flag that the role can be used in a location (optional)
        :param name: Name of the role (optional)
        :param permission_param: Set an individual permission. This is an alternative to the permissions hash for easier use in the API tester (optional)
        :param permissions: A hash of the role permissions (optional)
        :param setting_param: Set an individual setting. This is an alternative to the settings hash for easier use in the API tester (optional)
        :param settings: A hash of the role settings (optional)
        """
        request_data = {
           'description': description,
           'for_account': for_account,
           'for_group': for_group,
           'for_location': for_location,
           'name': name,
           'permissions': permissions,
           'settings': settings,
           'uuid': uuid,
        }
        if permission_param is not None:
            permission_param_dict = {'{prefix}{k}'.format(prefix='permission_', k=k): v for k,v in permission_param.items()}
            request_data.update(permission_param_dict)
        if setting_param is not None:
            setting_param_dict = {'{prefix}{k}'.format(prefix='setting_', k=k): v for k,v in setting_param.items()}
            request_data.update(setting_param_dict)
	
        errors_mapping = {}
        errors_mapping[('INVALID_JSON', None)] = InvalidJson('The field is not in valid JSON format. The error_subtype holds the name of the field')
        errors_mapping[('INVALID_PERMISSION', None)] = InvalidPermission('Invalid permission flag. The error_subtype holds the name of the permission flag.')
        errors_mapping[('INVALID_PERMISSION_VALUE', None)] = InvalidPermissionValue('The permission flag has an invalid value. The error_subtype holds the name of the permission flag.')
        errors_mapping[('NOT_FOUND', None)] = NotFound('The role can not be found')
        errors_mapping[('NOT_PERMITTED', None)] = NotPermitted('You are not permitted to edit the role')
        errors_mapping[('NO_OTHER_ROLE_EDIT', None)] = NoOtherRoleEdit('No other role has role_edit permissions so you can not disable role_edit for this role')
        query_data = {
            'api': self._api,
            'url': '/role/set',
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
        :param uuid: The role uuid
        """
        request_data = {
           'uuid': uuid,
        }
	
        errors_mapping = {}
        errors_mapping[('MISSING_FIELDS', None)] = MissingFields('A required field is missing or does not have data in it. The error_subtype holds a array of all the missing fields')
        errors_mapping[('NOT_FOUND', None)] = NotFound('The role can not be found')
        errors_mapping[('NOT_PERMITTED', None)] = NotPermitted('You are not permitted to view this role')
        query_data = {
            'api': self._api,
            'url': '/role/get',
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
        :param uuid: The role uuid
        """
        request_data = {
           'uuid': uuid,
        }
	
        errors_mapping = {}
        errors_mapping[('IN_USE', None)] = InUse('The role is in use. The error_subtype holds a array of the objects that are using it')
        errors_mapping[('MISSING_FIELDS', None)] = MissingFields('A required field is missing or does not have data in it. The error_subtype holds a array of all the missing fields')
        errors_mapping[('NOT_FOUND', None)] = NotFound('The role can not be found')
        errors_mapping[('NOT_PERMITTED', None)] = NotPermitted('You are not permitted to delete this role')
        query_data = {
            'api': self._api,
            'url': '/role/delete',
            'request_data': request_data,
            'errors_mapping': errors_mapping,
            'required_sid': True,
        }
        return QueryO(**query_data)
    
    def default_permissions(
        self,
        account_id=None,
    ):
        """Default permissions.
        :param account_id: The account id (optional)
        """
        request_data = {
           'account_id': account_id,
        }
	
        errors_mapping = {}
        errors_mapping[('MISSING_FIELDS', None)] = MissingFields('A required field is missing or does not have data in it. The error_subtype holds a array of all the missing fields')
        query_data = {
            'api': self._api,
            'url': '/role/default/permissions',
            'request_data': request_data,
            'errors_mapping': errors_mapping,
            'required_sid': True,
        }
        return QueryO(**query_data)
    
    def report_detail(
        self,
        account_id,
    ):
        """Report detail.
        :param account_id: The account id
        """
        request_data = {
           'account_id': account_id,
        }
	
        errors_mapping = {}
        errors_mapping[('MISSING_FIELDS', None)] = MissingFields('A required field is missing or does not have data in it. The error_subtype holds a array of all the missing fields')
        errors_mapping[('NOT_FOUND', None)] = NotFound('The account was not found')
        errors_mapping[('NOT_PERMITTED', None)] = NotPermitted('You are not permitted to run this report')
        errors_mapping[('REPORT_ERROR', None)] = ReportError('Unable to start the report')
        query_data = {
            'api': self._api,
            'url': '/role/report/detail',
            'request_data': request_data,
            'errors_mapping': errors_mapping,
            'required_sid': True,
        }
        return QueryO(**query_data)
    