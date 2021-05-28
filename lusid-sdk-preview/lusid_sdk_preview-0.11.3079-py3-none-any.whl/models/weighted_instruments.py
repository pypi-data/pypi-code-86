# coding: utf-8

"""
    LUSID API

    FINBOURNE Technology  # noqa: E501

    The version of the OpenAPI document: 0.11.3079
    Contact: info@finbourne.com
    Generated by: https://openapi-generator.tech
"""


import pprint
import re  # noqa: F401

import six

class WeightedInstruments(object):
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
        'instruments': 'list[WeightedInstrument]'
    }

    attribute_map = {
        'instruments': 'instruments'
    }

    required_map = {
        'instruments': 'required'
    }

    def __init__(self, instruments=None):  # noqa: E501
        """
        WeightedInstruments - a model defined in OpenAPI

        :param instruments:  The instruments that are held in the set. (required)
        :type instruments: list[lusid.WeightedInstrument]

        """  # noqa: E501

        self._instruments = None
        self.discriminator = None

        self.instruments = instruments

    @property
    def instruments(self):
        """Gets the instruments of this WeightedInstruments.  # noqa: E501

        The instruments that are held in the set.  # noqa: E501

        :return: The instruments of this WeightedInstruments.  # noqa: E501
        :rtype: list[WeightedInstrument]
        """
        return self._instruments

    @instruments.setter
    def instruments(self, instruments):
        """Sets the instruments of this WeightedInstruments.

        The instruments that are held in the set.  # noqa: E501

        :param instruments: The instruments of this WeightedInstruments.  # noqa: E501
        :type: list[WeightedInstrument]
        """
        if instruments is None:
            raise ValueError("Invalid value for `instruments`, must not be `None`")  # noqa: E501

        self._instruments = instruments

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
        if not isinstance(other, WeightedInstruments):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
