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

class ExportCollectionBody(object):
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
        'format': 'str',
        'query': 'Query',
        'file': 'Files'
    }

    attribute_map = {
        'format': 'format',
        'query': 'query',
        'file': 'file'
    }

    def __init__(self, format=None, query=None, file=None):  # noqa: E501
        """ExportCollectionBody - a model defined in Swagger"""  # noqa: E501
        self._format = None
        self._query = None
        self._file = None
        self.discriminator = None
        self.format = format
        self.query = query
        self.file = file

    @property
    def format(self):
        """Gets the format of this ExportCollectionBody.  # noqa: E501

        What file format to save the export to. One of csv, xml, json  # noqa: E501

        :return: The format of this ExportCollectionBody.  # noqa: E501
        :rtype: str
        """
        return self._format

    @format.setter
    def format(self, format):
        """Sets the format of this ExportCollectionBody.

        What file format to save the export to. One of csv, xml, json  # noqa: E501

        :param format: The format of this ExportCollectionBody.  # noqa: E501
        :type: str
        """
        if format is None:
            raise ValueError("Invalid value for `format`, must not be `None`")  # noqa: E501
        allowed_values = ["csv", "xml", "json"]  # noqa: E501
        if format not in allowed_values:
            raise ValueError(
                "Invalid value for `format` ({0}), must be one of {1}"  # noqa: E501
                .format(format, allowed_values)
            )

        self._format = format

    @property
    def query(self):
        """Gets the query of this ExportCollectionBody.  # noqa: E501


        :return: The query of this ExportCollectionBody.  # noqa: E501
        :rtype: Query
        """
        return self._query

    @query.setter
    def query(self, query):
        """Sets the query of this ExportCollectionBody.


        :param query: The query of this ExportCollectionBody.  # noqa: E501
        :type: Query
        """
        if query is None:
            raise ValueError("Invalid value for `query`, must not be `None`")  # noqa: E501

        self._query = query

    @property
    def file(self):
        """Gets the file of this ExportCollectionBody.  # noqa: E501


        :return: The file of this ExportCollectionBody.  # noqa: E501
        :rtype: Files
        """
        return self._file

    @file.setter
    def file(self, file):
        """Sets the file of this ExportCollectionBody.


        :param file: The file of this ExportCollectionBody.  # noqa: E501
        :type: Files
        """
        if file is None:
            raise ValueError("Invalid value for `file`, must not be `None`")  # noqa: E501

        self._file = file

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
        if issubclass(ExportCollectionBody, dict):
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
        if not isinstance(other, ExportCollectionBody):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
