# coding: utf-8

"""
    syntropy-controller

    No description provided (generated by Swagger Codegen https://github.com/swagger-api/swagger-codegen)  # noqa: E501

    OpenAPI spec version: 0.1.0
    
    Generated by: https://github.com/swagger-api/swagger-codegen.git
"""

import pprint
import re  # noqa: F401

import six


class TsoaPartialInterfaceObject_(object):
    """NOTE: This class is auto generated by the swagger code generator program.

    Do not edit the class manually.
    """

    """
    Attributes:
      swagger_types (dict): The key is attribute name
                            and the value is attribute type.
      attribute_map (dict): The key is attribute name
                            and the value is json key in definition.
    """
    swagger_types = {
        "interface_name": "str",
        "interface_type": "InterfaceType",
        "server_id": "float",
        "server_cidr_ipv4": "str",
        "server_cidr_ipv6": "str",
        "interface_monitoring_cidr": "str",
        "interface_kvm_gateway_ipv4": "str",
        "interface_additional_routes_cidrs": "str",
    }

    attribute_map = {
        "interface_name": "interface_name",
        "interface_type": "interface_type",
        "server_id": "server_id",
        "server_cidr_ipv4": "server_cidr_ipv4",
        "server_cidr_ipv6": "server_cidr_ipv6",
        "interface_monitoring_cidr": "interface_monitoring_cidr",
        "interface_kvm_gateway_ipv4": "interface_kvm_gateway_ipv4",
        "interface_additional_routes_cidrs": "interface_additional_routes_cidrs",
    }

    def __init__(
        self,
        interface_name=None,
        interface_type=None,
        server_id=None,
        server_cidr_ipv4=None,
        server_cidr_ipv6=None,
        interface_monitoring_cidr=None,
        interface_kvm_gateway_ipv4=None,
        interface_additional_routes_cidrs=None,
    ):  # noqa: E501
        """TsoaPartialInterfaceObject_ - a model defined in Swagger"""  # noqa: E501
        self._interface_name = None
        self._interface_type = None
        self._server_id = None
        self._server_cidr_ipv4 = None
        self._server_cidr_ipv6 = None
        self._interface_monitoring_cidr = None
        self._interface_kvm_gateway_ipv4 = None
        self._interface_additional_routes_cidrs = None
        self.discriminator = None
        if interface_name is not None:
            self.interface_name = interface_name
        if interface_type is not None:
            self.interface_type = interface_type
        if server_id is not None:
            self.server_id = server_id
        if server_cidr_ipv4 is not None:
            self.server_cidr_ipv4 = server_cidr_ipv4
        if server_cidr_ipv6 is not None:
            self.server_cidr_ipv6 = server_cidr_ipv6
        if interface_monitoring_cidr is not None:
            self.interface_monitoring_cidr = interface_monitoring_cidr
        if interface_kvm_gateway_ipv4 is not None:
            self.interface_kvm_gateway_ipv4 = interface_kvm_gateway_ipv4
        if interface_additional_routes_cidrs is not None:
            self.interface_additional_routes_cidrs = interface_additional_routes_cidrs

    @property
    def interface_name(self):
        """Gets the interface_name of this TsoaPartialInterfaceObject_.  # noqa: E501


        :return: The interface_name of this TsoaPartialInterfaceObject_.  # noqa: E501
        :rtype: str
        """
        return self._interface_name

    @interface_name.setter
    def interface_name(self, interface_name):
        """Sets the interface_name of this TsoaPartialInterfaceObject_.


        :param interface_name: The interface_name of this TsoaPartialInterfaceObject_.  # noqa: E501
        :type: str
        """

        self._interface_name = interface_name

    @property
    def interface_type(self):
        """Gets the interface_type of this TsoaPartialInterfaceObject_.  # noqa: E501


        :return: The interface_type of this TsoaPartialInterfaceObject_.  # noqa: E501
        :rtype: InterfaceType
        """
        return self._interface_type

    @interface_type.setter
    def interface_type(self, interface_type):
        """Sets the interface_type of this TsoaPartialInterfaceObject_.


        :param interface_type: The interface_type of this TsoaPartialInterfaceObject_.  # noqa: E501
        :type: InterfaceType
        """

        self._interface_type = interface_type

    @property
    def server_id(self):
        """Gets the server_id of this TsoaPartialInterfaceObject_.  # noqa: E501


        :return: The server_id of this TsoaPartialInterfaceObject_.  # noqa: E501
        :rtype: float
        """
        return self._server_id

    @server_id.setter
    def server_id(self, server_id):
        """Sets the server_id of this TsoaPartialInterfaceObject_.


        :param server_id: The server_id of this TsoaPartialInterfaceObject_.  # noqa: E501
        :type: float
        """

        self._server_id = server_id

    @property
    def server_cidr_ipv4(self):
        """Gets the server_cidr_ipv4 of this TsoaPartialInterfaceObject_.  # noqa: E501


        :return: The server_cidr_ipv4 of this TsoaPartialInterfaceObject_.  # noqa: E501
        :rtype: str
        """
        return self._server_cidr_ipv4

    @server_cidr_ipv4.setter
    def server_cidr_ipv4(self, server_cidr_ipv4):
        """Sets the server_cidr_ipv4 of this TsoaPartialInterfaceObject_.


        :param server_cidr_ipv4: The server_cidr_ipv4 of this TsoaPartialInterfaceObject_.  # noqa: E501
        :type: str
        """

        self._server_cidr_ipv4 = server_cidr_ipv4

    @property
    def server_cidr_ipv6(self):
        """Gets the server_cidr_ipv6 of this TsoaPartialInterfaceObject_.  # noqa: E501


        :return: The server_cidr_ipv6 of this TsoaPartialInterfaceObject_.  # noqa: E501
        :rtype: str
        """
        return self._server_cidr_ipv6

    @server_cidr_ipv6.setter
    def server_cidr_ipv6(self, server_cidr_ipv6):
        """Sets the server_cidr_ipv6 of this TsoaPartialInterfaceObject_.


        :param server_cidr_ipv6: The server_cidr_ipv6 of this TsoaPartialInterfaceObject_.  # noqa: E501
        :type: str
        """

        self._server_cidr_ipv6 = server_cidr_ipv6

    @property
    def interface_monitoring_cidr(self):
        """Gets the interface_monitoring_cidr of this TsoaPartialInterfaceObject_.  # noqa: E501


        :return: The interface_monitoring_cidr of this TsoaPartialInterfaceObject_.  # noqa: E501
        :rtype: str
        """
        return self._interface_monitoring_cidr

    @interface_monitoring_cidr.setter
    def interface_monitoring_cidr(self, interface_monitoring_cidr):
        """Sets the interface_monitoring_cidr of this TsoaPartialInterfaceObject_.


        :param interface_monitoring_cidr: The interface_monitoring_cidr of this TsoaPartialInterfaceObject_.  # noqa: E501
        :type: str
        """

        self._interface_monitoring_cidr = interface_monitoring_cidr

    @property
    def interface_kvm_gateway_ipv4(self):
        """Gets the interface_kvm_gateway_ipv4 of this TsoaPartialInterfaceObject_.  # noqa: E501


        :return: The interface_kvm_gateway_ipv4 of this TsoaPartialInterfaceObject_.  # noqa: E501
        :rtype: str
        """
        return self._interface_kvm_gateway_ipv4

    @interface_kvm_gateway_ipv4.setter
    def interface_kvm_gateway_ipv4(self, interface_kvm_gateway_ipv4):
        """Sets the interface_kvm_gateway_ipv4 of this TsoaPartialInterfaceObject_.


        :param interface_kvm_gateway_ipv4: The interface_kvm_gateway_ipv4 of this TsoaPartialInterfaceObject_.  # noqa: E501
        :type: str
        """

        self._interface_kvm_gateway_ipv4 = interface_kvm_gateway_ipv4

    @property
    def interface_additional_routes_cidrs(self):
        """Gets the interface_additional_routes_cidrs of this TsoaPartialInterfaceObject_.  # noqa: E501


        :return: The interface_additional_routes_cidrs of this TsoaPartialInterfaceObject_.  # noqa: E501
        :rtype: str
        """
        return self._interface_additional_routes_cidrs

    @interface_additional_routes_cidrs.setter
    def interface_additional_routes_cidrs(self, interface_additional_routes_cidrs):
        """Sets the interface_additional_routes_cidrs of this TsoaPartialInterfaceObject_.


        :param interface_additional_routes_cidrs: The interface_additional_routes_cidrs of this TsoaPartialInterfaceObject_.  # noqa: E501
        :type: str
        """

        self._interface_additional_routes_cidrs = interface_additional_routes_cidrs

    def to_dict(self):
        """Returns the model properties as a dict"""
        result = {}

        for attr, _ in six.iteritems(self.swagger_types):
            value = getattr(self, attr)
            if isinstance(value, list):
                result[attr] = list(
                    map(lambda x: x.to_dict() if hasattr(x, "to_dict") else x, value)
                )
            elif hasattr(value, "to_dict"):
                result[attr] = value.to_dict()
            elif isinstance(value, dict):
                result[attr] = dict(
                    map(
                        lambda item: (item[0], item[1].to_dict())
                        if hasattr(item[1], "to_dict")
                        else item,
                        value.items(),
                    )
                )
            else:
                result[attr] = value
        if issubclass(TsoaPartialInterfaceObject_, dict):
            for key, value in self.items():
                result[key] = value

        return result

    def to_str(self):
        """Returns the string representation of the model"""
        return pprint.pformat(self.to_dict())

    def __repr__(self):
        """For `print` and `pprint`"""
        return self.to_str()

    def __eq__(self, other):
        """Returns true if both objects are equal"""
        if not isinstance(other, TsoaPartialInterfaceObject_):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
