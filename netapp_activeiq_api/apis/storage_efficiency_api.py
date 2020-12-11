# coding: utf-8

from .api_client import ApiClient


class StorageEfficiencyApi:
    def __init__(self, api_client=None):
        if api_client is None:
            api_client = ApiClient()
        self.api_client = api_client

    # Version 2 API's

    def get_efficiency_details_by_level(
        self, source, id, level, **kwargs
    ):  # noqa: E501
        """Provides information about system efficiency based on different parameters at the customer,site,group,cluster or system level.  # noqa: E501

        Provides information about system efficiency based on different parameters at the customer,site,group,cluster or system level.\"   # noqa: E501
        :param str source: The source from where this service is being invoked. (required)
        :param str id: Valid values are customer ID, site ID, group Name,serial Numbers and cluster ID. (required)
        :param str level: Valid values are customer, site, group, serial_numbers and cluster. (required)
        :param str aff: Specifies if the systems are AFF or NONAFF.
        """

        all_params = ["source", "id", "level", "aff"]  # noqa: E501

        params = locals()
        for key, val in params["kwargs"].items():
            if key not in all_params:
                raise TypeError(
                    "Got an unexpected keyword argument '%s'"
                    " to method se_details" % key
                )
            params[key] = val
        del params["kwargs"]
        # verify the required parameter 'source' is set
        if "source" not in params or params["source"] is None:
            raise ValueError(
                "Missing the required parameter `source` when calling `get_efficiency_details_by_level`"
            )  # noqa: E501
        # verify the required parameter 'id' is set
        if "id" not in params or params["id"] is None:
            raise ValueError(
                "Missing the required parameter `id` when calling `get_efficiency_details_by_level`"
            )  # noqa: E501
        # verify the required parameter 'level' is set
        if "level" not in params or params["level"] is None:
            raise ValueError(
                "Missing the required parameter `level` when calling `get_efficiency_details_by_level`"
            )  # noqa: E501

        path_params = {}
        if "id" in params:
            path_params["id"] = params["id"]  # noqa: E501
        if "level" in params:
            path_params["level"] = params["level"]  # noqa: E501

        query_params = []
        if "aff" in params:
            query_params.append(("aff", params["aff"]))  # noqa: E501

        header_params = {}
        if "source" in params:
            header_params["source"] = params["source"]  # noqa: E501

        body_params = None

        return self.api_client.call_api(
            "/v1/efficiency/details/level/{level}/id/{id}",
            "GET",
            path_params,
            query_params,
            header_params,
            body=body_params,
        )

    # Version 1 API's

    def get_efficiency_summary_by_level(self, id, level, **kwargs):  # noqa: E501
        """Provides details about the systems with maximum capacity savings for a customer, site, group, or a set of serial numbers.  # noqa: E501

        Lists information about the top 5 systems with maximum capacity savings as a result of storage efficiency features for a customer, site, group, or a set of serial numbers.  # noqa: E501
        :param str id: Unique identifier for the level. Valid values are customer ID, site ID, group name, and serial numbers. (required)
        :param str level: Identifies the level for which information will be provided. Valid values are customer, site, group, and serial_numbers.  (required)
        """

        all_params = ["id", "level"]  # noqa: E501

        params = locals()
        for key, val in params["kwargs"].items():
            if key not in all_params:
                raise TypeError(
                    "Got an unexpected keyword argument '%s'"
                    " to method get_efficiency_summary_by_level" % key
                )
            params[key] = val
        del params["kwargs"]
        # verify the required parameter 'id' is set
        if "id" not in params or params["id"] is None:
            raise ValueError(
                "Missing the required parameter `id` when calling `get_efficiency_summary_by_level`"
            )  # noqa: E501
        # verify the required parameter 'level' is set
        if "level" not in params or params["level"] is None:
            raise ValueError(
                "Missing the required parameter `level` when calling `get_efficiency_summary_by_level`"
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
            "/v1/efficiency/summary/level/{level}/id/{id}",
            "GET",
            path_params,
            query_params,
            header_params,
            body=body_params,
        )

    def get_efficiency_summary(self, **kwargs):  # noqa: E501
        """Provides details about the systems with maximum capacity savings for a customer, site, group, or a set of serial numbers.  # noqa: E501

        Provides details about the storage efficiency of the systems for a customer, site, group, or a set of serial numbers. The results are provided in a paginated manner.  # noqa: E501
        :param str customer: Customer ID for which data is to be returned.
        :param str site: Site ID for which data is to be returned.
        :param str group: Name of the group for which data is to be returned.
        :param str cluster: Cluster ID for which data is to be returned.
        :param str serial_numbers: Comma-separated list of serial numbers for which data is to be returned.
        :param float start: Specifies the index of the first efficiency details to be returned.
        :param float limit: Specifies the number of efficiency details to be displayed on a page. The default limit is 1000.
        """

        all_params = [
            "customer",
            "site",
            "group",
            "cluster",
            "serial_numbers",
            "start",
            "limit",
        ]  # noqa: E501

        params = locals()
        for key, val in params["kwargs"].items():
            if key not in all_params:
                raise TypeError(
                    "Got an unexpected keyword argument '%s'"
                    " to method get_efficiency_summary" % key
                )
            params[key] = val
        del params["kwargs"]

        path_params = {}

        query_params = []
        if "customer" in params:
            query_params.append(("customer", params["customer"]))  # noqa: E501
        if "site" in params:
            query_params.append(("site", params["site"]))  # noqa: E501
        if "group" in params:
            query_params.append(("group", params["group"]))  # noqa: E501
        if "cluster" in params:
            query_params.append(("cluster", params["cluster"]))  # noqa: E501
        if "serial_numbers" in params:
            query_params.append(
                ("serialNumbers", params["serial_numbers"])
            )  # noqa: E501
        if "start" in params:
            query_params.append(("start", params["start"]))  # noqa: E501
        if "limit" in params:
            query_params.append(("limit", params["limit"]))  # noqa: E501

        header_params = {}

        body_params = None

        return self.api_client.call_api(
            "/v2/efficiency/summary",
            "GET",
            path_params,
            query_params,
            header_params,
            body=body_params,
        )
