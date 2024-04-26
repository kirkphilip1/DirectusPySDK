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


class FieldsApi(object):
    """NOTE: This class is auto generated by the swagger code generator program.

    Do not edit the class manually.
    Ref: https://github.com/swagger-api/swagger-codegen
    """

    def __init__(self, api_client=None):
        if api_client is None:
            api_client = ApiClient()
        self.api_client = api_client

    def create_field(self, collection, **kwargs):  # noqa: E501
        """Create Field in Collection  # noqa: E501

        Create a new field in a given collection.  # noqa: E501
        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please pass async_req=True
        >>> thread = api.create_field(collection, async_req=True)
        >>> result = thread.get()

        :param async_req bool
        :param str collection: Unique identifier of the collection the item resides in. (required)
        :param FieldsCollectionBody body:
        :return: InlineResponse20020
                 If the method is called asynchronously,
                 returns the request thread.
        """
        kwargs['_return_http_data_only'] = True
        if kwargs.get('async_req'):
            return self.create_field_with_http_info(collection, **kwargs)  # noqa: E501
        else:
            (data) = self.create_field_with_http_info(collection, **kwargs)  # noqa: E501
            return data

    def create_field_with_http_info(self, collection, **kwargs):  # noqa: E501
        """Create Field in Collection  # noqa: E501

        Create a new field in a given collection.  # noqa: E501
        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please pass async_req=True
        >>> thread = api.create_field_with_http_info(collection, async_req=True)
        >>> result = thread.get()

        :param async_req bool
        :param str collection: Unique identifier of the collection the item resides in. (required)
        :param FieldsCollectionBody body:
        :return: InlineResponse20020
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
                    " to method create_field" % key
                )
            params[key] = val
        del params['kwargs']
        # verify the required parameter 'collection' is set
        if ('collection' not in params or
                params['collection'] is None):
            raise ValueError("Missing the required parameter `collection` when calling `create_field`")  # noqa: E501

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
        # HTTP header `Accept`
        header_params['Accept'] = self.api_client.select_header_accept(
            ['application/json'])  # noqa: E501

        # HTTP header `Content-Type`
        header_params['Content-Type'] = self.api_client.select_header_content_type(  # noqa: E501
            ['application/json'])  # noqa: E501

        # Authentication setting
        auth_settings = []  # noqa: E501

        return self.api_client.call_api(
            '/fields/{collection}', 'POST',
            path_params,
            query_params,
            header_params,
            body=body_params,
            post_params=form_params,
            files=local_var_files,
            response_type='InlineResponse20020',  # noqa: E501
            auth_settings=auth_settings,
            async_req=params.get('async_req'),
            _return_http_data_only=params.get('_return_http_data_only'),
            _preload_content=params.get('_preload_content', True),
            _request_timeout=params.get('_request_timeout'),
            collection_formats=collection_formats)

    def delete_field(self, collection, id, **kwargs):  # noqa: E501
        """Delete a Field  # noqa: E501

        Delete an existing field.  # noqa: E501
        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please pass async_req=True
        >>> thread = api.delete_field(collection, id, async_req=True)
        >>> result = thread.get()

        :param async_req bool
        :param str collection: Unique identifier of the collection the item resides in. (required)
        :param str id: Unique identifier of the field. (required)
        :return: None
                 If the method is called asynchronously,
                 returns the request thread.
        """
        kwargs['_return_http_data_only'] = True
        if kwargs.get('async_req'):
            return self.delete_field_with_http_info(collection, id, **kwargs)  # noqa: E501
        else:
            (data) = self.delete_field_with_http_info(collection, id, **kwargs)  # noqa: E501
            return data

    def delete_field_with_http_info(self, collection, id, **kwargs):  # noqa: E501
        """Delete a Field  # noqa: E501

        Delete an existing field.  # noqa: E501
        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please pass async_req=True
        >>> thread = api.delete_field_with_http_info(collection, id, async_req=True)
        >>> result = thread.get()

        :param async_req bool
        :param str collection: Unique identifier of the collection the item resides in. (required)
        :param str id: Unique identifier of the field. (required)
        :return: None
                 If the method is called asynchronously,
                 returns the request thread.
        """

        all_params = ['collection', 'id']  # noqa: E501
        all_params.append('async_req')
        all_params.append('_return_http_data_only')
        all_params.append('_preload_content')
        all_params.append('_request_timeout')

        params = locals()
        for key, val in six.iteritems(params['kwargs']):
            if key not in all_params:
                raise TypeError(
                    "Got an unexpected keyword argument '%s'"
                    " to method delete_field" % key
                )
            params[key] = val
        del params['kwargs']
        # verify the required parameter 'collection' is set
        if ('collection' not in params or
                params['collection'] is None):
            raise ValueError("Missing the required parameter `collection` when calling `delete_field`")  # noqa: E501
        # verify the required parameter 'id' is set
        if ('id' not in params or
                params['id'] is None):
            raise ValueError("Missing the required parameter `id` when calling `delete_field`")  # noqa: E501

        collection_formats = {}

        path_params = {}
        if 'collection' in params:
            path_params['collection'] = params['collection']  # noqa: E501
        if 'id' in params:
            path_params['id'] = params['id']  # noqa: E501

        query_params = []

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
            '/fields/{collection}/{id}', 'DELETE',
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

    def get_collection_field(self, collection, id, **kwargs):  # noqa: E501
        """Retrieve a Field  # noqa: E501

        Retrieves the details of a single field in a given collection.  # noqa: E501
        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please pass async_req=True
        >>> thread = api.get_collection_field(collection, id, async_req=True)
        >>> result = thread.get()

        :param async_req bool
        :param str collection: Unique identifier of the collection the item resides in. (required)
        :param str id: Unique identifier of the field. (required)
        :return: InlineResponse20020
                 If the method is called asynchronously,
                 returns the request thread.
        """
        kwargs['_return_http_data_only'] = True
        if kwargs.get('async_req'):
            return self.get_collection_field_with_http_info(collection, id, **kwargs)  # noqa: E501
        else:
            (data) = self.get_collection_field_with_http_info(collection, id, **kwargs)  # noqa: E501
            return data

    def get_collection_field_with_http_info(self, collection, id, **kwargs):  # noqa: E501
        """Retrieve a Field  # noqa: E501

        Retrieves the details of a single field in a given collection.  # noqa: E501
        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please pass async_req=True
        >>> thread = api.get_collection_field_with_http_info(collection, id, async_req=True)
        >>> result = thread.get()

        :param async_req bool
        :param str collection: Unique identifier of the collection the item resides in. (required)
        :param str id: Unique identifier of the field. (required)
        :return: InlineResponse20020
                 If the method is called asynchronously,
                 returns the request thread.
        """

        all_params = ['collection', 'id']  # noqa: E501
        all_params.append('async_req')
        all_params.append('_return_http_data_only')
        all_params.append('_preload_content')
        all_params.append('_request_timeout')

        params = locals()
        for key, val in six.iteritems(params['kwargs']):
            if key not in all_params:
                raise TypeError(
                    "Got an unexpected keyword argument '%s'"
                    " to method get_collection_field" % key
                )
            params[key] = val
        del params['kwargs']
        # verify the required parameter 'collection' is set
        if ('collection' not in params or
                params['collection'] is None):
            raise ValueError("Missing the required parameter `collection` when calling `get_collection_field`")  # noqa: E501
        # verify the required parameter 'id' is set
        if ('id' not in params or
                params['id'] is None):
            raise ValueError("Missing the required parameter `id` when calling `get_collection_field`")  # noqa: E501

        collection_formats = {}

        path_params = {}
        if 'collection' in params:
            path_params['collection'] = params['collection']  # noqa: E501
        if 'id' in params:
            path_params['id'] = params['id']  # noqa: E501

        query_params = []

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
            '/fields/{collection}/{id}', 'GET',
            path_params,
            query_params,
            header_params,
            body=body_params,
            post_params=form_params,
            files=local_var_files,
            response_type='InlineResponse20020',  # noqa: E501
            auth_settings=auth_settings,
            async_req=params.get('async_req'),
            _return_http_data_only=params.get('_return_http_data_only'),
            _preload_content=params.get('_preload_content', True),
            _request_timeout=params.get('_request_timeout'),
            collection_formats=collection_formats)

    def get_collection_fields(self, collection, **kwargs):  # noqa: E501
        """List Fields in Collection  # noqa: E501

        Returns a list of the fields available in the given collection.  # noqa: E501
        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please pass async_req=True
        >>> thread = api.get_collection_fields(collection, async_req=True)
        >>> result = thread.get()

        :param async_req bool
        :param str collection: Unique identifier of the collection the item resides in. (required)
        :param list[str] sort: How to sort the returned items. `sort` is a CSV of fields used to sort the fetched items. Sorting defaults to ascending (ASC) order but a minus sign (` - `) can be used to reverse this to descending (DESC) order. Fields are prioritized by their order in the CSV. You can also use a ` ? ` to sort randomly. 
        :return: InlineResponse20019
                 If the method is called asynchronously,
                 returns the request thread.
        """
        kwargs['_return_http_data_only'] = True
        if kwargs.get('async_req'):
            return self.get_collection_fields_with_http_info(collection, **kwargs)  # noqa: E501
        else:
            (data) = self.get_collection_fields_with_http_info(collection, **kwargs)  # noqa: E501
            return data

    def get_collection_fields_with_http_info(self, collection, **kwargs):  # noqa: E501
        """List Fields in Collection  # noqa: E501

        Returns a list of the fields available in the given collection.  # noqa: E501
        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please pass async_req=True
        >>> thread = api.get_collection_fields_with_http_info(collection, async_req=True)
        >>> result = thread.get()

        :param async_req bool
        :param str collection: Unique identifier of the collection the item resides in. (required)
        :param list[str] sort: How to sort the returned items. `sort` is a CSV of fields used to sort the fetched items. Sorting defaults to ascending (ASC) order but a minus sign (` - `) can be used to reverse this to descending (DESC) order. Fields are prioritized by their order in the CSV. You can also use a ` ? ` to sort randomly. 
        :return: InlineResponse20019
                 If the method is called asynchronously,
                 returns the request thread.
        """

        all_params = ['collection', 'sort']  # noqa: E501
        all_params.append('async_req')
        all_params.append('_return_http_data_only')
        all_params.append('_preload_content')
        all_params.append('_request_timeout')

        params = locals()
        for key, val in six.iteritems(params['kwargs']):
            if key not in all_params:
                raise TypeError(
                    "Got an unexpected keyword argument '%s'"
                    " to method get_collection_fields" % key
                )
            params[key] = val
        del params['kwargs']
        # verify the required parameter 'collection' is set
        if ('collection' not in params or
                params['collection'] is None):
            raise ValueError("Missing the required parameter `collection` when calling `get_collection_fields`")  # noqa: E501

        collection_formats = {}

        path_params = {}
        if 'collection' in params:
            path_params['collection'] = params['collection']  # noqa: E501

        query_params = []
        if 'sort' in params:
            query_params.append(('sort', params['sort']))  # noqa: E501
            collection_formats['sort'] = 'csv'  # noqa: E501

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
            '/fields/{collection}', 'GET',
            path_params,
            query_params,
            header_params,
            body=body_params,
            post_params=form_params,
            files=local_var_files,
            response_type='InlineResponse20019',  # noqa: E501
            auth_settings=auth_settings,
            async_req=params.get('async_req'),
            _return_http_data_only=params.get('_return_http_data_only'),
            _preload_content=params.get('_preload_content', True),
            _request_timeout=params.get('_request_timeout'),
            collection_formats=collection_formats)

    def get_fields(self, **kwargs):  # noqa: E501
        """List All Fields  # noqa: E501

        Returns a list of the fields available in the project.  # noqa: E501
        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please pass async_req=True
        >>> thread = api.get_fields(async_req=True)
        >>> result = thread.get()

        :param async_req bool
        :param int limit: A limit on the number of objects that are returned.
        :param list[str] sort: How to sort the returned items. `sort` is a CSV of fields used to sort the fetched items. Sorting defaults to ascending (ASC) order but a minus sign (` - `) can be used to reverse this to descending (DESC) order. Fields are prioritized by their order in the CSV. You can also use a ` ? ` to sort randomly. 
        :return: InlineResponse20019
                 If the method is called asynchronously,
                 returns the request thread.
        """
        kwargs['_return_http_data_only'] = True
        if kwargs.get('async_req'):
            return self.get_fields_with_http_info(**kwargs)  # noqa: E501
        else:
            (data) = self.get_fields_with_http_info(**kwargs)  # noqa: E501
            return data

    def get_fields_with_http_info(self, **kwargs):  # noqa: E501
        """List All Fields  # noqa: E501

        Returns a list of the fields available in the project.  # noqa: E501
        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please pass async_req=True
        >>> thread = api.get_fields_with_http_info(async_req=True)
        >>> result = thread.get()

        :param async_req bool
        :param int limit: A limit on the number of objects that are returned.
        :param list[str] sort: How to sort the returned items. `sort` is a CSV of fields used to sort the fetched items. Sorting defaults to ascending (ASC) order but a minus sign (` - `) can be used to reverse this to descending (DESC) order. Fields are prioritized by their order in the CSV. You can also use a ` ? ` to sort randomly. 
        :return: InlineResponse20019
                 If the method is called asynchronously,
                 returns the request thread.
        """

        all_params = ['limit', 'sort']  # noqa: E501
        all_params.append('async_req')
        all_params.append('_return_http_data_only')
        all_params.append('_preload_content')
        all_params.append('_request_timeout')

        params = locals()
        for key, val in six.iteritems(params['kwargs']):
            if key not in all_params:
                raise TypeError(
                    "Got an unexpected keyword argument '%s'"
                    " to method get_fields" % key
                )
            params[key] = val
        del params['kwargs']

        collection_formats = {}

        path_params = {}

        query_params = []
        if 'limit' in params:
            query_params.append(('limit', params['limit']))  # noqa: E501
        if 'sort' in params:
            query_params.append(('sort', params['sort']))  # noqa: E501
            collection_formats['sort'] = 'csv'  # noqa: E501

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
            '/fields', 'GET',
            path_params,
            query_params,
            header_params,
            body=body_params,
            post_params=form_params,
            files=local_var_files,
            response_type='InlineResponse20019',  # noqa: E501
            auth_settings=auth_settings,
            async_req=params.get('async_req'),
            _return_http_data_only=params.get('_return_http_data_only'),
            _preload_content=params.get('_preload_content', True),
            _request_timeout=params.get('_request_timeout'),
            collection_formats=collection_formats)

    def update_field(self, collection, id, **kwargs):  # noqa: E501
        """Update a Field  # noqa: E501

        Update an existing field.  # noqa: E501
        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please pass async_req=True
        >>> thread = api.update_field(collection, id, async_req=True)
        >>> result = thread.get()

        :param async_req bool
        :param str collection: Unique identifier of the collection the item resides in. (required)
        :param str id: Unique identifier of the field. (required)
        :param CollectionIdBody body:
        :return: InlineResponse20020
                 If the method is called asynchronously,
                 returns the request thread.
        """
        kwargs['_return_http_data_only'] = True
        if kwargs.get('async_req'):
            return self.update_field_with_http_info(collection, id, **kwargs)  # noqa: E501
        else:
            (data) = self.update_field_with_http_info(collection, id, **kwargs)  # noqa: E501
            return data

    def update_field_with_http_info(self, collection, id, **kwargs):  # noqa: E501
        """Update a Field  # noqa: E501

        Update an existing field.  # noqa: E501
        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please pass async_req=True
        >>> thread = api.update_field_with_http_info(collection, id, async_req=True)
        >>> result = thread.get()

        :param async_req bool
        :param str collection: Unique identifier of the collection the item resides in. (required)
        :param str id: Unique identifier of the field. (required)
        :param CollectionIdBody body:
        :return: InlineResponse20020
                 If the method is called asynchronously,
                 returns the request thread.
        """

        all_params = ['collection', 'id', 'body']  # noqa: E501
        all_params.append('async_req')
        all_params.append('_return_http_data_only')
        all_params.append('_preload_content')
        all_params.append('_request_timeout')

        params = locals()
        for key, val in six.iteritems(params['kwargs']):
            if key not in all_params:
                raise TypeError(
                    "Got an unexpected keyword argument '%s'"
                    " to method update_field" % key
                )
            params[key] = val
        del params['kwargs']
        # verify the required parameter 'collection' is set
        if ('collection' not in params or
                params['collection'] is None):
            raise ValueError("Missing the required parameter `collection` when calling `update_field`")  # noqa: E501
        # verify the required parameter 'id' is set
        if ('id' not in params or
                params['id'] is None):
            raise ValueError("Missing the required parameter `id` when calling `update_field`")  # noqa: E501

        collection_formats = {}

        path_params = {}
        if 'collection' in params:
            path_params['collection'] = params['collection']  # noqa: E501
        if 'id' in params:
            path_params['id'] = params['id']  # noqa: E501

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
            '/fields/{collection}/{id}', 'PATCH',
            path_params,
            query_params,
            header_params,
            body=body_params,
            post_params=form_params,
            files=local_var_files,
            response_type='InlineResponse20020',  # noqa: E501
            auth_settings=auth_settings,
            async_req=params.get('async_req'),
            _return_http_data_only=params.get('_return_http_data_only'),
            _preload_content=params.get('_preload_content', True),
            _request_timeout=params.get('_request_timeout'),
            collection_formats=collection_formats)