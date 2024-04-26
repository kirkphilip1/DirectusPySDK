# coding: utf-8

"""
    Dynamic API Specification

    This is a dynamically generated API specification for all endpoints existing on the current project.  # noqa: E501

    OpenAPI spec version: 10.10.5
    
    Generated by: https://github.com/swagger-api/swagger-codegen.git
"""

import pprint
import re  # noqa: F401

import six

class InlineResponse20027(object):
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
        'data': 'list[Operations]',
        'meta': 'XMetadata'
    }

    attribute_map = {
        'data': 'data',
        'meta': 'meta'
    }

    def __init__(self, data=None, meta=None):  # noqa: E501
        """InlineResponse20027 - a model defined in Swagger"""  # noqa: E501
        self._data = None
        self._meta = None
        self.discriminator = None
        if data is not None:
            self.data = data
        if meta is not None:
            self.meta = meta

    @property
    def data(self):
        """Gets the data of this InlineResponse20027.  # noqa: E501


        :return: The data of this InlineResponse20027.  # noqa: E501
        :rtype: list[Operations]
        """
        return self._data

    @data.setter
    def data(self, data):
        """Sets the data of this InlineResponse20027.


        :param data: The data of this InlineResponse20027.  # noqa: E501
        :type: list[Operations]
        """

        self._data = data

    @property
    def meta(self):
        """Gets the meta of this InlineResponse20027.  # noqa: E501


        :return: The meta of this InlineResponse20027.  # noqa: E501
        :rtype: XMetadata
        """
        return self._meta

    @meta.setter
    def meta(self, meta):
        """Sets the meta of this InlineResponse20027.


        :param meta: The meta of this InlineResponse20027.  # noqa: E501
        :type: XMetadata
        """

        self._meta = meta

    def to_dict(self):
        """Returns the model properties as a dict"""
        result = {}

        for attr, _ in six.iteritems(self.swagger_types):
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
        if issubclass(InlineResponse20027, dict):
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
        if not isinstance(other, InlineResponse20027):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
