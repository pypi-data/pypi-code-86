try:
	from zcrmsdk.src.com.zoho.crm.api.exception import SDKException
	from zcrmsdk.src.com.zoho.crm.api.util import Constants
	from zcrmsdk.src.com.zoho.crm.api.blue_print.response_handler import ResponseHandler
except Exception:
	from ..exception import SDKException
	from ..util import Constants
	from .response_handler import ResponseHandler


class ResponseWrapper(ResponseHandler):
	def __init__(self):
		"""Creates an instance of ResponseWrapper"""
		super().__init__()

		self.__blueprint = None
		self.__key_modified = dict()

	def get_blueprint(self):
		"""
		The method to get the blueprint

		Returns:
			BluePrint: An instance of BluePrint
		"""

		return self.__blueprint

	def set_blueprint(self, blueprint):
		"""
		The method to set the value to blueprint

		Parameters:
			blueprint (BluePrint) : An instance of BluePrint
		"""

		try:
			from zcrmsdk.src.com.zoho.crm.api.blue_print.blue_print import BluePrint
		except Exception:
			from .blue_print import BluePrint

		if blueprint is not None and not isinstance(blueprint, BluePrint):
			raise SDKException(Constants.DATA_TYPE_ERROR, 'KEY: blueprint EXPECTED TYPE: BluePrint', None, None)
		
		self.__blueprint = blueprint
		self.__key_modified['blueprint'] = 1

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
