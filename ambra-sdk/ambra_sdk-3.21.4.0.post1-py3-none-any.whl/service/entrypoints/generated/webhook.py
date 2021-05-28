""" Webhook.

Do not edit this file by hand.
This is generated by parsing api.html service doc.
"""
from ambra_sdk.exceptions.service import AccountNotFound
from ambra_sdk.exceptions.service import CustomNotHash
from ambra_sdk.exceptions.service import FdcJwtInvalidPrivateKey
from ambra_sdk.exceptions.service import IncompleteFilter
from ambra_sdk.exceptions.service import InvalidCron
from ambra_sdk.exceptions.service import InvalidEvent
from ambra_sdk.exceptions.service import InvalidFilterField
from ambra_sdk.exceptions.service import InvalidJson
from ambra_sdk.exceptions.service import InvalidMethod
from ambra_sdk.exceptions.service import InvalidRegexp
from ambra_sdk.exceptions.service import InvalidTransformCondition
from ambra_sdk.exceptions.service import InvalidType
from ambra_sdk.exceptions.service import InvalidWebhookSetup
from ambra_sdk.exceptions.service import MissingFields
from ambra_sdk.exceptions.service import NodeNotFound
from ambra_sdk.exceptions.service import NotFound
from ambra_sdk.exceptions.service import NotHash
from ambra_sdk.exceptions.service import NotPermitted
from ambra_sdk.exceptions.service import NotWithCron
from ambra_sdk.exceptions.service import ParseFailed
from ambra_sdk.exceptions.service import SfdcJwtMissingFields
from ambra_sdk.exceptions.service import SfdcJwtNotHash
from ambra_sdk.exceptions.service import SfdcMissingFields
from ambra_sdk.exceptions.service import SfdcNotHash
from ambra_sdk.exceptions.service import SidUserNotFound
from ambra_sdk.exceptions.service import SidUserNotInAccount
from ambra_sdk.exceptions.service import UserNotFound
from ambra_sdk.service.query import QueryO

class Webhook:
    """Webhook."""

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
        errors_mapping[('MISSING_FIELDS', None)] = MissingFields('A required field is missing or does not have data in it. The error_subtype holds a array of all the missing fields')
        errors_mapping[('NOT_FOUND', None)] = NotFound('The account can not be found')
        errors_mapping[('NOT_PERMITTED', None)] = NotPermitted('You are not permitted to view this list')
        query_data = {
            'api': self._api,
            'url': '/webhook/list',
            'request_data': request_data,
            'errors_mapping': errors_mapping,
            'required_sid': True,
        }
        return QueryO(**query_data)
    
    def add(
        self,
        account_id,
        event,
        method,
        name,
        url,
        auth=None,
        by_accession_number=None,
        by_uid=None,
        by_webhook_event=None,
        cron=None,
        delay=None,
        filter_field=None,
        filter_regexp=None,
        max_age=None,
        node_id=None,
        once=None,
        parameters=None,
        retry=None,
        sid_user_id=None,
        suspended=None,
    ):
        """Add.
        :param account_id: uuid of the account
        :param event: Event to call it on (See the notes for the available events)
        :param method: Method to call it with (POST|GET|POST_JSON|PUT|GET_JSON)
        :param name: Name of the webhook
        :param url: URL to call
        :param auth: A JSON hash with the authentication details (optional)
        :param by_accession_number: Flag to expand the once search to include studies with the same accession_number (optional)
        :param by_uid: Flag to expand the once search to include studies with the same study_uid (optional)
        :param by_webhook_event: Flag to fire WEBHOOK_FAILED once at final unsuccessful try of a failing webhook (optional)
        :param cron: Cron timing string for CRON events e.g 0 9 * * mon-fri(optional)
        :param delay: Number of seconds to delay running this webhook for after it is triggered (optional)
        :param filter_field: Name of the study field (by default) or another object's field (should have prefix like "webhook.") to filter on (optional)
        :param filter_regexp: Regular expression to match the value of the filter_field against (optional)
        :param max_age: Ignore studies that are more than this number of days old based on the study_date (optional)
        :param node_id: uuid of the node to proxy the webhook through (optional)
        :param once: Flag that this webhook should only be run once for a specific study (optional)
        :param parameters: A JSON object of the parameter names and values (optional)
        :param retry: Retry the webhook if it fails (optional)
        :param sid_user_id: UUID of the user to generate a sid as (optional)
        :param suspended: This webhook is suspended and not triggered (optional)
        """
        request_data = {
           'account_id': account_id,
           'auth': auth,
           'by_accession_number': by_accession_number,
           'by_uid': by_uid,
           'by_webhook_event': by_webhook_event,
           'cron': cron,
           'delay': delay,
           'event': event,
           'filter_field': filter_field,
           'filter_regexp': filter_regexp,
           'max_age': max_age,
           'method': method,
           'name': name,
           'node_id': node_id,
           'once': once,
           'parameters': parameters,
           'retry': retry,
           'sid_user_id': sid_user_id,
           'suspended': suspended,
           'url': url,
        }
	
        errors_mapping = {}
        errors_mapping[('ACCOUNT_NOT_FOUND', None)] = AccountNotFound('The account can not be found')
        errors_mapping[('CUSTOM_NOT_HASH', None)] = CustomNotHash('The custom auth value is not a JSON hash')
        errors_mapping[('FDC_JWT_INVALID_PRIVATE_KEY', None)] = FdcJwtInvalidPrivateKey('The private key is invalid')
        errors_mapping[('INCOMPLETE_FILTER', None)] = IncompleteFilter('Both a field and regexp are required')
        errors_mapping[('INVALID_CRON', None)] = InvalidCron('The cron value is invalid')
        errors_mapping[('INVALID_EVENT', None)] = InvalidEvent('An invalid event was passed')
        errors_mapping[('INVALID_FILTER_FIELD', None)] = InvalidFilterField('Invalid filter field name')
        errors_mapping[('INVALID_JSON', None)] = InvalidJson('The parameters field is not in valid JSON format.')
        errors_mapping[('INVALID_METHOD', None)] = InvalidMethod('An invalid method was passed')
        errors_mapping[('INVALID_REGEXP', None)] = InvalidRegexp('Invalid regular expression')
        errors_mapping[('INVALID_TRANSFORM_CONDITION', None)] = InvalidTransformCondition('The transform condition is invalid')
        errors_mapping[('MISSING_FIELDS', None)] = MissingFields('A required field is missing or does not have data in it. The error_subtype holds a array of all the missing fields')
        errors_mapping[('NODE_NOT_FOUND', None)] = NodeNotFound('The node can not be found')
        errors_mapping[('NOT_HASH', None)] = NotHash('The parameter or auth field is not a hash.')
        errors_mapping[('NOT_PERMITTED', None)] = NotPermitted('You are not permitted to add a webhook to this account')
        errors_mapping[('NOT_WITH_CRON', None)] = NotWithCron('The delay or retry option can not be used for cron events')
        errors_mapping[('SFDC_JWT_MISSING_FIELDS', None)] = SfdcJwtMissingFields('Fields are missing for the SFDC auth hash')
        errors_mapping[('SFDC_JWT_NOT_HASH', None)] = SfdcJwtNotHash('The SFDC auth value is not a JSON hash')
        errors_mapping[('SFDC_MISSING_FIELDS', None)] = SfdcMissingFields('Fields are missing for the SFDC auth hash')
        errors_mapping[('SFDC_NOT_HASH', None)] = SfdcNotHash('The SFDC auth value is not a JSON hash')
        errors_mapping[('SID_USER_NOT_FOUND', None)] = SidUserNotFound('The sid user can not be found')
        errors_mapping[('SID_USER_NOT_IN_ACCOUNT', None)] = SidUserNotInAccount('The sid user is not a member of this account')
        errors_mapping[('USER_NOT_FOUND', None)] = UserNotFound('The basic authentication user can not be found')
        query_data = {
            'api': self._api,
            'url': '/webhook/add',
            'request_data': request_data,
            'errors_mapping': errors_mapping,
            'required_sid': True,
        }
        return QueryO(**query_data)
    
    def set(
        self,
        uuid,
        auth=None,
        by_accession_number=None,
        by_uid=None,
        by_webhook_event=None,
        cron=None,
        delay=None,
        event=None,
        filter_field=None,
        filter_regexp=None,
        max_age=None,
        method=None,
        name=None,
        node_id=None,
        once=None,
        parameters=None,
        retry=None,
        sid_user_id=None,
        suspended=None,
        url=None,
    ):
        """Set.
        :param uuid: uuid of the webhook
        :param auth: A JSON hash with the authentication details (optional)
        :param by_accession_number: Flag to expand the once search to include studies with the same accession_number (optional)
        :param by_uid: Flag to expand the once search to include studies with the same study_uid (optional)
        :param by_webhook_event: Flag to fire WEBHOOK_FAILED once at final unsuccessful try of a failing webhook (optional)
        :param cron: Cron timing string for CRON events (optional)
        :param delay: Number of seconds to delay running this webhook for after it is triggered (optional)
        :param event: Event to call it on (optional see add command for options)
        :param filter_field: Name of the field to filter on (optional)
        :param filter_regexp: Regular expression to match the value of the filter_field against (optional)
        :param max_age: Ignore studies that are more than this number of days old based on the study_date (optional)
        :param method: Method to call it with (optional see add command for options)
        :param name: Name of the webhook (optional)
        :param node_id: uuid of the node to proxy the webhook through (optional)
        :param once: Flag that this webhook should only be run once for a specific study (optional)
        :param parameters: A JSON object of the parameter names and values (optional see add command for options)
        :param retry: Retry the webhook if it fails (optional)
        :param sid_user_id: UUID of the user to generate a sid as (optional)
        :param suspended: This webhook is suspended and not triggered (optional)
        :param url: URL to call (optional)
        """
        request_data = {
           'auth': auth,
           'by_accession_number': by_accession_number,
           'by_uid': by_uid,
           'by_webhook_event': by_webhook_event,
           'cron': cron,
           'delay': delay,
           'event': event,
           'filter_field': filter_field,
           'filter_regexp': filter_regexp,
           'max_age': max_age,
           'method': method,
           'name': name,
           'node_id': node_id,
           'once': once,
           'parameters': parameters,
           'retry': retry,
           'sid_user_id': sid_user_id,
           'suspended': suspended,
           'url': url,
           'uuid': uuid,
        }
	
        errors_mapping = {}
        errors_mapping[('INCOMPLETE_FILTER', None)] = IncompleteFilter('Both a field and regexp are required')
        errors_mapping[('INVALID_CRON', None)] = InvalidCron('The cron value is invalid')
        errors_mapping[('INVALID_EVENT', None)] = InvalidEvent('An invalid event was passed')
        errors_mapping[('INVALID_FILTER_FIELD', None)] = InvalidFilterField('Invalid filter field name')
        errors_mapping[('INVALID_JSON', None)] = InvalidJson('The parameters field is not in valid JSON format.')
        errors_mapping[('INVALID_METHOD', None)] = InvalidMethod('An invalid method was passed')
        errors_mapping[('INVALID_REGEXP', None)] = InvalidRegexp('Invalid regular expression')
        errors_mapping[('INVALID_TRANSFORM_CONDITION', None)] = InvalidTransformCondition('The transform condition is invalid')
        errors_mapping[('MISSING_FIELDS', None)] = MissingFields('A required field is missing or does not have data in it. The error_subtype holds a array of all the missing fields')
        errors_mapping[('NODE_NOT_FOUND', None)] = NodeNotFound('The node can not be found')
        errors_mapping[('NOT_FOUND', None)] = NotFound('The webhook can not be found')
        errors_mapping[('NOT_HASH', None)] = NotHash('The parameter field is not a hash.')
        errors_mapping[('NOT_PERMITTED', None)] = NotPermitted('You are not permitted to edit the webhook')
        errors_mapping[('NOT_WITH_CRON', None)] = NotWithCron('The delay or retry option can not be used for cron events')
        errors_mapping[('SFDC_MISSING_FIELDS', None)] = SfdcMissingFields('Fields are missing for the SFDC auth hash')
        errors_mapping[('SFDC_NOT_HASH', None)] = SfdcNotHash('The SFDC auth value is not a JSON hash')
        errors_mapping[('SID_USER_NOT_FOUND', None)] = SidUserNotFound('The sid user can not be found')
        errors_mapping[('SID_USER_NOT_IN_ACCOUNT', None)] = SidUserNotInAccount('The sid user is not a member of this account')
        query_data = {
            'api': self._api,
            'url': '/webhook/set',
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
        :param uuid: uuid of the webhook
        """
        request_data = {
           'uuid': uuid,
        }
	
        errors_mapping = {}
        errors_mapping[('MISSING_FIELDS', None)] = MissingFields('A required field is missing or does not have data in it. The error_subtype holds a array of all the missing fields')
        errors_mapping[('NOT_FOUND', None)] = NotFound('The webhook can not be found')
        errors_mapping[('NOT_PERMITTED', None)] = NotPermitted('You are not permitted to view the webhook')
        query_data = {
            'api': self._api,
            'url': '/webhook/get',
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
        :param uuid: uuid of the webhook
        """
        request_data = {
           'uuid': uuid,
        }
	
        errors_mapping = {}
        errors_mapping[('MISSING_FIELDS', None)] = MissingFields('A required field is missing or does not have data in it. The error_subtype holds a array of all the missing fields')
        errors_mapping[('NOT_FOUND', None)] = NotFound('The webhook can not be found')
        errors_mapping[('NOT_PERMITTED', None)] = NotPermitted('You are not permitted to delete the webhook')
        query_data = {
            'api': self._api,
            'url': '/webhook/delete',
            'request_data': request_data,
            'errors_mapping': errors_mapping,
            'required_sid': True,
        }
        return QueryO(**query_data)
    
    def trigger(
        self,
        study_id,
        uuid,
    ):
        """Trigger.
        :param study_id: uuid of the study to fire the webhook for
        :param uuid: uuid of the webhook
        """
        request_data = {
           'study_id': study_id,
           'uuid': uuid,
        }
	
        errors_mapping = {}
        errors_mapping[('MISSING_FIELDS', None)] = MissingFields('A required field is missing or does not have data in it. The error_subtype holds a array of all the missing fields')
        errors_mapping[('NOT_FOUND', None)] = NotFound('The webhook or study can not be found')
        errors_mapping[('NOT_PERMITTED', None)] = NotPermitted('You are not permitted to trigger the webhook')
        query_data = {
            'api': self._api,
            'url': '/webhook/trigger',
            'request_data': request_data,
            'errors_mapping': errors_mapping,
            'required_sid': True,
        }
        return QueryO(**query_data)
    
    def run(
        self,
        study_id,
        uuid,
    ):
        """Run.
        :param study_id: uuid of the study to run the webhook for
        :param uuid: uuid of the webhook
        """
        request_data = {
           'study_id': study_id,
           'uuid': uuid,
        }
	
        errors_mapping = {}
        errors_mapping[('INVALID_WEBHOOK_SETUP', None)] = InvalidWebhookSetup('The webhook must be a MANUAL webhook with no delay or retry options enabled')
        errors_mapping[('MISSING_FIELDS', None)] = MissingFields('A required field is missing or does not have data in it. The error_subtype holds a array of all the missing fields')
        errors_mapping[('NOT_FOUND', None)] = NotFound('The webhook or study can not be found')
        errors_mapping[('NOT_PERMITTED', None)] = NotPermitted('You are not permitted to run the webhook')
        query_data = {
            'api': self._api,
            'url': '/webhook/run',
            'request_data': request_data,
            'errors_mapping': errors_mapping,
            'required_sid': True,
        }
        return QueryO(**query_data)
    
    def event(
        self,
        type,
        integration_key=None,
        namespace_id=None,
        share_code=None,
        study_count=None,
    ):
        """Event.
        :param type: The type of event (STUDY_UPLOAD_START|STUDY_UPLOAD_END)
        :param integration_key: The integration key associated with the event (optional)
        :param namespace_id: namespace_id
        :param share_code: share_code
        :param study_count: The number of studies associated with the event (optional)
        """
        request_data = {
           'integration_key': integration_key,
           'namespace_id': namespace_id,
           'share_code': share_code,
           'study_count': study_count,
           'type': type,
        }
	
        errors_mapping = {}
        errors_mapping[('INVALID_TYPE', None)] = InvalidType('Invalid event type')
        errors_mapping[('MISSING_FIELDS', None)] = MissingFields('A required field is missing or does not have data in it. The error_subtype holds a array of all the missing fields')
        query_data = {
            'api': self._api,
            'url': '/webhook/event',
            'request_data': request_data,
            'errors_mapping': errors_mapping,
            'required_sid': True,
        }
        return QueryO(**query_data)
    
    def email(
        self,
        html,
        subject,
        template_id,
        text,
        to,
        webhook_id,
    ):
        """Email.
        :param html: The HTML part of the email
        :param subject: The subject of the email
        :param template_id: The email template UUID to be used
        :param text: The text part of the email
        :param to: The email address(es) to send the email to
        :param webhook_id: The uuid of the calling webhook
        """
        request_data = {
           'html': html,
           'subject': subject,
           'template_id': template_id,
           'text': text,
           'to': to,
           'webhook_id': webhook_id,
        }
	
        errors_mapping = {}
        errors_mapping[('MISSING_FIELDS', None)] = MissingFields('A required field is missing or does not have data in it. The error_subtype holds a array of all the missing fields')
        errors_mapping[('NOT_PERMITTED', None)] = NotPermitted('This is not a call from a valid webhook')
        errors_mapping[('PARSE_FAILED', None)] = ParseFailed('Template parsing failed for a field. The error_subtype holds the name of the field')
        query_data = {
            'api': self._api,
            'url': '/webhook/email',
            'request_data': request_data,
            'errors_mapping': errors_mapping,
            'required_sid': False,
        }
        return QueryO(**query_data)
    