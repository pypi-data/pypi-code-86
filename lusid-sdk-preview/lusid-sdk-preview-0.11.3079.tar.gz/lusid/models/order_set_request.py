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

class OrderSetRequest(object):
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
        'order_requests': 'list[OrderRequest]'
    }

    attribute_map = {
        'order_requests': 'orderRequests'
    }

    required_map = {
        'order_requests': 'optional'
    }

    def __init__(self, order_requests=None):  # noqa: E501
        """
        OrderSetRequest - a model defined in OpenAPI

        :param order_requests:  A collection of OrderRequests.
        :type order_requests: list[lusid.OrderRequest]

        """  # noqa: E501

        self._order_requests = None
        self.discriminator = None

        self.order_requests = order_requests

    @property
    def order_requests(self):
        """Gets the order_requests of this OrderSetRequest.  # noqa: E501

        A collection of OrderRequests.  # noqa: E501

        :return: The order_requests of this OrderSetRequest.  # noqa: E501
        :rtype: list[OrderRequest]
        """
        return self._order_requests

    @order_requests.setter
    def order_requests(self, order_requests):
        """Sets the order_requests of this OrderSetRequest.

        A collection of OrderRequests.  # noqa: E501

        :param order_requests: The order_requests of this OrderSetRequest.  # noqa: E501
        :type: list[OrderRequest]
        """

        self._order_requests = order_requests

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
        if not isinstance(other, OrderSetRequest):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
