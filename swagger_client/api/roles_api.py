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


class RolesApi(object):
    """NOTE: This class is auto generated by the swagger code generator program.

    Do not edit the class manually.
    Ref: https://github.com/swagger-api/swagger-codegen
    """

    def __init__(self, api_client=None):
        if api_client is None:
            api_client = ApiClient()
        self.api_client = api_client

    def create_role(self, **kwargs):  # noqa: E501
        """Create a Role  # noqa: E501

        Create a new role.  # noqa: E501
        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please pass async_req=True
        >>> thread = api.create_role(async_req=True)
        >>> result = thread.get()

        :param async_req bool
        :param RolesBody body:
        :param list[str] fields: Control what fields are being returned in the object.
        :param str meta: What metadata to return in the response.
        :return: InlineResponse20039
                 If the method is called asynchronously,
                 returns the request thread.
        """
        kwargs['_return_http_data_only'] = True
        if kwargs.get('async_req'):
            return self.create_role_with_http_info(**kwargs)  # noqa: E501
        else:
            (data) = self.create_role_with_http_info(**kwargs)  # noqa: E501
            return data

    def create_role_with_http_info(self, **kwargs):  # noqa: E501
        """Create a Role  # noqa: E501

        Create a new role.  # noqa: E501
        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please pass async_req=True
        >>> thread = api.create_role_with_http_info(async_req=True)
        >>> result = thread.get()

        :param async_req bool
        :param RolesBody body:
        :param list[str] fields: Control what fields are being returned in the object.
        :param str meta: What metadata to return in the response.
        :return: InlineResponse20039
                 If the method is called asynchronously,
                 returns the request thread.
        """

        all_params = ['body', 'fields', 'meta']  # noqa: E501
        all_params.append('async_req')
        all_params.append('_return_http_data_only')
        all_params.append('_preload_content')
        all_params.append('_request_timeout')

        params = locals()
        for key, val in six.iteritems(params['kwargs']):
            if key not in all_params:
                raise TypeError(
                    "Got an unexpected keyword argument '%s'"
                    " to method create_role" % key
                )
            params[key] = val
        del params['kwargs']

        collection_formats = {}

        path_params = {}

        query_params = []
        if 'fields' in params:
            query_params.append(('fields', params['fields']))  # noqa: E501
            collection_formats['fields'] = 'csv'  # noqa: E501
        if 'meta' in params:
            query_params.append(('meta', params['meta']))  # noqa: E501

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
            '/roles', 'POST',
            path_params,
            query_params,
            header_params,
            body=body_params,
            post_params=form_params,
            files=local_var_files,
            response_type='InlineResponse20039',  # noqa: E501
            auth_settings=auth_settings,
            async_req=params.get('async_req'),
            _return_http_data_only=params.get('_return_http_data_only'),
            _preload_content=params.get('_preload_content', True),
            _request_timeout=params.get('_request_timeout'),
            collection_formats=collection_formats)

    def delete_role(self, id, **kwargs):  # noqa: E501
        """Delete a Role  # noqa: E501

        Delete an existing role  # noqa: E501
        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please pass async_req=True
        >>> thread = api.delete_role(id, async_req=True)
        >>> result = thread.get()

        :param async_req bool
        :param str id: Unique identifier for the object. (required)
        :return: None
                 If the method is called asynchronously,
                 returns the request thread.
        """
        kwargs['_return_http_data_only'] = True
        if kwargs.get('async_req'):
            return self.delete_role_with_http_info(id, **kwargs)  # noqa: E501
        else:
            (data) = self.delete_role_with_http_info(id, **kwargs)  # noqa: E501
            return data

    def delete_role_with_http_info(self, id, **kwargs):  # noqa: E501
        """Delete a Role  # noqa: E501

        Delete an existing role  # noqa: E501
        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please pass async_req=True
        >>> thread = api.delete_role_with_http_info(id, async_req=True)
        >>> result = thread.get()

        :param async_req bool
        :param str id: Unique identifier for the object. (required)
        :return: None
                 If the method is called asynchronously,
                 returns the request thread.
        """

        all_params = ['id']  # noqa: E501
        all_params.append('async_req')
        all_params.append('_return_http_data_only')
        all_params.append('_preload_content')
        all_params.append('_request_timeout')

        params = locals()
        for key, val in six.iteritems(params['kwargs']):
            if key not in all_params:
                raise TypeError(
                    "Got an unexpected keyword argument '%s'"
                    " to method delete_role" % key
                )
            params[key] = val
        del params['kwargs']
        # verify the required parameter 'id' is set
        if ('id' not in params or
                params['id'] is None):
            raise ValueError("Missing the required parameter `id` when calling `delete_role`")  # noqa: E501

        collection_formats = {}

        path_params = {}
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
            '/roles/{id}', 'DELETE',
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

    def delete_roles(self, **kwargs):  # noqa: E501
        """Delete Multiple Roles  # noqa: E501

        Delete multiple existing roles.  # noqa: E501
        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please pass async_req=True
        >>> thread = api.delete_roles(async_req=True)
        >>> result = thread.get()

        :param async_req bool
        :return: None
                 If the method is called asynchronously,
                 returns the request thread.
        """
        kwargs['_return_http_data_only'] = True
        if kwargs.get('async_req'):
            return self.delete_roles_with_http_info(**kwargs)  # noqa: E501
        else:
            (data) = self.delete_roles_with_http_info(**kwargs)  # noqa: E501
            return data

    def delete_roles_with_http_info(self, **kwargs):  # noqa: E501
        """Delete Multiple Roles  # noqa: E501

        Delete multiple existing roles.  # noqa: E501
        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please pass async_req=True
        >>> thread = api.delete_roles_with_http_info(async_req=True)
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
                    " to method delete_roles" % key
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
        # HTTP header `Accept`
        header_params['Accept'] = self.api_client.select_header_accept(
            ['application/json'])  # noqa: E501

        # Authentication setting
        auth_settings = []  # noqa: E501

        return self.api_client.call_api(
            '/roles', 'DELETE',
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

    def get_role(self, id, **kwargs):  # noqa: E501
        """Retrieve a Role  # noqa: E501

        Retrieve a single role by unique identifier.  # noqa: E501
        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please pass async_req=True
        >>> thread = api.get_role(id, async_req=True)
        >>> result = thread.get()

        :param async_req bool
        :param str id: Unique identifier for the object. (required)
        :param list[str] fields: Control what fields are being returned in the object.
        :param str meta: What metadata to return in the response.
        :return: InlineResponse20039
                 If the method is called asynchronously,
                 returns the request thread.
        """
        kwargs['_return_http_data_only'] = True
        if kwargs.get('async_req'):
            return self.get_role_with_http_info(id, **kwargs)  # noqa: E501
        else:
            (data) = self.get_role_with_http_info(id, **kwargs)  # noqa: E501
            return data

    def get_role_with_http_info(self, id, **kwargs):  # noqa: E501
        """Retrieve a Role  # noqa: E501

        Retrieve a single role by unique identifier.  # noqa: E501
        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please pass async_req=True
        >>> thread = api.get_role_with_http_info(id, async_req=True)
        >>> result = thread.get()

        :param async_req bool
        :param str id: Unique identifier for the object. (required)
        :param list[str] fields: Control what fields are being returned in the object.
        :param str meta: What metadata to return in the response.
        :return: InlineResponse20039
                 If the method is called asynchronously,
                 returns the request thread.
        """

        all_params = ['id', 'fields', 'meta']  # noqa: E501
        all_params.append('async_req')
        all_params.append('_return_http_data_only')
        all_params.append('_preload_content')
        all_params.append('_request_timeout')

        params = locals()
        for key, val in six.iteritems(params['kwargs']):
            if key not in all_params:
                raise TypeError(
                    "Got an unexpected keyword argument '%s'"
                    " to method get_role" % key
                )
            params[key] = val
        del params['kwargs']
        # verify the required parameter 'id' is set
        if ('id' not in params or
                params['id'] is None):
            raise ValueError("Missing the required parameter `id` when calling `get_role`")  # noqa: E501

        collection_formats = {}

        path_params = {}
        if 'id' in params:
            path_params['id'] = params['id']  # noqa: E501

        query_params = []
        if 'fields' in params:
            query_params.append(('fields', params['fields']))  # noqa: E501
            collection_formats['fields'] = 'csv'  # noqa: E501
        if 'meta' in params:
            query_params.append(('meta', params['meta']))  # noqa: E501

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
            '/roles/{id}', 'GET',
            path_params,
            query_params,
            header_params,
            body=body_params,
            post_params=form_params,
            files=local_var_files,
            response_type='InlineResponse20039',  # noqa: E501
            auth_settings=auth_settings,
            async_req=params.get('async_req'),
            _return_http_data_only=params.get('_return_http_data_only'),
            _preload_content=params.get('_preload_content', True),
            _request_timeout=params.get('_request_timeout'),
            collection_formats=collection_formats)

    def get_roles(self, **kwargs):  # noqa: E501
        """List Roles  # noqa: E501

        List the roles.  # noqa: E501
        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please pass async_req=True
        >>> thread = api.get_roles(async_req=True)
        >>> result = thread.get()

        :param async_req bool
        :param list[str] fields: Control what fields are being returned in the object.
        :param int limit: A limit on the number of objects that are returned.
        :param int offset: How many items to skip when fetching data.
        :param str meta: What metadata to return in the response.
        :param list[str] sort: How to sort the returned items. `sort` is a CSV of fields used to sort the fetched items. Sorting defaults to ascending (ASC) order but a minus sign (` - `) can be used to reverse this to descending (DESC) order. Fields are prioritized by their order in the CSV. You can also use a ` ? ` to sort randomly. 
        :param object filter: Select items in collection by given conditions.
        :param str search: Filter by items that contain the given search query in one of their fields.
        :param int page: Cursor for use in pagination. Often used in combination with limit.
        :return: InlineResponse20038
                 If the method is called asynchronously,
                 returns the request thread.
        """
        kwargs['_return_http_data_only'] = True
        if kwargs.get('async_req'):
            return self.get_roles_with_http_info(**kwargs)  # noqa: E501
        else:
            (data) = self.get_roles_with_http_info(**kwargs)  # noqa: E501
            return data

    def get_roles_with_http_info(self, **kwargs):  # noqa: E501
        """List Roles  # noqa: E501

        List the roles.  # noqa: E501
        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please pass async_req=True
        >>> thread = api.get_roles_with_http_info(async_req=True)
        >>> result = thread.get()

        :param async_req bool
        :param list[str] fields: Control what fields are being returned in the object.
        :param int limit: A limit on the number of objects that are returned.
        :param int offset: How many items to skip when fetching data.
        :param str meta: What metadata to return in the response.
        :param list[str] sort: How to sort the returned items. `sort` is a CSV of fields used to sort the fetched items. Sorting defaults to ascending (ASC) order but a minus sign (` - `) can be used to reverse this to descending (DESC) order. Fields are prioritized by their order in the CSV. You can also use a ` ? ` to sort randomly. 
        :param object filter: Select items in collection by given conditions.
        :param str search: Filter by items that contain the given search query in one of their fields.
        :param int page: Cursor for use in pagination. Often used in combination with limit.
        :return: InlineResponse20038
                 If the method is called asynchronously,
                 returns the request thread.
        """

        all_params = ['fields', 'limit', 'offset', 'meta', 'sort', 'filter', 'search', 'page']  # noqa: E501
        all_params.append('async_req')
        all_params.append('_return_http_data_only')
        all_params.append('_preload_content')
        all_params.append('_request_timeout')

        params = locals()
        for key, val in six.iteritems(params['kwargs']):
            if key not in all_params:
                raise TypeError(
                    "Got an unexpected keyword argument '%s'"
                    " to method get_roles" % key
                )
            params[key] = val
        del params['kwargs']

        collection_formats = {}

        path_params = {}

        query_params = []
        if 'fields' in params:
            query_params.append(('fields', params['fields']))  # noqa: E501
            collection_formats['fields'] = 'csv'  # noqa: E501
        if 'limit' in params:
            query_params.append(('limit', params['limit']))  # noqa: E501
        if 'offset' in params:
            query_params.append(('offset', params['offset']))  # noqa: E501
        if 'meta' in params:
            query_params.append(('meta', params['meta']))  # noqa: E501
        if 'sort' in params:
            query_params.append(('sort', params['sort']))  # noqa: E501
            collection_formats['sort'] = 'csv'  # noqa: E501
        if 'filter' in params:
            query_params.append(('filter', params['filter']))  # noqa: E501
        if 'search' in params:
            query_params.append(('search', params['search']))  # noqa: E501
        if 'page' in params:
            query_params.append(('page', params['page']))  # noqa: E501

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
            '/roles', 'GET',
            path_params,
            query_params,
            header_params,
            body=body_params,
            post_params=form_params,
            files=local_var_files,
            response_type='InlineResponse20038',  # noqa: E501
            auth_settings=auth_settings,
            async_req=params.get('async_req'),
            _return_http_data_only=params.get('_return_http_data_only'),
            _preload_content=params.get('_preload_content', True),
            _request_timeout=params.get('_request_timeout'),
            collection_formats=collection_formats)

    def update_role(self, id, **kwargs):  # noqa: E501
        """Update a Role  # noqa: E501

        Update an existing role  # noqa: E501
        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please pass async_req=True
        >>> thread = api.update_role(id, async_req=True)
        >>> result = thread.get()

        :param async_req bool
        :param str id: Unique identifier for the object. (required)
        :param RolesIdBody body:
        :param list[str] fields: Control what fields are being returned in the object.
        :param str meta: What metadata to return in the response.
        :return: InlineResponse20039
                 If the method is called asynchronously,
                 returns the request thread.
        """
        kwargs['_return_http_data_only'] = True
        if kwargs.get('async_req'):
            return self.update_role_with_http_info(id, **kwargs)  # noqa: E501
        else:
            (data) = self.update_role_with_http_info(id, **kwargs)  # noqa: E501
            return data

    def update_role_with_http_info(self, id, **kwargs):  # noqa: E501
        """Update a Role  # noqa: E501

        Update an existing role  # noqa: E501
        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please pass async_req=True
        >>> thread = api.update_role_with_http_info(id, async_req=True)
        >>> result = thread.get()

        :param async_req bool
        :param str id: Unique identifier for the object. (required)
        :param RolesIdBody body:
        :param list[str] fields: Control what fields are being returned in the object.
        :param str meta: What metadata to return in the response.
        :return: InlineResponse20039
                 If the method is called asynchronously,
                 returns the request thread.
        """

        all_params = ['id', 'body', 'fields', 'meta']  # noqa: E501
        all_params.append('async_req')
        all_params.append('_return_http_data_only')
        all_params.append('_preload_content')
        all_params.append('_request_timeout')

        params = locals()
        for key, val in six.iteritems(params['kwargs']):
            if key not in all_params:
                raise TypeError(
                    "Got an unexpected keyword argument '%s'"
                    " to method update_role" % key
                )
            params[key] = val
        del params['kwargs']
        # verify the required parameter 'id' is set
        if ('id' not in params or
                params['id'] is None):
            raise ValueError("Missing the required parameter `id` when calling `update_role`")  # noqa: E501

        collection_formats = {}

        path_params = {}
        if 'id' in params:
            path_params['id'] = params['id']  # noqa: E501

        query_params = []
        if 'fields' in params:
            query_params.append(('fields', params['fields']))  # noqa: E501
            collection_formats['fields'] = 'csv'  # noqa: E501
        if 'meta' in params:
            query_params.append(('meta', params['meta']))  # noqa: E501

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
            '/roles/{id}', 'PATCH',
            path_params,
            query_params,
            header_params,
            body=body_params,
            post_params=form_params,
            files=local_var_files,
            response_type='InlineResponse20039',  # noqa: E501
            auth_settings=auth_settings,
            async_req=params.get('async_req'),
            _return_http_data_only=params.get('_return_http_data_only'),
            _preload_content=params.get('_preload_content', True),
            _request_timeout=params.get('_request_timeout'),
            collection_formats=collection_formats)

    def update_roles(self, **kwargs):  # noqa: E501
        """Update Multiple Roles  # noqa: E501

        Update multiple roles at the same time.  # noqa: E501
        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please pass async_req=True
        >>> thread = api.update_roles(async_req=True)
        >>> result = thread.get()

        :param async_req bool
        :param RolesBody1 body:
        :param list[str] fields: Control what fields are being returned in the object.
        :param int limit: A limit on the number of objects that are returned.
        :param str meta: What metadata to return in the response.
        :param int offset: How many items to skip when fetching data.
        :param list[str] sort: How to sort the returned items. `sort` is a CSV of fields used to sort the fetched items. Sorting defaults to ascending (ASC) order but a minus sign (` - `) can be used to reverse this to descending (DESC) order. Fields are prioritized by their order in the CSV. You can also use a ` ? ` to sort randomly. 
        :param object filter: Select items in collection by given conditions.
        :param str search: Filter by items that contain the given search query in one of their fields.
        :return: InlineResponse20038
                 If the method is called asynchronously,
                 returns the request thread.
        """
        kwargs['_return_http_data_only'] = True
        if kwargs.get('async_req'):
            return self.update_roles_with_http_info(**kwargs)  # noqa: E501
        else:
            (data) = self.update_roles_with_http_info(**kwargs)  # noqa: E501
            return data

    def update_roles_with_http_info(self, **kwargs):  # noqa: E501
        """Update Multiple Roles  # noqa: E501

        Update multiple roles at the same time.  # noqa: E501
        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please pass async_req=True
        >>> thread = api.update_roles_with_http_info(async_req=True)
        >>> result = thread.get()

        :param async_req bool
        :param RolesBody1 body:
        :param list[str] fields: Control what fields are being returned in the object.
        :param int limit: A limit on the number of objects that are returned.
        :param str meta: What metadata to return in the response.
        :param int offset: How many items to skip when fetching data.
        :param list[str] sort: How to sort the returned items. `sort` is a CSV of fields used to sort the fetched items. Sorting defaults to ascending (ASC) order but a minus sign (` - `) can be used to reverse this to descending (DESC) order. Fields are prioritized by their order in the CSV. You can also use a ` ? ` to sort randomly. 
        :param object filter: Select items in collection by given conditions.
        :param str search: Filter by items that contain the given search query in one of their fields.
        :return: InlineResponse20038
                 If the method is called asynchronously,
                 returns the request thread.
        """

        all_params = ['body', 'fields', 'limit', 'meta', 'offset', 'sort', 'filter', 'search']  # noqa: E501
        all_params.append('async_req')
        all_params.append('_return_http_data_only')
        all_params.append('_preload_content')
        all_params.append('_request_timeout')

        params = locals()
        for key, val in six.iteritems(params['kwargs']):
            if key not in all_params:
                raise TypeError(
                    "Got an unexpected keyword argument '%s'"
                    " to method update_roles" % key
                )
            params[key] = val
        del params['kwargs']

        collection_formats = {}

        path_params = {}

        query_params = []
        if 'fields' in params:
            query_params.append(('fields', params['fields']))  # noqa: E501
            collection_formats['fields'] = 'csv'  # noqa: E501
        if 'limit' in params:
            query_params.append(('limit', params['limit']))  # noqa: E501
        if 'meta' in params:
            query_params.append(('meta', params['meta']))  # noqa: E501
        if 'offset' in params:
            query_params.append(('offset', params['offset']))  # noqa: E501
        if 'sort' in params:
            query_params.append(('sort', params['sort']))  # noqa: E501
            collection_formats['sort'] = 'csv'  # noqa: E501
        if 'filter' in params:
            query_params.append(('filter', params['filter']))  # noqa: E501
        if 'search' in params:
            query_params.append(('search', params['search']))  # noqa: E501

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
            '/roles', 'PATCH',
            path_params,
            query_params,
            header_params,
            body=body_params,
            post_params=form_params,
            files=local_var_files,
            response_type='InlineResponse20038',  # noqa: E501
            auth_settings=auth_settings,
            async_req=params.get('async_req'),
            _return_http_data_only=params.get('_return_http_data_only'),
            _preload_content=params.get('_preload_content', True),
            _request_timeout=params.get('_request_timeout'),
            collection_formats=collection_formats)
