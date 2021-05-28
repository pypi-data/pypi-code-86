try:
	from zcrmsdk.src.com.zoho.crm.api.exception import SDKException
	from zcrmsdk.src.com.zoho.crm.api.util import Constants
	from zcrmsdk.src.com.zoho.crm.api.pipeline.transfer_action_handler import TransferActionHandler
except Exception:
	from ..exception import SDKException
	from ..util import Constants
	from .transfer_action_handler import TransferActionHandler


class TransferActionWrapper(TransferActionHandler):
	def __init__(self):
		"""Creates an instance of TransferActionWrapper"""
		super().__init__()

		self.__transfer_pipeline = None
		self.__key_modified = dict()

	def get_transfer_pipeline(self):
		"""
		The method to get the transfer_pipeline

		Returns:
			list: An instance of list
		"""

		return self.__transfer_pipeline

	def set_transfer_pipeline(self, transfer_pipeline):
		"""
		The method to set the value to transfer_pipeline

		Parameters:
			transfer_pipeline (list) : An instance of list
		"""

		if transfer_pipeline is not None and not isinstance(transfer_pipeline, list):
			raise SDKException(Constants.DATA_TYPE_ERROR, 'KEY: transfer_pipeline EXPECTED TYPE: list', None, None)
		
		self.__transfer_pipeline = transfer_pipeline
		self.__key_modified['transfer_pipeline'] = 1

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
