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
from swagger_client.api.items_sources_api import ItemsSourcesApi  # noqa: E501
from swagger_client.rest import ApiException


class TestItemsSourcesApi(unittest.TestCase):
    """ItemsSourcesApi unit test stubs"""

    def setUp(self):
        self.api = ItemsSourcesApi()  # noqa: E501

    def tearDown(self):
        pass

    def test_create_items_sources(self):
        """Test case for create_items_sources

        Create an Item  # noqa: E501
        """
        pass

    def test_delete_items_sources(self):
        """Test case for delete_items_sources

        Delete Multiple Items  # noqa: E501
        """
        pass

    def test_delete_single_items_sources(self):
        """Test case for delete_single_items_sources

        Delete an Item  # noqa: E501
        """
        pass

    def test_read_items_sources(self):
        """Test case for read_items_sources

        List Items  # noqa: E501
        """
        pass

    def test_read_single_items_sources(self):
        """Test case for read_single_items_sources

        Retrieve an Item  # noqa: E501
        """
        pass

    def test_update_items_sources(self):
        """Test case for update_items_sources

        Update Multiple Items  # noqa: E501
        """
        pass

    def test_update_single_items_sources(self):
        """Test case for update_single_items_sources

        Update an Item  # noqa: E501
        """
        pass


if __name__ == '__main__':
    unittest.main()