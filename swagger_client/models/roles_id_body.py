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

class RolesIdBody(object):
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
        'description': 'str',
        'enforce_tfa': 'bool',
        'external_id': 'str',
        'ip_access': 'list[str]',
        'module_listing': 'str',
        'name': 'str'
    }

    attribute_map = {
        'description': 'description',
        'enforce_tfa': 'enforce_tfa',
        'external_id': 'external_id',
        'ip_access': 'ip_access',
        'module_listing': 'module_listing',
        'name': 'name'
    }

    def __init__(self, description=None, enforce_tfa=None, external_id=None, ip_access=None, module_listing=None, name=None):  # noqa: E501
        """RolesIdBody - a model defined in Swagger"""  # noqa: E501
        self._description = None
        self._enforce_tfa = None
        self._external_id = None
        self._ip_access = None
        self._module_listing = None
        self._name = None
        self.discriminator = None
        if description is not None:
            self.description = description
        if enforce_tfa is not None:
            self.enforce_tfa = enforce_tfa
        if external_id is not None:
            self.external_id = external_id
        if ip_access is not None:
            self.ip_access = ip_access
        if module_listing is not None:
            self.module_listing = module_listing
        if name is not None:
            self.name = name

    @property
    def description(self):
        """Gets the description of this RolesIdBody.  # noqa: E501

        Description of the role.  # noqa: E501

        :return: The description of this RolesIdBody.  # noqa: E501
        :rtype: str
        """
        return self._description

    @description.setter
    def description(self, description):
        """Sets the description of this RolesIdBody.

        Description of the role.  # noqa: E501

        :param description: The description of this RolesIdBody.  # noqa: E501
        :type: str
        """

        self._description = description

    @property
    def enforce_tfa(self):
        """Gets the enforce_tfa of this RolesIdBody.  # noqa: E501

        Whether or not this role enforces the use of 2FA.  # noqa: E501

        :return: The enforce_tfa of this RolesIdBody.  # noqa: E501
        :rtype: bool
        """
        return self._enforce_tfa

    @enforce_tfa.setter
    def enforce_tfa(self, enforce_tfa):
        """Sets the enforce_tfa of this RolesIdBody.

        Whether or not this role enforces the use of 2FA.  # noqa: E501

        :param enforce_tfa: The enforce_tfa of this RolesIdBody.  # noqa: E501
        :type: bool
        """

        self._enforce_tfa = enforce_tfa

    @property
    def external_id(self):
        """Gets the external_id of this RolesIdBody.  # noqa: E501

        ID used with external services in SCIM.  # noqa: E501

        :return: The external_id of this RolesIdBody.  # noqa: E501
        :rtype: str
        """
        return self._external_id

    @external_id.setter
    def external_id(self, external_id):
        """Sets the external_id of this RolesIdBody.

        ID used with external services in SCIM.  # noqa: E501

        :param external_id: The external_id of this RolesIdBody.  # noqa: E501
        :type: str
        """

        self._external_id = external_id

    @property
    def ip_access(self):
        """Gets the ip_access of this RolesIdBody.  # noqa: E501

        Array of IP addresses that are allowed to connect to the API as a user of this role.  # noqa: E501

        :return: The ip_access of this RolesIdBody.  # noqa: E501
        :rtype: list[str]
        """
        return self._ip_access

    @ip_access.setter
    def ip_access(self, ip_access):
        """Sets the ip_access of this RolesIdBody.

        Array of IP addresses that are allowed to connect to the API as a user of this role.  # noqa: E501

        :param ip_access: The ip_access of this RolesIdBody.  # noqa: E501
        :type: list[str]
        """

        self._ip_access = ip_access

    @property
    def module_listing(self):
        """Gets the module_listing of this RolesIdBody.  # noqa: E501

        Custom override for the admin app module bar navigation.  # noqa: E501

        :return: The module_listing of this RolesIdBody.  # noqa: E501
        :rtype: str
        """
        return self._module_listing

    @module_listing.setter
    def module_listing(self, module_listing):
        """Sets the module_listing of this RolesIdBody.

        Custom override for the admin app module bar navigation.  # noqa: E501

        :param module_listing: The module_listing of this RolesIdBody.  # noqa: E501
        :type: str
        """

        self._module_listing = module_listing

    @property
    def name(self):
        """Gets the name of this RolesIdBody.  # noqa: E501

        Name of the role.  # noqa: E501

        :return: The name of this RolesIdBody.  # noqa: E501
        :rtype: str
        """
        return self._name

    @name.setter
    def name(self, name):
        """Sets the name of this RolesIdBody.

        Name of the role.  # noqa: E501

        :param name: The name of this RolesIdBody.  # noqa: E501
        :type: str
        """

        self._name = name

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
        if issubclass(RolesIdBody, dict):
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
        if not isinstance(other, RolesIdBody):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
