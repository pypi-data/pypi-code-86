try:
	from zcrmsdk.src.com.zoho.crm.api.exception import SDKException
	from zcrmsdk.src.com.zoho.crm.api.util import Constants
	from zcrmsdk.src.com.zoho.crm.api.send_mail import Template
except Exception:
	from ..exception import SDKException
	from ..util import Constants
	from ..send_mail import Template


class EmailTemplate(Template):
	def __init__(self):
		"""Creates an instance of EmailTemplate"""
		super().__init__()

		self.__content = None
		self.__created_time = None
		self.__subject = None
		self.__module = None
		self.__type = None
		self.__created_by = None
		self.__modified_time = None
		self.__last_usage_time = None
		self.__associated = None
		self.__name = None
		self.__modified_by = None
		self.__description = None
		self.__id = None
		self.__editor_mode = None
		self.__favorite = None
		self.__attachments = None
		self.__folder = None
		self.__consent_linked = None
		self.__key_modified = dict()

	def get_content(self):
		"""
		The method to get the content

		Returns:
			string: A string representing the content
		"""

		return self.__content

	def set_content(self, content):
		"""
		The method to set the value to content

		Parameters:
			content (string) : A string representing the content
		"""

		if content is not None and not isinstance(content, str):
			raise SDKException(Constants.DATA_TYPE_ERROR, 'KEY: content EXPECTED TYPE: str', None, None)
		
		self.__content = content
		self.__key_modified['content'] = 1

	def get_created_time(self):
		"""
		The method to get the created_time

		Returns:
			datetime: An instance of datetime
		"""

		return self.__created_time

	def set_created_time(self, created_time):
		"""
		The method to set the value to created_time

		Parameters:
			created_time (datetime) : An instance of datetime
		"""

		from datetime import datetime

		if created_time is not None and not isinstance(created_time, datetime):
			raise SDKException(Constants.DATA_TYPE_ERROR, 'KEY: created_time EXPECTED TYPE: datetime', None, None)
		
		self.__created_time = created_time
		self.__key_modified['created_time'] = 1

	def get_subject(self):
		"""
		The method to get the subject

		Returns:
			string: A string representing the subject
		"""

		return self.__subject

	def set_subject(self, subject):
		"""
		The method to set the value to subject

		Parameters:
			subject (string) : A string representing the subject
		"""

		if subject is not None and not isinstance(subject, str):
			raise SDKException(Constants.DATA_TYPE_ERROR, 'KEY: subject EXPECTED TYPE: str', None, None)
		
		self.__subject = subject
		self.__key_modified['subject'] = 1

	def get_module(self):
		"""
		The method to get the module

		Returns:
			Module: An instance of Module
		"""

		return self.__module

	def set_module(self, module):
		"""
		The method to set the value to module

		Parameters:
			module (Module) : An instance of Module
		"""

		try:
			from zcrmsdk.src.com.zoho.crm.api.modules import Module
		except Exception:
			from ..modules import Module

		if module is not None and not isinstance(module, Module):
			raise SDKException(Constants.DATA_TYPE_ERROR, 'KEY: module EXPECTED TYPE: Module', None, None)
		
		self.__module = module
		self.__key_modified['module'] = 1

	def get_type(self):
		"""
		The method to get the type

		Returns:
			string: A string representing the type
		"""

		return self.__type

	def set_type(self, type):
		"""
		The method to set the value to type

		Parameters:
			type (string) : A string representing the type
		"""

		if type is not None and not isinstance(type, str):
			raise SDKException(Constants.DATA_TYPE_ERROR, 'KEY: type EXPECTED TYPE: str', None, None)
		
		self.__type = type
		self.__key_modified['type'] = 1

	def get_created_by(self):
		"""
		The method to get the created_by

		Returns:
			User: An instance of User
		"""

		return self.__created_by

	def set_created_by(self, created_by):
		"""
		The method to set the value to created_by

		Parameters:
			created_by (User) : An instance of User
		"""

		try:
			from zcrmsdk.src.com.zoho.crm.api.users import User
		except Exception:
			from ..users import User

		if created_by is not None and not isinstance(created_by, User):
			raise SDKException(Constants.DATA_TYPE_ERROR, 'KEY: created_by EXPECTED TYPE: User', None, None)
		
		self.__created_by = created_by
		self.__key_modified['created_by'] = 1

	def get_modified_time(self):
		"""
		The method to get the modified_time

		Returns:
			datetime: An instance of datetime
		"""

		return self.__modified_time

	def set_modified_time(self, modified_time):
		"""
		The method to set the value to modified_time

		Parameters:
			modified_time (datetime) : An instance of datetime
		"""

		from datetime import datetime

		if modified_time is not None and not isinstance(modified_time, datetime):
			raise SDKException(Constants.DATA_TYPE_ERROR, 'KEY: modified_time EXPECTED TYPE: datetime', None, None)
		
		self.__modified_time = modified_time
		self.__key_modified['modified_time'] = 1

	def get_last_usage_time(self):
		"""
		The method to get the last_usage_time

		Returns:
			datetime: An instance of datetime
		"""

		return self.__last_usage_time

	def set_last_usage_time(self, last_usage_time):
		"""
		The method to set the value to last_usage_time

		Parameters:
			last_usage_time (datetime) : An instance of datetime
		"""

		from datetime import datetime

		if last_usage_time is not None and not isinstance(last_usage_time, datetime):
			raise SDKException(Constants.DATA_TYPE_ERROR, 'KEY: last_usage_time EXPECTED TYPE: datetime', None, None)
		
		self.__last_usage_time = last_usage_time
		self.__key_modified['last_usage_time'] = 1

	def get_associated(self):
		"""
		The method to get the associated

		Returns:
			bool: A bool representing the associated
		"""

		return self.__associated

	def set_associated(self, associated):
		"""
		The method to set the value to associated

		Parameters:
			associated (bool) : A bool representing the associated
		"""

		if associated is not None and not isinstance(associated, bool):
			raise SDKException(Constants.DATA_TYPE_ERROR, 'KEY: associated EXPECTED TYPE: bool', None, None)
		
		self.__associated = associated
		self.__key_modified['associated'] = 1

	def get_name(self):
		"""
		The method to get the name

		Returns:
			string: A string representing the name
		"""

		return self.__name

	def set_name(self, name):
		"""
		The method to set the value to name

		Parameters:
			name (string) : A string representing the name
		"""

		if name is not None and not isinstance(name, str):
			raise SDKException(Constants.DATA_TYPE_ERROR, 'KEY: name EXPECTED TYPE: str', None, None)
		
		self.__name = name
		self.__key_modified['name'] = 1

	def get_modified_by(self):
		"""
		The method to get the modified_by

		Returns:
			User: An instance of User
		"""

		return self.__modified_by

	def set_modified_by(self, modified_by):
		"""
		The method to set the value to modified_by

		Parameters:
			modified_by (User) : An instance of User
		"""

		try:
			from zcrmsdk.src.com.zoho.crm.api.users import User
		except Exception:
			from ..users import User

		if modified_by is not None and not isinstance(modified_by, User):
			raise SDKException(Constants.DATA_TYPE_ERROR, 'KEY: modified_by EXPECTED TYPE: User', None, None)
		
		self.__modified_by = modified_by
		self.__key_modified['modified_by'] = 1

	def get_description(self):
		"""
		The method to get the description

		Returns:
			string: A string representing the description
		"""

		return self.__description

	def set_description(self, description):
		"""
		The method to set the value to description

		Parameters:
			description (string) : A string representing the description
		"""

		if description is not None and not isinstance(description, str):
			raise SDKException(Constants.DATA_TYPE_ERROR, 'KEY: description EXPECTED TYPE: str', None, None)
		
		self.__description = description
		self.__key_modified['description'] = 1

	def get_id(self):
		"""
		The method to get the id

		Returns:
			int: An int representing the id
		"""

		return self.__id

	def set_id(self, id):
		"""
		The method to set the value to id

		Parameters:
			id (int) : An int representing the id
		"""

		if id is not None and not isinstance(id, int):
			raise SDKException(Constants.DATA_TYPE_ERROR, 'KEY: id EXPECTED TYPE: int', None, None)
		
		self.__id = id
		self.__key_modified['id'] = 1

	def get_editor_mode(self):
		"""
		The method to get the editor_mode

		Returns:
			string: A string representing the editor_mode
		"""

		return self.__editor_mode

	def set_editor_mode(self, editor_mode):
		"""
		The method to set the value to editor_mode

		Parameters:
			editor_mode (string) : A string representing the editor_mode
		"""

		if editor_mode is not None and not isinstance(editor_mode, str):
			raise SDKException(Constants.DATA_TYPE_ERROR, 'KEY: editor_mode EXPECTED TYPE: str', None, None)
		
		self.__editor_mode = editor_mode
		self.__key_modified['editor_mode'] = 1

	def get_favorite(self):
		"""
		The method to get the favorite

		Returns:
			bool: A bool representing the favorite
		"""

		return self.__favorite

	def set_favorite(self, favorite):
		"""
		The method to set the value to favorite

		Parameters:
			favorite (bool) : A bool representing the favorite
		"""

		if favorite is not None and not isinstance(favorite, bool):
			raise SDKException(Constants.DATA_TYPE_ERROR, 'KEY: favorite EXPECTED TYPE: bool', None, None)
		
		self.__favorite = favorite
		self.__key_modified['favorite'] = 1

	def get_attachments(self):
		"""
		The method to get the attachments

		Returns:
			list: An instance of list
		"""

		return self.__attachments

	def set_attachments(self, attachments):
		"""
		The method to set the value to attachments

		Parameters:
			attachments (list) : An instance of list
		"""

		if attachments is not None and not isinstance(attachments, list):
			raise SDKException(Constants.DATA_TYPE_ERROR, 'KEY: attachments EXPECTED TYPE: list', None, None)
		
		self.__attachments = attachments
		self.__key_modified['attachments'] = 1

	def get_folder(self):
		"""
		The method to get the folder

		Returns:
			EmailTemplate: An instance of EmailTemplate
		"""

		return self.__folder

	def set_folder(self, folder):
		"""
		The method to set the value to folder

		Parameters:
			folder (EmailTemplate) : An instance of EmailTemplate
		"""

		try:
			from zcrmsdk.src.com.zoho.crm.api.email_templates.email_template import EmailTemplate
		except Exception:
			from .email_template import EmailTemplate

		if folder is not None and not isinstance(folder, EmailTemplate):
			raise SDKException(Constants.DATA_TYPE_ERROR, 'KEY: folder EXPECTED TYPE: EmailTemplate', None, None)
		
		self.__folder = folder
		self.__key_modified['folder'] = 1

	def get_consent_linked(self):
		"""
		The method to get the consent_linked

		Returns:
			bool: A bool representing the consent_linked
		"""

		return self.__consent_linked

	def set_consent_linked(self, consent_linked):
		"""
		The method to set the value to consent_linked

		Parameters:
			consent_linked (bool) : A bool representing the consent_linked
		"""

		if consent_linked is not None and not isinstance(consent_linked, bool):
			raise SDKException(Constants.DATA_TYPE_ERROR, 'KEY: consent_linked EXPECTED TYPE: bool', None, None)
		
		self.__consent_linked = consent_linked
		self.__key_modified['consent_linked'] = 1

	def is_key_modified(self, key):
		"""
		The method to check if the user has modified the given key

		Parameters:
			key (string) : A string representing the key

		Returns:
			int: An int representing the modification
		"""

		if key is not None and not isinstance(key, str):
			raise SDKException(Constants.DATA_TYPE_ERROR, 'KEY: key EXPECTED TYPE: str', None, None)
		
		if key in self.__key_modified:
			return self.__key_modified.get(key)
		
		return None

	def set_key_modified(self, key, modification):
		"""
		The method to mark the given key as modified

		Parameters:
			key (string) : A string representing the key
			modification (int) : An int representing the modification
		"""

		if key is not None and not isinstance(key, str):
			raise SDKException(Constants.DATA_TYPE_ERROR, 'KEY: key EXPECTED TYPE: str', None, None)
		
		if modification is not None and not isinstance(modification, int):
			raise SDKException(Constants.DATA_TYPE_ERROR, 'KEY: modification EXPECTED TYPE: int', None, None)
		
		self.__key_modified[key] = modification
