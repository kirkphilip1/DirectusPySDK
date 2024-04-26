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

class FieldsCollectionBody(object):
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
        'field': 'str',
        'type': 'str',
        'schema': 'FieldscollectionSchema',
        'meta': 'FieldscollectionMeta'
    }

    attribute_map = {
        'field': 'field',
        'type': 'type',
        'schema': 'schema',
        'meta': 'meta'
    }

    def __init__(self, field=None, type=None, schema=None, meta=None):  # noqa: E501
        """FieldsCollectionBody - a model defined in Swagger"""  # noqa: E501
        self._field = None
        self._type = None
        self._schema = None
        self._meta = None
        self.discriminator = None
        self.field = field
        self.type = type
        if schema is not None:
            self.schema = schema
        if meta is not None:
            self.meta = meta

    @property
    def field(self):
        """Gets the field of this FieldsCollectionBody.  # noqa: E501

        Unique name of the field. Field name is unique within the collection.  # noqa: E501

        :return: The field of this FieldsCollectionBody.  # noqa: E501
        :rtype: str
        """
        return self._field

    @field.setter
    def field(self, field):
        """Sets the field of this FieldsCollectionBody.

        Unique name of the field. Field name is unique within the collection.  # noqa: E501

        :param field: The field of this FieldsCollectionBody.  # noqa: E501
        :type: str
        """
        if field is None:
            raise ValueError("Invalid value for `field`, must not be `None`")  # noqa: E501

        self._field = field

    @property
    def type(self):
        """Gets the type of this FieldsCollectionBody.  # noqa: E501

        Directus specific data type. Used to cast values in the API.  # noqa: E501

        :return: The type of this FieldsCollectionBody.  # noqa: E501
        :rtype: str
        """
        return self._type

    @type.setter
    def type(self, type):
        """Sets the type of this FieldsCollectionBody.

        Directus specific data type. Used to cast values in the API.  # noqa: E501

        :param type: The type of this FieldsCollectionBody.  # noqa: E501
        :type: str
        """
        if type is None:
            raise ValueError("Invalid value for `type`, must not be `None`")  # noqa: E501

        self._type = type

    @property
    def schema(self):
        """Gets the schema of this FieldsCollectionBody.  # noqa: E501


        :return: The schema of this FieldsCollectionBody.  # noqa: E501
        :rtype: FieldscollectionSchema
        """
        return self._schema

    @schema.setter
    def schema(self, schema):
        """Sets the schema of this FieldsCollectionBody.


        :param schema: The schema of this FieldsCollectionBody.  # noqa: E501
        :type: FieldscollectionSchema
        """

        self._schema = schema

    @property
    def meta(self):
        """Gets the meta of this FieldsCollectionBody.  # noqa: E501


        :return: The meta of this FieldsCollectionBody.  # noqa: E501
        :rtype: FieldscollectionMeta
        """
        return self._meta

    @meta.setter
    def meta(self, meta):
        """Sets the meta of this FieldsCollectionBody.


        :param meta: The meta of this FieldsCollectionBody.  # noqa: E501
        :type: FieldscollectionMeta
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
        if issubclass(FieldsCollectionBody, dict):
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
        if not isinstance(other, FieldsCollectionBody):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other