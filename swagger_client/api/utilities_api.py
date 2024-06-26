# coding: utf-8

"""
    Dynamic API Specification

    This is a dynamically generated API specification for all endpoints existing on the current project.  # noqa: E501

    OpenAPI spec version: 10.10.5
    
    Generated by: https://github.com/swagger-api/swagger-codegen.git
"""

from __future__ import absolute_import

import re  # noqa: F401

# python 2 and python 3 compatibility library
import six

from swagger_client.api_client import ApiClient


class UtilitiesApi(object):
    """NOTE: This class is auto generated by the swagger code generator program.

    Do not edit the class manually.
    Ref: https://github.com/swagger-api/swagger-codegen
    """

    def __init__(self, api_client=None):
        if api_client is None:
            api_client = ApiClient()
        self.api_client = api_client

    def call_import(self, collection, **kwargs):  # noqa: E501
        """Import Items  # noqa: E501

        Import multiple records from a JSON or CSV file into a collection.  # noqa: E501
        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please pass async_req=True
        >>> thread = api.call_import(collection, async_req=True)
        >>> result = thread.get()

        :param async_req bool
        :param str collection: Collection identifier (required)
        :param str file:
        :return: None
                 If the method is called asynchronously,
                 returns the request thread.
        """
        kwargs['_return_http_data_only'] = True
        if kwargs.get('async_req'):
            return self.call_import_with_http_info(collection, **kwargs)  # noqa: E501
        else:
            (data) = self.call_import_with_http_info(collection, **kwargs)  # noqa: E501
            return data

    def call_import_with_http_info(self, collection, **kwargs):  # noqa: E501
        """Import Items  # noqa: E501

        Import multiple records from a JSON or CSV file into a collection.  # noqa: E501
        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please pass async_req=True
        >>> thread = api.call_import_with_http_info(collection, async_req=True)
        >>> result = thread.get()

        :param async_req bool
        :param str collection: Collection identifier (required)
        :param str file:
        :return: None
                 If the method is called asynchronously,
                 returns the request thread.
        """

        all_params = ['collection', 'file']  # noqa: E501
        all_params.append('async_req')
        all_params.append('_return_http_data_only')
        all_params.append('_preload_content')
        all_params.append('_request_timeout')

        params = locals()
        for key, val in six.iteritems(params['kwargs']):
            if key not in all_params:
                raise TypeError(
                    "Got an unexpected keyword argument '%s'"
                    " to method call_import" % key
                )
            params[key] = val
        del params['kwargs']
        # verify the required parameter 'collection' is set
        if ('collection' not in params or
                params['collection'] is None):
            raise ValueError("Missing the required parameter `collection` when calling `call_import`")  # noqa: E501

        collection_formats = {}

        path_params = {}
        if 'collection' in params:
            path_params['collection'] = params['collection']  # noqa: E501

        query_params = []

        header_params = {}

        form_params = []
        local_var_files = {}
        if 'file' in params:
            local_var_files['file'] = params['file']  # noqa: E501

        body_params = None
        # HTTP header `Content-Type`
        header_params['Content-Type'] = self.api_client.select_header_content_type(  # noqa: E501
            ['multipart/form-data'])  # noqa: E501

        # Authentication setting
        auth_settings = []  # noqa: E501

        return self.api_client.call_api(
            '/utils/import/{collection}', 'POST',
            path_params,
            query_params,
            header_params,
            body=body_params,
            post_params=form_params,
            files=local_var_files,
            response_type=None,  # noqa: E501
            auth_settings=auth_settings,
            async_req=params.get('async_req'),
            _return_http_data_only=params.get('_return_http_data_only'),
            _preload_content=params.get('_preload_content', True),
            _request_timeout=params.get('_request_timeout'),
            collection_formats=collection_formats)

    def clear_cache(self, **kwargs):  # noqa: E501
        """Clear Cache  # noqa: E501

        Resets both the data and schema cache of Directus.  # noqa: E501
        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please pass async_req=True
        >>> thread = api.clear_cache(async_req=True)
        >>> result = thread.get()

        :param async_req bool
        :return: None
                 If the method is called asynchronously,
                 returns the request thread.
        """
        kwargs['_return_http_data_only'] = True
        if kwargs.get('async_req'):
            return self.clear_cache_with_http_info(**kwargs)  # noqa: E501
        else:
            (data) = self.clear_cache_with_http_info(**kwargs)  # noqa: E501
            return data

    def clear_cache_with_http_info(self, **kwargs):  # noqa: E501
        """Clear Cache  # noqa: E501

        Resets both the data and schema cache of Directus.  # noqa: E501
        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please pass async_req=True
        >>> thread = api.clear_cache_with_http_info(async_req=True)
        >>> result = thread.get()

        :param async_req bool
        :return: None
                 If the method is called asynchronously,
                 returns the request thread.
        """

        all_params = []  # noqa: E501
        all_params.append('async_req')
        all_params.append('_return_http_data_only')
        all_params.append('_preload_content')
        all_params.append('_request_timeout')

        params = locals()
        for key, val in six.iteritems(params['kwargs']):
            if key not in all_params:
                raise TypeError(
                    "Got an unexpected keyword argument '%s'"
                    " to method clear_cache" % key
                )
            params[key] = val
        del params['kwargs']

        collection_formats = {}

        path_params = {}

        query_params = []

        header_params = {}

        form_params = []
        local_var_files = {}

        body_params = None
        # Authentication setting
        auth_settings = []  # noqa: E501

        return self.api_client.call_api(
            '/utils/cache/clear', 'POST',
            path_params,
            query_params,
            header_params,
            body=body_params,
            post_params=form_params,
            files=local_var_files,
            response_type=None,  # noqa: E501
            auth_settings=auth_settings,
            async_req=params.get('async_req'),
            _return_http_data_only=params.get('_return_http_data_only'),
            _preload_content=params.get('_preload_content', True),
            _request_timeout=params.get('_request_timeout'),
            collection_formats=collection_formats)

    def export(self, collection, **kwargs):  # noqa: E501
        """Export Items  # noqa: E501

        Export a larger data set to a file in the File Library  # noqa: E501
        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please pass async_req=True
        >>> thread = api.export(collection, async_req=True)
        >>> result = thread.get()

        :param async_req bool
        :param str collection: Collection identifier (required)
        :param ExportCollectionBody body:
        :return: None
                 If the method is called asynchronously,
                 returns the request thread.
        """
        kwargs['_return_http_data_only'] = True
        if kwargs.get('async_req'):
            return self.export_with_http_info(collection, **kwargs)  # noqa: E501
        else:
            (data) = self.export_with_http_info(collection, **kwargs)  # noqa: E501
            return data

    def export_with_http_info(self, collection, **kwargs):  # noqa: E501
        """Export Items  # noqa: E501

        Export a larger data set to a file in the File Library  # noqa: E501
        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please pass async_req=True
        >>> thread = api.export_with_http_info(collection, async_req=True)
        >>> result = thread.get()

        :param async_req bool
        :param str collection: Collection identifier (required)
        :param ExportCollectionBody body:
        :return: None
                 If the method is called asynchronously,
                 returns the request thread.
        """

        all_params = ['collection', 'body']  # noqa: E501
        all_params.append('async_req')
        all_params.append('_return_http_data_only')
        all_params.append('_preload_content')
        all_params.append('_request_timeout')

        params = locals()
        for key, val in six.iteritems(params['kwargs']):
            if key not in all_params:
                raise TypeError(
                    "Got an unexpected keyword argument '%s'"
                    " to method export" % key
                )
            params[key] = val
        del params['kwargs']
        # verify the required parameter 'collection' is set
        if ('collection' not in params or
                params['collection'] is None):
            raise ValueError("Missing the required parameter `collection` when calling `export`")  # noqa: E501

        collection_formats = {}

        path_params = {}
        if 'collection' in params:
            path_params['collection'] = params['collection']  # noqa: E501

        query_params = []

        header_params = {}

        form_params = []
        local_var_files = {}

        body_params = None
        if 'body' in params:
            body_params = params['body']
        # HTTP header `Content-Type`
        header_params['Content-Type'] = self.api_client.select_header_content_type(  # noqa: E501
            ['application/json'])  # noqa: E501

        # Authentication setting
        auth_settings = []  # noqa: E501

        return self.api_client.call_api(
            '/utils/export/{collection}', 'POST',
            path_params,
            query_params,
            header_params,
            body=body_params,
            post_params=form_params,
            files=local_var_files,
            response_type=None,  # noqa: E501
            auth_settings=auth_settings,
            async_req=params.get('async_req'),
            _return_http_data_only=params.get('_return_http_data_only'),
            _preload_content=params.get('_preload_content', True),
            _request_timeout=params.get('_request_timeout'),
            collection_formats=collection_formats)

    def hash_generate(self, **kwargs):  # noqa: E501
        """Hash a string  # noqa: E501

        Generate a hash for a given string.  # noqa: E501
        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please pass async_req=True
        >>> thread = api.hash_generate(async_req=True)
        >>> result = thread.get()

        :param async_req bool
        :param HashGenerateBody body:
        :return: InlineResponse2006
                 If the method is called asynchronously,
                 returns the request thread.
        """
        kwargs['_return_http_data_only'] = True
        if kwargs.get('async_req'):
            return self.hash_generate_with_http_info(**kwargs)  # noqa: E501
        else:
            (data) = self.hash_generate_with_http_info(**kwargs)  # noqa: E501
            return data

    def hash_generate_with_http_info(self, **kwargs):  # noqa: E501
        """Hash a string  # noqa: E501

        Generate a hash for a given string.  # noqa: E501
        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please pass async_req=True
        >>> thread = api.hash_generate_with_http_info(async_req=True)
        >>> result = thread.get()

        :param async_req bool
        :param HashGenerateBody body:
        :return: InlineResponse2006
                 If the method is called asynchronously,
                 returns the request thread.
        """

        all_params = ['body']  # noqa: E501
        all_params.append('async_req')
        all_params.append('_return_http_data_only')
        all_params.append('_preload_content')
        all_params.append('_request_timeout')

        params = locals()
        for key, val in six.iteritems(params['kwargs']):
            if key not in all_params:
                raise TypeError(
                    "Got an unexpected keyword argument '%s'"
                    " to method hash_generate" % key
                )
            params[key] = val
        del params['kwargs']

        collection_formats = {}

        path_params = {}

        query_params = []

        header_params = {}

        form_params = []
        local_var_files = {}

        body_params = None
        if 'body' in params:
            body_params = params['body']
        # HTTP header `Accept`
        header_params['Accept'] = self.api_client.select_header_accept(
            ['application/json'])  # noqa: E501

        # HTTP header `Content-Type`
        header_params['Content-Type'] = self.api_client.select_header_content_type(  # noqa: E501
            ['application/json'])  # noqa: E501

        # Authentication setting
        auth_settings = []  # noqa: E501

        return self.api_client.call_api(
            '/utils/hash/generate', 'POST',
            path_params,
            query_params,
            header_params,
            body=body_params,
            post_params=form_params,
            files=local_var_files,
            response_type='InlineResponse2006',  # noqa: E501
            auth_settings=auth_settings,
            async_req=params.get('async_req'),
            _return_http_data_only=params.get('_return_http_data_only'),
            _preload_content=params.get('_preload_content', True),
            _request_timeout=params.get('_request_timeout'),
            collection_formats=collection_formats)

    def hash_verify(self, **kwargs):  # noqa: E501
        """Hash a string  # noqa: E501

        Generate a hash for a given string.  # noqa: E501
        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please pass async_req=True
        >>> thread = api.hash_verify(async_req=True)
        >>> result = thread.get()

        :param async_req bool
        :param HashVerifyBody body:
        :return: InlineResponse2007
                 If the method is called asynchronously,
                 returns the request thread.
        """
        kwargs['_return_http_data_only'] = True
        if kwargs.get('async_req'):
            return self.hash_verify_with_http_info(**kwargs)  # noqa: E501
        else:
            (data) = self.hash_verify_with_http_info(**kwargs)  # noqa: E501
            return data

    def hash_verify_with_http_info(self, **kwargs):  # noqa: E501
        """Hash a string  # noqa: E501

        Generate a hash for a given string.  # noqa: E501
        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please pass async_req=True
        >>> thread = api.hash_verify_with_http_info(async_req=True)
        >>> result = thread.get()

        :param async_req bool
        :param HashVerifyBody body:
        :return: InlineResponse2007
                 If the method is called asynchronously,
                 returns the request thread.
        """

        all_params = ['body']  # noqa: E501
        all_params.append('async_req')
        all_params.append('_return_http_data_only')
        all_params.append('_preload_content')
        all_params.append('_request_timeout')

        params = locals()
        for key, val in six.iteritems(params['kwargs']):
            if key not in all_params:
                raise TypeError(
                    "Got an unexpected keyword argument '%s'"
                    " to method hash_verify" % key
                )
            params[key] = val
        del params['kwargs']

        collection_formats = {}

        path_params = {}

        query_params = []

        header_params = {}

        form_params = []
        local_var_files = {}

        body_params = None
        if 'body' in params:
            body_params = params['body']
        # HTTP header `Accept`
        header_params['Accept'] = self.api_client.select_header_accept(
            ['application/json'])  # noqa: E501

        # HTTP header `Content-Type`
        header_params['Content-Type'] = self.api_client.select_header_content_type(  # noqa: E501
            ['application/json'])  # noqa: E501

        # Authentication setting
        auth_settings = []  # noqa: E501

        return self.api_client.call_api(
            '/utils/hash/verify', 'POST',
            path_params,
            query_params,
            header_params,
            body=body_params,
            post_params=form_params,
            files=local_var_files,
            response_type='InlineResponse2007',  # noqa: E501
            auth_settings=auth_settings,
            async_req=params.get('async_req'),
            _return_http_data_only=params.get('_return_http_data_only'),
            _preload_content=params.get('_preload_content', True),
            _request_timeout=params.get('_request_timeout'),
            collection_formats=collection_formats)

    def random(self, **kwargs):  # noqa: E501
        """Get a Random String  # noqa: E501

        Returns a random string of given length.  # noqa: E501
        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please pass async_req=True
        >>> thread = api.random(async_req=True)
        >>> result = thread.get()

        :param async_req bool
        :param int length: Length of the random string.
        :return: InlineResponse2008
                 If the method is called asynchronously,
                 returns the request thread.
        """
        kwargs['_return_http_data_only'] = True
        if kwargs.get('async_req'):
            return self.random_with_http_info(**kwargs)  # noqa: E501
        else:
            (data) = self.random_with_http_info(**kwargs)  # noqa: E501
            return data

    def random_with_http_info(self, **kwargs):  # noqa: E501
        """Get a Random String  # noqa: E501

        Returns a random string of given length.  # noqa: E501
        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please pass async_req=True
        >>> thread = api.random_with_http_info(async_req=True)
        >>> result = thread.get()

        :param async_req bool
        :param int length: Length of the random string.
        :return: InlineResponse2008
                 If the method is called asynchronously,
                 returns the request thread.
        """

        all_params = ['length']  # noqa: E501
        all_params.append('async_req')
        all_params.append('_return_http_data_only')
        all_params.append('_preload_content')
        all_params.append('_request_timeout')

        params = locals()
        for key, val in six.iteritems(params['kwargs']):
            if key not in all_params:
                raise TypeError(
                    "Got an unexpected keyword argument '%s'"
                    " to method random" % key
                )
            params[key] = val
        del params['kwargs']

        collection_formats = {}

        path_params = {}

        query_params = []
        if 'length' in params:
            query_params.append(('length', params['length']))  # noqa: E501

        header_params = {}

        form_params = []
        local_var_files = {}

        body_params = None
        # HTTP header `Accept`
        header_params['Accept'] = self.api_client.select_header_accept(
            ['application/json'])  # noqa: E501

        # Authentication setting
        auth_settings = []  # noqa: E501

        return self.api_client.call_api(
            '/utils/random/string', 'GET',
            path_params,
            query_params,
            header_params,
            body=body_params,
            post_params=form_params,
            files=local_var_files,
            response_type='InlineResponse2008',  # noqa: E501
            auth_settings=auth_settings,
            async_req=params.get('async_req'),
            _return_http_data_only=params.get('_return_http_data_only'),
            _preload_content=params.get('_preload_content', True),
            _request_timeout=params.get('_request_timeout'),
            collection_formats=collection_formats)

    def sort(self, collection, **kwargs):  # noqa: E501
        """Sort Items  # noqa: E501

        Re-sort items in collection based on start and to value of item  # noqa: E501
        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please pass async_req=True
        >>> thread = api.sort(collection, async_req=True)
        >>> result = thread.get()

        :param async_req bool
        :param str collection: Collection identifier (required)
        :param SortCollectionBody body:
        :return: None
                 If the method is called asynchronously,
                 returns the request thread.
        """
        kwargs['_return_http_data_only'] = True
        if kwargs.get('async_req'):
            return self.sort_with_http_info(collection, **kwargs)  # noqa: E501
        else:
            (data) = self.sort_with_http_info(collection, **kwargs)  # noqa: E501
            return data

    def sort_with_http_info(self, collection, **kwargs):  # noqa: E501
        """Sort Items  # noqa: E501

        Re-sort items in collection based on start and to value of item  # noqa: E501
        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please pass async_req=True
        >>> thread = api.sort_with_http_info(collection, async_req=True)
        >>> result = thread.get()

        :param async_req bool
        :param str collection: Collection identifier (required)
        :param SortCollectionBody body:
        :return: None
                 If the method is called asynchronously,
                 returns the request thread.
        """

        all_params = ['collection', 'body']  # noqa: E501
        all_params.append('async_req')
        all_params.append('_return_http_data_only')
        all_params.append('_preload_content')
        all_params.append('_request_timeout')

        params = locals()
        for key, val in six.iteritems(params['kwargs']):
            if key not in all_params:
                raise TypeError(
                    "Got an unexpected keyword argument '%s'"
                    " to method sort" % key
                )
            params[key] = val
        del params['kwargs']
        # verify the required parameter 'collection' is set
        if ('collection' not in params or
                params['collection'] is None):
            raise ValueError("Missing the required parameter `collection` when calling `sort`")  # noqa: E501

        collection_formats = {}

        path_params = {}
        if 'collection' in params:
            path_params['collection'] = params['collection']  # noqa: E501

        query_params = []

        header_params = {}

        form_params = []
        local_var_files = {}

        body_params = None
        if 'body' in params:
            body_params = params['body']
        # HTTP header `Content-Type`
        header_params['Content-Type'] = self.api_client.select_header_content_type(  # noqa: E501
            ['application/json'])  # noqa: E501

        # Authentication setting
        auth_settings = []  # noqa: E501

        return self.api_client.call_api(
            '/utils/sort/{collection}', 'POST',
            path_params,
            query_params,
            header_params,
            body=body_params,
            post_params=form_params,
            files=local_var_files,
            response_type=None,  # noqa: E501
            auth_settings=auth_settings,
            async_req=params.get('async_req'),
            _return_http_data_only=params.get('_return_http_data_only'),
            _preload_content=params.get('_preload_content', True),
            _request_timeout=params.get('_request_timeout'),
            collection_formats=collection_formats)
