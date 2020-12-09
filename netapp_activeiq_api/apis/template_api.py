# coding: utf-8

# import re  # noqa: F401
# from typing import Dict

from .api_client import ApiClient


class ExampleApi:
    def __init__(self, api_client=None):
        if api_client is None:
            api_client = ApiClient()
        self.api_client = api_client

    def example_function(self, id, level, **kwargs):  # noqa: E501
        """Provides the details about the systems .....   # noqa: E501
        Lists information about systems for a customer...

        :param str id: Unique identifier for the level. Valid values are customer ID, site ID, group name, cluster, serial numbers and watchList id. (required)
        :param str level: Identifies the level for which information will be provided. Valid values are customer, site, group, cluster, serial_numbers and watchlist.  (required)
        """

        all_params = ["level", "id", "start", "limit"]  # noqa: E501

        params = locals()
        for key, val in params["kwargs"].items():
            if key not in all_params:
                raise TypeError(
                    "Got an unexpected keyword argument '%s'"
                    " to method get_capacity_trend_details_by_level" % key
                )
            params[key] = val
        del params["kwargs"]
        # verify the required parameter 'level' is set
        if "level" not in params or params["level"] is None:
            raise ValueError(
                "Missing the required parameter `level` when calling `get_capacity_trend_details_by_level`"
            )  # noqa: E501
        # verify the required parameter 'id' is set
        if "id" not in params or params["id"] is None:
            raise ValueError(
                "Missing the required parameter `id` when calling `get_capacity_trend_details_by_level`"
            )  # noqa: E501

        path_params = {}
        if "level" in params:
            path_params["level"] = params["level"]  # noqa: E501
        if "id" in params:
            path_params["id"] = params["id"]  # noqa: E501

        query_params = []
        if "start" in params:
            query_params.append(("start", params["start"]))  # noqa: E501
        if "limit" in params:
            query_params.append(("limit", params["limit"]))  # noqa: E501

        header_params = {}

        body_params = None

        return self.api_client.call_api(
            "/v2/path/path/{level}/id/{id}",
            "GET",
            path_params,
            query_params,
            header_params,
            body=body_params,
        )
