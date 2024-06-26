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

class Users(object):
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
        'id': 'str',
        'first_name': 'str',
        'last_name': 'str',
        'email': 'str',
        'password': 'str',
        'location': 'str',
        'title': 'str',
        'description': 'str',
        'tags': 'list[str]',
        'avatar': 'OneOfUsersAvatar',
        'language': 'str',
        'tfa_secret': 'str',
        'status': 'str',
        'role': 'OneOfUsersRole',
        'token': 'str',
        'last_access': 'datetime',
        'last_page': 'str',
        'provider': 'str',
        'external_identifier': 'str',
        'auth_data': 'object',
        'email_notifications': 'bool',
        'appearance': 'str',
        'theme_dark': 'str',
        'theme_light': 'str',
        'theme_light_overrides': 'object',
        'theme_dark_overrides': 'object'
    }

    attribute_map = {
        'id': 'id',
        'first_name': 'first_name',
        'last_name': 'last_name',
        'email': 'email',
        'password': 'password',
        'location': 'location',
        'title': 'title',
        'description': 'description',
        'tags': 'tags',
        'avatar': 'avatar',
        'language': 'language',
        'tfa_secret': 'tfa_secret',
        'status': 'status',
        'role': 'role',
        'token': 'token',
        'last_access': 'last_access',
        'last_page': 'last_page',
        'provider': 'provider',
        'external_identifier': 'external_identifier',
        'auth_data': 'auth_data',
        'email_notifications': 'email_notifications',
        'appearance': 'appearance',
        'theme_dark': 'theme_dark',
        'theme_light': 'theme_light',
        'theme_light_overrides': 'theme_light_overrides',
        'theme_dark_overrides': 'theme_dark_overrides'
    }

    def __init__(self, id=None, first_name=None, last_name=None, email=None, password=None, location=None, title=None, description=None, tags=None, avatar=None, language=None, tfa_secret=None, status=None, role=None, token=None, last_access=None, last_page=None, provider=None, external_identifier=None, auth_data=None, email_notifications=None, appearance=None, theme_dark=None, theme_light=None, theme_light_overrides=None, theme_dark_overrides=None):  # noqa: E501
        """Users - a model defined in Swagger"""  # noqa: E501
        self._id = None
        self._first_name = None
        self._last_name = None
        self._email = None
        self._password = None
        self._location = None
        self._title = None
        self._description = None
        self._tags = None
        self._avatar = None
        self._language = None
        self._tfa_secret = None
        self._status = None
        self._role = None
        self._token = None
        self._last_access = None
        self._last_page = None
        self._provider = None
        self._external_identifier = None
        self._auth_data = None
        self._email_notifications = None
        self._appearance = None
        self._theme_dark = None
        self._theme_light = None
        self._theme_light_overrides = None
        self._theme_dark_overrides = None
        self.discriminator = None
        if id is not None:
            self.id = id
        if first_name is not None:
            self.first_name = first_name
        if last_name is not None:
            self.last_name = last_name
        if email is not None:
            self.email = email
        if password is not None:
            self.password = password
        if location is not None:
            self.location = location
        if title is not None:
            self.title = title
        if description is not None:
            self.description = description
        if tags is not None:
            self.tags = tags
        if avatar is not None:
            self.avatar = avatar
        if language is not None:
            self.language = language
        if tfa_secret is not None:
            self.tfa_secret = tfa_secret
        if status is not None:
            self.status = status
        if role is not None:
            self.role = role
        if token is not None:
            self.token = token
        if last_access is not None:
            self.last_access = last_access
        if last_page is not None:
            self.last_page = last_page
        if provider is not None:
            self.provider = provider
        if external_identifier is not None:
            self.external_identifier = external_identifier
        if auth_data is not None:
            self.auth_data = auth_data
        if email_notifications is not None:
            self.email_notifications = email_notifications
        if appearance is not None:
            self.appearance = appearance
        if theme_dark is not None:
            self.theme_dark = theme_dark
        if theme_light is not None:
            self.theme_light = theme_light
        if theme_light_overrides is not None:
            self.theme_light_overrides = theme_light_overrides
        if theme_dark_overrides is not None:
            self.theme_dark_overrides = theme_dark_overrides

    @property
    def id(self):
        """Gets the id of this Users.  # noqa: E501

        Unique identifier for the user.  # noqa: E501

        :return: The id of this Users.  # noqa: E501
        :rtype: str
        """
        return self._id

    @id.setter
    def id(self, id):
        """Sets the id of this Users.

        Unique identifier for the user.  # noqa: E501

        :param id: The id of this Users.  # noqa: E501
        :type: str
        """

        self._id = id

    @property
    def first_name(self):
        """Gets the first_name of this Users.  # noqa: E501

        First name of the user.  # noqa: E501

        :return: The first_name of this Users.  # noqa: E501
        :rtype: str
        """
        return self._first_name

    @first_name.setter
    def first_name(self, first_name):
        """Sets the first_name of this Users.

        First name of the user.  # noqa: E501

        :param first_name: The first_name of this Users.  # noqa: E501
        :type: str
        """

        self._first_name = first_name

    @property
    def last_name(self):
        """Gets the last_name of this Users.  # noqa: E501

        Last name of the user.  # noqa: E501

        :return: The last_name of this Users.  # noqa: E501
        :rtype: str
        """
        return self._last_name

    @last_name.setter
    def last_name(self, last_name):
        """Sets the last_name of this Users.

        Last name of the user.  # noqa: E501

        :param last_name: The last_name of this Users.  # noqa: E501
        :type: str
        """

        self._last_name = last_name

    @property
    def email(self):
        """Gets the email of this Users.  # noqa: E501

        Unique email address for the user.  # noqa: E501

        :return: The email of this Users.  # noqa: E501
        :rtype: str
        """
        return self._email

    @email.setter
    def email(self, email):
        """Sets the email of this Users.

        Unique email address for the user.  # noqa: E501

        :param email: The email of this Users.  # noqa: E501
        :type: str
        """

        self._email = email

    @property
    def password(self):
        """Gets the password of this Users.  # noqa: E501

        Password of the user.  # noqa: E501

        :return: The password of this Users.  # noqa: E501
        :rtype: str
        """
        return self._password

    @password.setter
    def password(self, password):
        """Sets the password of this Users.

        Password of the user.  # noqa: E501

        :param password: The password of this Users.  # noqa: E501
        :type: str
        """

        self._password = password

    @property
    def location(self):
        """Gets the location of this Users.  # noqa: E501

        The user's location.  # noqa: E501

        :return: The location of this Users.  # noqa: E501
        :rtype: str
        """
        return self._location

    @location.setter
    def location(self, location):
        """Sets the location of this Users.

        The user's location.  # noqa: E501

        :param location: The location of this Users.  # noqa: E501
        :type: str
        """

        self._location = location

    @property
    def title(self):
        """Gets the title of this Users.  # noqa: E501

        The user's title.  # noqa: E501

        :return: The title of this Users.  # noqa: E501
        :rtype: str
        """
        return self._title

    @title.setter
    def title(self, title):
        """Sets the title of this Users.

        The user's title.  # noqa: E501

        :param title: The title of this Users.  # noqa: E501
        :type: str
        """

        self._title = title

    @property
    def description(self):
        """Gets the description of this Users.  # noqa: E501

        The user's description.  # noqa: E501

        :return: The description of this Users.  # noqa: E501
        :rtype: str
        """
        return self._description

    @description.setter
    def description(self, description):
        """Sets the description of this Users.

        The user's description.  # noqa: E501

        :param description: The description of this Users.  # noqa: E501
        :type: str
        """

        self._description = description

    @property
    def tags(self):
        """Gets the tags of this Users.  # noqa: E501

        The user's tags.  # noqa: E501

        :return: The tags of this Users.  # noqa: E501
        :rtype: list[str]
        """
        return self._tags

    @tags.setter
    def tags(self, tags):
        """Sets the tags of this Users.

        The user's tags.  # noqa: E501

        :param tags: The tags of this Users.  # noqa: E501
        :type: list[str]
        """

        self._tags = tags

    @property
    def avatar(self):
        """Gets the avatar of this Users.  # noqa: E501

        The user's avatar.  # noqa: E501

        :return: The avatar of this Users.  # noqa: E501
        :rtype: OneOfUsersAvatar
        """
        return self._avatar

    @avatar.setter
    def avatar(self, avatar):
        """Sets the avatar of this Users.

        The user's avatar.  # noqa: E501

        :param avatar: The avatar of this Users.  # noqa: E501
        :type: OneOfUsersAvatar
        """

        self._avatar = avatar

    @property
    def language(self):
        """Gets the language of this Users.  # noqa: E501

        The user's language used in Directus.  # noqa: E501

        :return: The language of this Users.  # noqa: E501
        :rtype: str
        """
        return self._language

    @language.setter
    def language(self, language):
        """Sets the language of this Users.

        The user's language used in Directus.  # noqa: E501

        :param language: The language of this Users.  # noqa: E501
        :type: str
        """

        self._language = language

    @property
    def tfa_secret(self):
        """Gets the tfa_secret of this Users.  # noqa: E501

        The 2FA secret string that's used to generate one time passwords.  # noqa: E501

        :return: The tfa_secret of this Users.  # noqa: E501
        :rtype: str
        """
        return self._tfa_secret

    @tfa_secret.setter
    def tfa_secret(self, tfa_secret):
        """Sets the tfa_secret of this Users.

        The 2FA secret string that's used to generate one time passwords.  # noqa: E501

        :param tfa_secret: The tfa_secret of this Users.  # noqa: E501
        :type: str
        """

        self._tfa_secret = tfa_secret

    @property
    def status(self):
        """Gets the status of this Users.  # noqa: E501

        Status of the user.  # noqa: E501

        :return: The status of this Users.  # noqa: E501
        :rtype: str
        """
        return self._status

    @status.setter
    def status(self, status):
        """Sets the status of this Users.

        Status of the user.  # noqa: E501

        :param status: The status of this Users.  # noqa: E501
        :type: str
        """
        allowed_values = ["active", "invited", "draft", "suspended", "deleted"]  # noqa: E501
        if status not in allowed_values:
            raise ValueError(
                "Invalid value for `status` ({0}), must be one of {1}"  # noqa: E501
                .format(status, allowed_values)
            )

        self._status = status

    @property
    def role(self):
        """Gets the role of this Users.  # noqa: E501

        Unique identifier of the role of this user.  # noqa: E501

        :return: The role of this Users.  # noqa: E501
        :rtype: OneOfUsersRole
        """
        return self._role

    @role.setter
    def role(self, role):
        """Sets the role of this Users.

        Unique identifier of the role of this user.  # noqa: E501

        :param role: The role of this Users.  # noqa: E501
        :type: OneOfUsersRole
        """

        self._role = role

    @property
    def token(self):
        """Gets the token of this Users.  # noqa: E501

        Static token for the user.  # noqa: E501

        :return: The token of this Users.  # noqa: E501
        :rtype: str
        """
        return self._token

    @token.setter
    def token(self, token):
        """Sets the token of this Users.

        Static token for the user.  # noqa: E501

        :param token: The token of this Users.  # noqa: E501
        :type: str
        """

        self._token = token

    @property
    def last_access(self):
        """Gets the last_access of this Users.  # noqa: E501

        When this user used the API last.  # noqa: E501

        :return: The last_access of this Users.  # noqa: E501
        :rtype: datetime
        """
        return self._last_access

    @last_access.setter
    def last_access(self, last_access):
        """Sets the last_access of this Users.

        When this user used the API last.  # noqa: E501

        :param last_access: The last_access of this Users.  # noqa: E501
        :type: datetime
        """

        self._last_access = last_access

    @property
    def last_page(self):
        """Gets the last_page of this Users.  # noqa: E501

        Last page that the user was on.  # noqa: E501

        :return: The last_page of this Users.  # noqa: E501
        :rtype: str
        """
        return self._last_page

    @last_page.setter
    def last_page(self, last_page):
        """Sets the last_page of this Users.

        Last page that the user was on.  # noqa: E501

        :param last_page: The last_page of this Users.  # noqa: E501
        :type: str
        """

        self._last_page = last_page

    @property
    def provider(self):
        """Gets the provider of this Users.  # noqa: E501


        :return: The provider of this Users.  # noqa: E501
        :rtype: str
        """
        return self._provider

    @provider.setter
    def provider(self, provider):
        """Sets the provider of this Users.


        :param provider: The provider of this Users.  # noqa: E501
        :type: str
        """

        self._provider = provider

    @property
    def external_identifier(self):
        """Gets the external_identifier of this Users.  # noqa: E501


        :return: The external_identifier of this Users.  # noqa: E501
        :rtype: str
        """
        return self._external_identifier

    @external_identifier.setter
    def external_identifier(self, external_identifier):
        """Sets the external_identifier of this Users.


        :param external_identifier: The external_identifier of this Users.  # noqa: E501
        :type: str
        """

        self._external_identifier = external_identifier

    @property
    def auth_data(self):
        """Gets the auth_data of this Users.  # noqa: E501


        :return: The auth_data of this Users.  # noqa: E501
        :rtype: object
        """
        return self._auth_data

    @auth_data.setter
    def auth_data(self, auth_data):
        """Sets the auth_data of this Users.


        :param auth_data: The auth_data of this Users.  # noqa: E501
        :type: object
        """

        self._auth_data = auth_data

    @property
    def email_notifications(self):
        """Gets the email_notifications of this Users.  # noqa: E501


        :return: The email_notifications of this Users.  # noqa: E501
        :rtype: bool
        """
        return self._email_notifications

    @email_notifications.setter
    def email_notifications(self, email_notifications):
        """Sets the email_notifications of this Users.


        :param email_notifications: The email_notifications of this Users.  # noqa: E501
        :type: bool
        """

        self._email_notifications = email_notifications

    @property
    def appearance(self):
        """Gets the appearance of this Users.  # noqa: E501


        :return: The appearance of this Users.  # noqa: E501
        :rtype: str
        """
        return self._appearance

    @appearance.setter
    def appearance(self, appearance):
        """Sets the appearance of this Users.


        :param appearance: The appearance of this Users.  # noqa: E501
        :type: str
        """

        self._appearance = appearance

    @property
    def theme_dark(self):
        """Gets the theme_dark of this Users.  # noqa: E501


        :return: The theme_dark of this Users.  # noqa: E501
        :rtype: str
        """
        return self._theme_dark

    @theme_dark.setter
    def theme_dark(self, theme_dark):
        """Sets the theme_dark of this Users.


        :param theme_dark: The theme_dark of this Users.  # noqa: E501
        :type: str
        """

        self._theme_dark = theme_dark

    @property
    def theme_light(self):
        """Gets the theme_light of this Users.  # noqa: E501


        :return: The theme_light of this Users.  # noqa: E501
        :rtype: str
        """
        return self._theme_light

    @theme_light.setter
    def theme_light(self, theme_light):
        """Sets the theme_light of this Users.


        :param theme_light: The theme_light of this Users.  # noqa: E501
        :type: str
        """

        self._theme_light = theme_light

    @property
    def theme_light_overrides(self):
        """Gets the theme_light_overrides of this Users.  # noqa: E501


        :return: The theme_light_overrides of this Users.  # noqa: E501
        :rtype: object
        """
        return self._theme_light_overrides

    @theme_light_overrides.setter
    def theme_light_overrides(self, theme_light_overrides):
        """Sets the theme_light_overrides of this Users.


        :param theme_light_overrides: The theme_light_overrides of this Users.  # noqa: E501
        :type: object
        """

        self._theme_light_overrides = theme_light_overrides

    @property
    def theme_dark_overrides(self):
        """Gets the theme_dark_overrides of this Users.  # noqa: E501


        :return: The theme_dark_overrides of this Users.  # noqa: E501
        :rtype: object
        """
        return self._theme_dark_overrides

    @theme_dark_overrides.setter
    def theme_dark_overrides(self, theme_dark_overrides):
        """Sets the theme_dark_overrides of this Users.


        :param theme_dark_overrides: The theme_dark_overrides of this Users.  # noqa: E501
        :type: object
        """

        self._theme_dark_overrides = theme_dark_overrides

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
        if issubclass(Users, dict):
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
        if not isinstance(other, Users):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
