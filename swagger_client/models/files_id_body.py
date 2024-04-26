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

class FilesIdBody(object):
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
        'title': 'str',
        'filename_download': 'str',
        'description': 'str',
        'folder': 'OneOffilesIdBodyFolder',
        'tags': 'list[str]',
        'file': 'object'
    }

    attribute_map = {
        'title': 'title',
        'filename_download': 'filename_download',
        'description': 'description',
        'folder': 'folder',
        'tags': 'tags',
        'file': 'file'
    }

    def __init__(self, title=None, filename_download=None, description=None, folder=None, tags=None, file=None):  # noqa: E501
        """FilesIdBody - a model defined in Swagger"""  # noqa: E501
        self._title = None
        self._filename_download = None
        self._description = None
        self._folder = None
        self._tags = None
        self._file = None
        self.discriminator = None
        if title is not None:
            self.title = title
        if filename_download is not None:
            self.filename_download = filename_download
        if description is not None:
            self.description = description
        if folder is not None:
            self.folder = folder
        if tags is not None:
            self.tags = tags
        self.file = file

    @property
    def title(self):
        """Gets the title of this FilesIdBody.  # noqa: E501

        Title for the file. Is extracted from the filename on upload, but can be edited by the user.  # noqa: E501

        :return: The title of this FilesIdBody.  # noqa: E501
        :rtype: str
        """
        return self._title

    @title.setter
    def title(self, title):
        """Sets the title of this FilesIdBody.

        Title for the file. Is extracted from the filename on upload, but can be edited by the user.  # noqa: E501

        :param title: The title of this FilesIdBody.  # noqa: E501
        :type: str
        """

        self._title = title

    @property
    def filename_download(self):
        """Gets the filename_download of this FilesIdBody.  # noqa: E501

        Preferred filename when file is downloaded.  # noqa: E501

        :return: The filename_download of this FilesIdBody.  # noqa: E501
        :rtype: str
        """
        return self._filename_download

    @filename_download.setter
    def filename_download(self, filename_download):
        """Sets the filename_download of this FilesIdBody.

        Preferred filename when file is downloaded.  # noqa: E501

        :param filename_download: The filename_download of this FilesIdBody.  # noqa: E501
        :type: str
        """

        self._filename_download = filename_download

    @property
    def description(self):
        """Gets the description of this FilesIdBody.  # noqa: E501

        Description for the file.  # noqa: E501

        :return: The description of this FilesIdBody.  # noqa: E501
        :rtype: str
        """
        return self._description

    @description.setter
    def description(self, description):
        """Sets the description of this FilesIdBody.

        Description for the file.  # noqa: E501

        :param description: The description of this FilesIdBody.  # noqa: E501
        :type: str
        """

        self._description = description

    @property
    def folder(self):
        """Gets the folder of this FilesIdBody.  # noqa: E501

        Virtual folder where this file resides in.  # noqa: E501

        :return: The folder of this FilesIdBody.  # noqa: E501
        :rtype: OneOffilesIdBodyFolder
        """
        return self._folder

    @folder.setter
    def folder(self, folder):
        """Sets the folder of this FilesIdBody.

        Virtual folder where this file resides in.  # noqa: E501

        :param folder: The folder of this FilesIdBody.  # noqa: E501
        :type: OneOffilesIdBodyFolder
        """

        self._folder = folder

    @property
    def tags(self):
        """Gets the tags of this FilesIdBody.  # noqa: E501

        Tags for the file. Is automatically populated based on Exif data for images.  # noqa: E501

        :return: The tags of this FilesIdBody.  # noqa: E501
        :rtype: list[str]
        """
        return self._tags

    @tags.setter
    def tags(self, tags):
        """Sets the tags of this FilesIdBody.

        Tags for the file. Is automatically populated based on Exif data for images.  # noqa: E501

        :param tags: The tags of this FilesIdBody.  # noqa: E501
        :type: list[str]
        """

        self._tags = tags

    @property
    def file(self):
        """Gets the file of this FilesIdBody.  # noqa: E501

        File contents.  # noqa: E501

        :return: The file of this FilesIdBody.  # noqa: E501
        :rtype: object
        """
        return self._file

    @file.setter
    def file(self, file):
        """Sets the file of this FilesIdBody.

        File contents.  # noqa: E501

        :param file: The file of this FilesIdBody.  # noqa: E501
        :type: object
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
        if issubclass(FilesIdBody, dict):
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
        if not isinstance(other, FilesIdBody):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
