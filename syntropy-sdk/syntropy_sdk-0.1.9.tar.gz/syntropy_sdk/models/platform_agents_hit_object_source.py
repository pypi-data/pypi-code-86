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


class PlatformAgentsHitObjectSource(object):
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
    swagger_types = {"agent_id": "float", "severity": "str", "timestamp": "datetime"}

    attribute_map = {
        "agent_id": "agent_id",
        "severity": "severity",
        "timestamp": "@timestamp",
    }

    def __init__(self, agent_id=None, severity=None, timestamp=None):  # noqa: E501
        """PlatformAgentsHitObjectSource - a model defined in Swagger"""  # noqa: E501
        self._agent_id = None
        self._severity = None
        self._timestamp = None
        self.discriminator = None
        self.agent_id = agent_id
        self.severity = severity
        self.timestamp = timestamp

    @property
    def agent_id(self):
        """Gets the agent_id of this PlatformAgentsHitObjectSource.  # noqa: E501


        :return: The agent_id of this PlatformAgentsHitObjectSource.  # noqa: E501
        :rtype: float
        """
        return self._agent_id

    @agent_id.setter
    def agent_id(self, agent_id):
        """Sets the agent_id of this PlatformAgentsHitObjectSource.


        :param agent_id: The agent_id of this PlatformAgentsHitObjectSource.  # noqa: E501
        :type: float
        """
        if agent_id is None:
            raise ValueError(
                "Invalid value for `agent_id`, must not be `None`"
            )  # noqa: E501

        self._agent_id = agent_id

    @property
    def severity(self):
        """Gets the severity of this PlatformAgentsHitObjectSource.  # noqa: E501


        :return: The severity of this PlatformAgentsHitObjectSource.  # noqa: E501
        :rtype: str
        """
        return self._severity

    @severity.setter
    def severity(self, severity):
        """Sets the severity of this PlatformAgentsHitObjectSource.


        :param severity: The severity of this PlatformAgentsHitObjectSource.  # noqa: E501
        :type: str
        """
        if severity is None:
            raise ValueError(
                "Invalid value for `severity`, must not be `None`"
            )  # noqa: E501
        allowed_values = ["WARN", "ERROR"]  # noqa: E501
        if severity not in allowed_values:
            raise ValueError(
                "Invalid value for `severity` ({0}), must be one of {1}".format(  # noqa: E501
                    severity, allowed_values
                )
            )

        self._severity = severity

    @property
    def timestamp(self):
        """Gets the timestamp of this PlatformAgentsHitObjectSource.  # noqa: E501


        :return: The timestamp of this PlatformAgentsHitObjectSource.  # noqa: E501
        :rtype: datetime
        """
        return self._timestamp

    @timestamp.setter
    def timestamp(self, timestamp):
        """Sets the timestamp of this PlatformAgentsHitObjectSource.


        :param timestamp: The timestamp of this PlatformAgentsHitObjectSource.  # noqa: E501
        :type: datetime
        """
        if timestamp is None:
            raise ValueError(
                "Invalid value for `timestamp`, must not be `None`"
            )  # noqa: E501

        self._timestamp = timestamp

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
        if issubclass(PlatformAgentsHitObjectSource, dict):
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
        if not isinstance(other, PlatformAgentsHitObjectSource):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
