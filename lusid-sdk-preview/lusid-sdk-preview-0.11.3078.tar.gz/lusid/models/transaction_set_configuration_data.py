# coding: utf-8

"""
    LUSID API

    FINBOURNE Technology  # noqa: E501

    The version of the OpenAPI document: 0.11.3078
    Contact: info@finbourne.com
    Generated by: https://openapi-generator.tech
"""


import pprint
import re  # noqa: F401

import six

class TransactionSetConfigurationData(object):
    """NOTE: This class is auto generated by OpenAPI Generator.
    Ref: https://openapi-generator.tech

    Do not edit the class manually.
    """

    """
    Attributes:
      openapi_types (dict): The key is attribute name
                            and the value is attribute type.
      attribute_map (dict): The key is attribute name
                            and the value is json key in definition.
      required_map (dict): The key is attribute name
                           and the value is whether it is 'required' or 'optional'.
    """
    openapi_types = {
        'transaction_configs': 'list[TransactionConfigurationData]',
        'side_definitions': 'list[SideConfigurationData]',
        'links': 'list[Link]'
    }

    attribute_map = {
        'transaction_configs': 'transactionConfigs',
        'side_definitions': 'sideDefinitions',
        'links': 'links'
    }

    required_map = {
        'transaction_configs': 'required',
        'side_definitions': 'optional',
        'links': 'optional'
    }

    def __init__(self, transaction_configs=None, side_definitions=None, links=None):  # noqa: E501
        """
        TransactionSetConfigurationData - a model defined in OpenAPI

        :param transaction_configs:  Collection of transaction type models (required)
        :type transaction_configs: list[lusid.TransactionConfigurationData]
        :param side_definitions:  Collection of side definitions
        :type side_definitions: list[lusid.SideConfigurationData]
        :param links: 
        :type links: list[lusid.Link]

        """  # noqa: E501

        self._transaction_configs = None
        self._side_definitions = None
        self._links = None
        self.discriminator = None

        self.transaction_configs = transaction_configs
        self.side_definitions = side_definitions
        self.links = links

    @property
    def transaction_configs(self):
        """Gets the transaction_configs of this TransactionSetConfigurationData.  # noqa: E501

        Collection of transaction type models  # noqa: E501

        :return: The transaction_configs of this TransactionSetConfigurationData.  # noqa: E501
        :rtype: list[TransactionConfigurationData]
        """
        return self._transaction_configs

    @transaction_configs.setter
    def transaction_configs(self, transaction_configs):
        """Sets the transaction_configs of this TransactionSetConfigurationData.

        Collection of transaction type models  # noqa: E501

        :param transaction_configs: The transaction_configs of this TransactionSetConfigurationData.  # noqa: E501
        :type: list[TransactionConfigurationData]
        """
        if transaction_configs is None:
            raise ValueError("Invalid value for `transaction_configs`, must not be `None`")  # noqa: E501

        self._transaction_configs = transaction_configs

    @property
    def side_definitions(self):
        """Gets the side_definitions of this TransactionSetConfigurationData.  # noqa: E501

        Collection of side definitions  # noqa: E501

        :return: The side_definitions of this TransactionSetConfigurationData.  # noqa: E501
        :rtype: list[SideConfigurationData]
        """
        return self._side_definitions

    @side_definitions.setter
    def side_definitions(self, side_definitions):
        """Sets the side_definitions of this TransactionSetConfigurationData.

        Collection of side definitions  # noqa: E501

        :param side_definitions: The side_definitions of this TransactionSetConfigurationData.  # noqa: E501
        :type: list[SideConfigurationData]
        """

        self._side_definitions = side_definitions

    @property
    def links(self):
        """Gets the links of this TransactionSetConfigurationData.  # noqa: E501


        :return: The links of this TransactionSetConfigurationData.  # noqa: E501
        :rtype: list[Link]
        """
        return self._links

    @links.setter
    def links(self, links):
        """Sets the links of this TransactionSetConfigurationData.


        :param links: The links of this TransactionSetConfigurationData.  # noqa: E501
        :type: list[Link]
        """

        self._links = links

    def to_dict(self):
        """Returns the model properties as a dict"""
        result = {}

        for attr, _ in six.iteritems(self.openapi_types):
            value = getattr(self, attr)
            if isinstance(value, list):
                result[attr] = list(map(
                    lambda x: x.to_dict() if hasattr(x, "to_dict") else x,
                    value
                ))
            elif hasattr(value, "to_dict"):
                result[attr] = value.to_dict()
            elif isinstance(value, dict):
                result[attr] = dict(map(
                    lambda item: (item[0], item[1].to_dict())
                    if hasattr(item[1], "to_dict") else item,
                    value.items()
                ))
            else:
                result[attr] = value

        return result

    def to_str(self):
        """Returns the string representation of the model"""
        return pprint.pformat(self.to_dict())

    def __repr__(self):
        """For `print` and `pprint`"""
        return self.to_str()

    def __eq__(self, other):
        """Returns true if both objects are equal"""
        if not isinstance(other, TransactionSetConfigurationData):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
