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


class TsoaPartialTunnelObject_(object):
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
        "tunnel_id": "float",
        "server_src_id": "float",
        "server_dst_id": "float",
        "interface_src_id": "float",
        "tunnel_cidr_ipv6": "str",
        "tunnel_status": "Status",
        "tunnel_status_reason": "str",
    }

    attribute_map = {
        "tunnel_id": "tunnel_id",
        "server_src_id": "server_src_id",
        "server_dst_id": "server_dst_id",
        "interface_src_id": "interface_src_id",
        "tunnel_cidr_ipv6": "tunnel_cidr_ipv6",
        "tunnel_status": "tunnel_status",
        "tunnel_status_reason": "tunnel_status_reason",
    }

    def __init__(
        self,
        tunnel_id=None,
        server_src_id=None,
        server_dst_id=None,
        interface_src_id=None,
        tunnel_cidr_ipv6=None,
        tunnel_status=None,
        tunnel_status_reason=None,
    ):  # noqa: E501
        """TsoaPartialTunnelObject_ - a model defined in Swagger"""  # noqa: E501
        self._tunnel_id = None
        self._server_src_id = None
        self._server_dst_id = None
        self._interface_src_id = None
        self._tunnel_cidr_ipv6 = None
        self._tunnel_status = None
        self._tunnel_status_reason = None
        self.discriminator = None
        if tunnel_id is not None:
            self.tunnel_id = tunnel_id
        if server_src_id is not None:
            self.server_src_id = server_src_id
        if server_dst_id is not None:
            self.server_dst_id = server_dst_id
        if interface_src_id is not None:
            self.interface_src_id = interface_src_id
        if tunnel_cidr_ipv6 is not None:
            self.tunnel_cidr_ipv6 = tunnel_cidr_ipv6
        if tunnel_status is not None:
            self.tunnel_status = tunnel_status
        if tunnel_status_reason is not None:
            self.tunnel_status_reason = tunnel_status_reason

    @property
    def tunnel_id(self):
        """Gets the tunnel_id of this TsoaPartialTunnelObject_.  # noqa: E501


        :return: The tunnel_id of this TsoaPartialTunnelObject_.  # noqa: E501
        :rtype: float
        """
        return self._tunnel_id

    @tunnel_id.setter
    def tunnel_id(self, tunnel_id):
        """Sets the tunnel_id of this TsoaPartialTunnelObject_.


        :param tunnel_id: The tunnel_id of this TsoaPartialTunnelObject_.  # noqa: E501
        :type: float
        """

        self._tunnel_id = tunnel_id

    @property
    def server_src_id(self):
        """Gets the server_src_id of this TsoaPartialTunnelObject_.  # noqa: E501


        :return: The server_src_id of this TsoaPartialTunnelObject_.  # noqa: E501
        :rtype: float
        """
        return self._server_src_id

    @server_src_id.setter
    def server_src_id(self, server_src_id):
        """Sets the server_src_id of this TsoaPartialTunnelObject_.


        :param server_src_id: The server_src_id of this TsoaPartialTunnelObject_.  # noqa: E501
        :type: float
        """

        self._server_src_id = server_src_id

    @property
    def server_dst_id(self):
        """Gets the server_dst_id of this TsoaPartialTunnelObject_.  # noqa: E501


        :return: The server_dst_id of this TsoaPartialTunnelObject_.  # noqa: E501
        :rtype: float
        """
        return self._server_dst_id

    @server_dst_id.setter
    def server_dst_id(self, server_dst_id):
        """Sets the server_dst_id of this TsoaPartialTunnelObject_.


        :param server_dst_id: The server_dst_id of this TsoaPartialTunnelObject_.  # noqa: E501
        :type: float
        """

        self._server_dst_id = server_dst_id

    @property
    def interface_src_id(self):
        """Gets the interface_src_id of this TsoaPartialTunnelObject_.  # noqa: E501


        :return: The interface_src_id of this TsoaPartialTunnelObject_.  # noqa: E501
        :rtype: float
        """
        return self._interface_src_id

    @interface_src_id.setter
    def interface_src_id(self, interface_src_id):
        """Sets the interface_src_id of this TsoaPartialTunnelObject_.


        :param interface_src_id: The interface_src_id of this TsoaPartialTunnelObject_.  # noqa: E501
        :type: float
        """

        self._interface_src_id = interface_src_id

    @property
    def tunnel_cidr_ipv6(self):
        """Gets the tunnel_cidr_ipv6 of this TsoaPartialTunnelObject_.  # noqa: E501


        :return: The tunnel_cidr_ipv6 of this TsoaPartialTunnelObject_.  # noqa: E501
        :rtype: str
        """
        return self._tunnel_cidr_ipv6

    @tunnel_cidr_ipv6.setter
    def tunnel_cidr_ipv6(self, tunnel_cidr_ipv6):
        """Sets the tunnel_cidr_ipv6 of this TsoaPartialTunnelObject_.


        :param tunnel_cidr_ipv6: The tunnel_cidr_ipv6 of this TsoaPartialTunnelObject_.  # noqa: E501
        :type: str
        """

        self._tunnel_cidr_ipv6 = tunnel_cidr_ipv6

    @property
    def tunnel_status(self):
        """Gets the tunnel_status of this TsoaPartialTunnelObject_.  # noqa: E501


        :return: The tunnel_status of this TsoaPartialTunnelObject_.  # noqa: E501
        :rtype: Status
        """
        return self._tunnel_status

    @tunnel_status.setter
    def tunnel_status(self, tunnel_status):
        """Sets the tunnel_status of this TsoaPartialTunnelObject_.


        :param tunnel_status: The tunnel_status of this TsoaPartialTunnelObject_.  # noqa: E501
        :type: Status
        """

        self._tunnel_status = tunnel_status

    @property
    def tunnel_status_reason(self):
        """Gets the tunnel_status_reason of this TsoaPartialTunnelObject_.  # noqa: E501


        :return: The tunnel_status_reason of this TsoaPartialTunnelObject_.  # noqa: E501
        :rtype: str
        """
        return self._tunnel_status_reason

    @tunnel_status_reason.setter
    def tunnel_status_reason(self, tunnel_status_reason):
        """Sets the tunnel_status_reason of this TsoaPartialTunnelObject_.


        :param tunnel_status_reason: The tunnel_status_reason of this TsoaPartialTunnelObject_.  # noqa: E501
        :type: str
        """

        self._tunnel_status_reason = tunnel_status_reason

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
        if issubclass(TsoaPartialTunnelObject_, dict):
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
        if not isinstance(other, TsoaPartialTunnelObject_):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
