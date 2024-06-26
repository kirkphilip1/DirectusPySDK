# coding: utf-8

"""
    Dynamic API Specification

    This is a dynamically generated API specification for all endpoints existing on the current project.  # noqa: E501

    OpenAPI spec version: 10.10.5
    
    Generated by: https://github.com/swagger-api/swagger-codegen.git
"""

from __future__ import absolute_import

import unittest

import swagger_client
from swagger_client.api.roles_api import RolesApi  # noqa: E501
from swagger_client.rest import ApiException


class TestRolesApi(unittest.TestCase):
    """RolesApi unit test stubs"""

    def setUp(self):
        self.api = RolesApi()  # noqa: E501

    def tearDown(self):
        pass

    def test_create_role(self):
        """Test case for create_role

        Create a Role  # noqa: E501
        """
        pass

    def test_delete_role(self):
        """Test case for delete_role

        Delete a Role  # noqa: E501
        """
        pass

    def test_delete_roles(self):
        """Test case for delete_roles

        Delete Multiple Roles  # noqa: E501
        """
        pass

    def test_get_role(self):
        """Test case for get_role

        Retrieve a Role  # noqa: E501
        """
        pass

    def test_get_roles(self):
        """Test case for get_roles

        List Roles  # noqa: E501
        """
        pass

    def test_update_role(self):
        """Test case for update_role

        Update a Role  # noqa: E501
        """
        pass

    def test_update_roles(self):
        """Test case for update_roles

        Update Multiple Roles  # noqa: E501
        """
        pass


if __name__ == '__main__':
    unittest.main()
