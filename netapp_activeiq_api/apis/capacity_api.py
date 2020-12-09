# coding: utf-8

from .api_client import ApiClient


class CapacityApi:
    def __init__(self, api_client=None):
        if api_client is None:
            api_client = ApiClient()
        self.api_client = api_client

    def get_capacity_details_by_level_v2(self, id, level, **kwargs):  # noqa: E501
        """Provides the details about the systems nearing allocated capacity limit for a customer, site, group, cluster, watchlist or a set of serial numbers.   # noqa: E501
        Lists information about systems for a customer, site, group, cluster, watchlist or serial numbers that have exceeded 90 percent system capacity or are predicted to do so soon.  Systems are grouped into the following categories: currently above 90 percent, expected to exceed 90 percent within 1 month, expected to exceed 90 percent within 3 months, expected to exceed 90 percent within 6 months, not expected to exceed 90 percent within 6 months.   # noqa: E501

        :param str id: Unique identifier for the level. Valid values are customer ID, site ID, group name, cluster, serial numbers and watchList id. (required)
        :param str level: Identifies the level for which information will be provided. Valid values are customer, site, group, cluster, serial_numbers and watchlist.  (required)
        """

        all_params = ["id", "level"]  # noqa: E501

        params = locals()
        for key, val in params["kwargs"].items():
            if key not in all_params:
                raise TypeError(
                    "Got an unexpected keyword argument '%s'"
                    " to method get_capacity_details_by_level_v2" % key
                )
            params[key] = val
        del params["kwargs"]
        # verify the required parameter 'id' is set
        if "id" not in params or params["id"] is None:
            raise ValueError(
                "Missing the required parameter `id` when calling `get_capacity_details_by_level_v2`"
            )  # noqa: E501
        # verify the required parameter 'level' is set
        if "level" not in params or params["level"] is None:
            raise ValueError(
                "Missing the required parameter `level` when calling `get_capacity_details_by_level_v2`"
            )  # noqa: E501

        path_params = {}
        if "id" in params:
            path_params["id"] = params["id"]  # noqa: E501
        if "level" in params:
            path_params["level"] = params["level"]  # noqa: E501

        query_params = []

        header_params = {}

        body_params = None

        return self.api_client.call_api(
            "/v2/capacity/details/level/{level}/id/{id}",
            "GET",
            path_params,
            query_params,
            header_params,
            body=body_params,
        )

    def get_capacity_summary_by_level_v2(self, id, level, **kwargs):  # noqa: E501
        """Provides the number of systems nearing allocated capacity limit for a customer, site, group, cluster watchlist or a set of serial numbers.  # noqa: E501
        Lists the number of systems for a customer, site, group, cluster, watchlist or a set of serial numbers that have exceeded 90 percent system capacity or are predicted to do so soon.  Counts are provided for the following categories: currently above 90 percent, expected to exceed 90 percent within 1 month, expected to exceed 90 percent within 3 months, expected to exceed 90 percent within 6 months, sum of systems which are above 90 percent and expected to exceed 90 percent in 6 months, not expected to exceed 90 percent within 6 months.   # noqa: E501

        :param str id: Unique identifier for the level. Valid values are customer ID, site ID, group name, cluster id, serial numbers and watchList id. (required)
        :param str level: Identifies the level for which information will be provided. Valid values are customer, site, group, cluster, serial_numbers and watchlist.  (required)
        """

        all_params = ["id", "level"]  # noqa: E501

        params = locals()
        for key, val in params["kwargs"].items():
            if key not in all_params:
                raise TypeError(
                    "Got an unexpected keyword argument '%s'"
                    " to method get_capacity_summary_by_level_v2" % key
                )
            params[key] = val
        del params["kwargs"]
        # verify the required parameter 'id' is set
        if "id" not in params or params["id"] is None:
            raise ValueError(
                "Missing the required parameter `id` when calling `get_capacity_summary_by_level_v2`"
            )  # noqa: E501
        # verify the required parameter 'level' is set
        if "level" not in params or params["level"] is None:
            raise ValueError(
                "Missing the required parameter `level` when calling `get_capacity_summary_by_level_v2`"
            )  # noqa: E501

        path_params = {}
        if "id" in params:
            path_params["id"] = params["id"]  # noqa: E501
        if "level" in params:
            path_params["level"] = params["level"]  # noqa: E501

        query_params = []

        header_params = {}

        body_params = None

        return self.api_client.call_api(
            "/v2/capacity/summary/level/{level}/id/{id}",
            "GET",
            path_params,
            query_params,
            header_params,
            body=body_params,
        )

    def get_capacity_trend_details_by_level(self, level, id, **kwargs):  # noqa: E501
        """Provides the capacity trending details about the systems for a customer, site, group, or a set of serial numbers.  # noqa: E501
        Returns the used and allocated capacity for each of the last 6 months of available data for each system by pagination   # noqa: E501

        :param str level: Identifies the level for which information will be provided. Valid values are customer, site, group, and serial_numbers.  (required)
        :param str id: Unique identifier for the level. Valid values are customer ID, site ID, group name, and serial numbers. (required)
        :param float start: The index of the first system to return.
        :param float limit: Specifies the number of systems to be displayed on a page. The default value is 1000.
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
            "/v1/capacity/trend/level/{level}/id/{id}",
            "GET",
            path_params,
            query_params,
            header_params,
            body=body_params,
        )
