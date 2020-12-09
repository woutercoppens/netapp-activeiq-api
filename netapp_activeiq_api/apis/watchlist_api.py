# coding: utf-8

from .api_client import ApiClient


class WatchlistApi:
    def __init__(self, api_client=None):
        if api_client is None:
            api_client = ApiClient()
        self.api_client = api_client

    def create_watchlist(self, request_body, **kwargs):  # noqa: E501
        """Creates a watchlist with customers, sites, groups, global parents, domestic parents, districts, regions, serial numbers, partners, and sales representatives.  # noqa: E501

        Returns the watchlist ID and watchlist name after successful creation of watchlist.  # noqa: E501
        :param RequestBody2 request_body: (required)
        """

        all_params = ["request_body"]  # noqa: E501

        params = locals()
        for key, val in params["kwargs"].items():
            if key not in all_params:
                raise TypeError(
                    "Got an unexpected keyword argument '%s'"
                    " to method create_watchlist" % key
                )
            params[key] = val
        del params["kwargs"]
        # verify the required parameter 'request_body' is set
        if "request_body" not in params or params["request_body"] is None:
            raise ValueError(
                "Missing the required parameter `request_body` when calling `create_watchlist`"
            )  # noqa: E501

        path_params = {}

        query_params = []

        header_params = {}

        body_params = None
        if "request_body" in params:
            body_params = params["request_body"]

        return self.api_client.call_api(
            "/v1/watchlist/create",
            "POST",
            path_params,
            query_params,
            header_params,
            body=body_params,
        )

    def default_watchlist(self, watchlist_id, **kwargs):  # noqa: E501
        """Update one of the created watchlist as default, based on the user input.  # noqa: E501

        Update one of created watchlist as default as per User input.  # noqa: E501
        :param str authorization_token: Access token to use the API services. (required)
        :param str watchlist_id: Unique identifier for the watchlist ID. (required)
        """

        all_params = ["watchlist_id"]  # noqa: E501

        params = locals()
        for key, val in params["kwargs"].items():
            if key not in all_params:
                raise TypeError(
                    "Got an unexpected keyword argument '%s'"
                    " to method default_watchlist" % key
                )
            params[key] = val
        del params["kwargs"]
        # verify the required parameter 'watchlist_id' is set
        if "watchlist_id" not in params or params["watchlist_id"] is None:
            raise ValueError(
                "Missing the required parameter `watchlist_id` when calling `default_watchlist`"
            )  # noqa: E501

        path_params = {}
        if "watchlist_id" in params:
            path_params["watchlistId"] = params["watchlist_id"]  # noqa: E501

        query_params = []

        header_params = {}

        body_params = None

        return self.api_client.call_api(
            "/v1/watchlist/default/watchlistId/{watchlistId}",
            "PUT",
            path_params,
            query_params,
            header_params,
            body=body_params,
        )

    def delete_watchlist(self, watchlist_id, **kwargs):  # noqa: E501
        """Specifies the watchlist to be deleted by given Watchlist ID.  # noqa: E501

        Delete the watchlist for valid Watchlist ID.  # noqa: E501
        :param str watchlist_id: Unique identifier for the watchlist ID. (required)
        """

        all_params = ["watchlist_id"]  # noqa: E501

        params = locals()
        for key, val in params["kwargs"].items():
            if key not in all_params:
                raise TypeError(
                    "Got an unexpected keyword argument '%s'"
                    " to method delete_watchlist" % key
                )
            params[key] = val
        del params["kwargs"]
        # verify the required parameter 'watchlist_id' is set
        if "watchlist_id" not in params or params["watchlist_id"] is None:
            raise ValueError(
                "Missing the required parameter `watchlist_id` when calling `delete_watchlist`"
            )  # noqa: E501

        path_params = {}
        if "watchlist_id" in params:
            path_params["watchlistId"] = params["watchlist_id"]  # noqa: E501

        query_params = []

        header_params = {}

        body_params = None

        return self.api_client.call_api(
            "/v1/watchlist/delete/watchlistId/{watchlistId}",
            "DELETE",
            path_params,
            query_params,
            header_params,
            body=body_params,
        )

    def list_watchlist(self, **kwargs):  # noqa: E501
        """Provide list of watchlist details for the user.  # noqa: E501

        Returns the list of watchlist details based on User ID.  # noqa: E501
        """

        all_params = []  # noqa: E501

        params = locals()
        for key, val in params["kwargs"].items():
            if key not in all_params:
                raise TypeError(
                    "Got an unexpected keyword argument '%s'"
                    " to method list_watchlist" % key
                )
            params[key] = val
        del params["kwargs"]

        path_params = {}

        query_params = []

        header_params = {}

        body_params = None

        return self.api_client.call_api(
            "/v1/watchlist/all",
            "GET",
            path_params,
            query_params,
            header_params,
            body=body_params,
        )

    def share_watchlist(self, request_body, **kwargs):  # noqa: E501
        """The created watchlist, user can share among internal other users.  # noqa: E501

        User can share the created watchlist with other internal users.  # noqa: E501
        :param RequestBody3 request_body: (required)
        """

        all_params = ["request_body"]  # noqa: E501

        params = locals()
        for key, val in params["kwargs"].items():
            if key not in all_params:
                raise TypeError(
                    "Got an unexpected keyword argument '%s'"
                    " to method share_watchlist" % key
                )
            params[key] = val
        del params["kwargs"]
        # verify the required parameter 'request_body' is set
        if "request_body" not in params or params["request_body"] is None:
            raise ValueError(
                "Missing the required parameter `request_body` when calling `share_watchlist`"
            )  # noqa: E501

        path_params = {}

        query_params = []

        header_params = {}

        body_params = None
        if "request_body" in params:
            body_params = params["request_body"]

        return self.api_client.call_api(
            "/v1/watchlist/share",
            "PUT",
            path_params,
            query_params,
            header_params,
            body=body_params,
        )

    def system_count(self, watchlist_id, **kwargs):  # noqa: E501
        """Get the total system count for the given Watchlist ID.  # noqa: E501

        Get the total system count for the given Watchlist ID.  # noqa: E501
        :param str watchlist_id: Unique identifier for the Watchlist. (required)
        """

        all_params = ["watchlist_id"]  # noqa: E501

        params = locals()
        for key, val in params["kwargs"].items():
            if key not in all_params:
                raise TypeError(
                    "Got an unexpected keyword argument '%s'"
                    " to method system_count" % key
                )
            params[key] = val
        del params["kwargs"]
        # verify the required parameter 'watchlist_id' is set
        if "watchlist_id" not in params or params["watchlist_id"] is None:
            raise ValueError(
                "Missing the required parameter `watchlist_id` when calling `system_count`"
            )  # noqa: E501

        path_params = {}
        if "watchlist_id" in params:
            path_params["watchlistId"] = params["watchlist_id"]  # noqa: E501

        query_params = []

        header_params = {}

        body_params = None

        return self.api_client.call_api(
            "/v1/watchlist/count/watchlistId/{watchlistId}",
            "GET",
            path_params,
            query_params,
            header_params,
            body=body_params,
        )

    def update_watchlist(self, request_body, **kwargs):  # noqa: E501
        """Updates a watchlist with customers, sites, groups, global parents, domestic parents, districts, regions, serial numbers, partners, and sales representatives.  # noqa: E501

        Returns the watchlist ID and watchlist name after successful updated of watchlist.  # noqa: E501
        :param RequestBody4 request_body: (required)
        """

        all_params = ["request_body"]  # noqa: E501

        params = locals()
        for key, val in params["kwargs"].items():
            if key not in all_params:
                raise TypeError(
                    "Got an unexpected keyword argument '%s'"
                    " to method update_watchlist" % key
                )
            params[key] = val
        del params["kwargs"]
        # verify the required parameter 'request_body' is set
        if "request_body" not in params or params["request_body"] is None:
            raise ValueError(
                "Missing the required parameter `request_body` when calling `update_watchlist`"
            )  # noqa: E501

        path_params = {}

        query_params = []

        header_params = {}

        body_params = None
        if "request_body" in params:
            body_params = params["request_body"]

        return self.api_client.call_api(
            "/v1/watchlist/update",
            "PUT",
            path_params,
            query_params,
            header_params,
            body=body_params,
        )

    def view_watchlist(self, id, **kwargs):  # noqa: E501
        """Provides details about the watchlists that a user created by using customers, sites, groups, global parents, domestic parents, districts, regions, serial numbers, partners, and sales representatives.  # noqa: E501

        Returns the watchlist details based on user provided watchlist ID.  # noqa: E501
        :param str id: Unique identifier for the Watchlist ID. (required)
        """

        all_params = ["id"]  # noqa: E501

        params = locals()
        for key, val in params["kwargs"].items():
            if key not in all_params:
                raise TypeError(
                    "Got an unexpected keyword argument '%s'"
                    " to method view_watchlist" % key
                )
            params[key] = val
        del params["kwargs"]
        # verify the required parameter 'id' is set
        if "id" not in params or params["id"] is None:
            raise ValueError(
                "Missing the required parameter `id` when calling `view_watchlist`"
            )  # noqa: E501

        path_params = {}
        if "id" in params:
            path_params["id"] = params["id"]  # noqa: E501

        query_params = []

        header_params = {}

        body_params = None

        return self.api_client.call_api(
            "/v1/watchlist/id/{id}",
            "GET",
            path_params,
            query_params,
            header_params,
            body=body_params,
        )
