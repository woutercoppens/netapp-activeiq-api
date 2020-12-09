# coding: utf-8

from .api_client import ApiClient


class SearchApi:
    def __init__(self, api_client=None):
        if api_client is None:
            api_client = ApiClient()
        self.api_client = api_client

    def search_aggregate_by_level(self, level, **kwargs):  # noqa: E501
        """Infers information about the customer, site, cluster, or group based on the entered keywords  # noqa: E501

        Infers information about the customer, site, cluster, or group based on the entered keywords. The system displays only the names that start with the entered text. For example: If the user searches for 'xyz' customers, then the search displays only customers starting with 'xyz'.   # noqa: E501
        :param str level: Specifies a unique identifier for the level.  (required)
        :param str name: Specifies the name of the customer, site, cluster, or group used for search.
        """

        all_params = ["level", "name"]  # noqa: E501

        params = locals()
        for key, val in params["kwargs"].items():
            if key not in all_params:
                raise TypeError(
                    "Got an unexpected keyword argument '%s'"
                    " to method search_aggregate_by_level" % key
                )
            params[key] = val
        del params["kwargs"]
        # verify the required parameter 'level' is set
        if "level" not in params or params["level"] is None:
            raise ValueError(
                "Missing the required parameter `level` when calling `search_aggregate_by_level`"
            )  # noqa: E501

        path_params = {}
        if "level" in params:
            path_params["level"] = params["level"]  # noqa: E501

        query_params = []
        if "name" in params:
            query_params.append(("name", params["name"]))  # noqa: E501

        header_params = {}

        body_params = None

        return self.api_client.call_api(
            "/v1/search/aggregate/level/{level}",
            "GET",
            path_params,
            query_params,
            header_params,
            body=body_params,
        )

    def search_aggregate_count_by_level(self, level, **kwargs):  # noqa: E501
        """Provides the aggregate count based on the input provided by the user.  # noqa: E501

        Infers information about the customer, site or group based on the ID entered.  # noqa: E501
        :param str level: Identifies the level for which information will be provided.  (required)
        :param str name: ID of the customer, site, or group that is used to search.
        """

        all_params = ["level", "name"]  # noqa: E501

        params = locals()
        for key, val in params["kwargs"].items():
            if key not in all_params:
                raise TypeError(
                    "Got an unexpected keyword argument '%s'"
                    " to method search_aggregate_count_by_level" % key
                )
            params[key] = val
        del params["kwargs"]
        # verify the required parameter 'level' is set
        if "level" not in params or params["level"] is None:
            raise ValueError(
                "Missing the required parameter `level` when calling `search_aggregate_count_by_level`"
            )  # noqa: E501

        path_params = {}
        if "level" in params:
            path_params["level"] = params["level"]  # noqa: E501

        query_params = []
        if "name" in params:
            query_params.append(("name", params["name"]))  # noqa: E501

        header_params = {}

        body_params = None

        return self.api_client.call_api(
            "/v1/search/count/aggregate/level/{level}",
            "GET",
            path_params,
            query_params,
            header_params,
            body=body_params,
        )

    def search_location_by_level(self, level, **kwargs):  # noqa: E501
        """Provides the list of regions, or districts based on the input provided by the user.  # noqa: E501

        Provides the list of region, district details based on the value entered by the user. The system displays only the names that start with the entered text. For example: If the user searches for 'xyz', then the search displays only regions starting with 'xyz'.   # noqa: E501
        :param str level: Unique identifier for the level.  (required)
        :param str name: Region name or district name that is used to search.
        """

        all_params = ["level", "name"]  # noqa: E501

        params = locals()
        for key, val in params["kwargs"].items():
            if key not in all_params:
                raise TypeError(
                    "Got an unexpected keyword argument '%s'"
                    " to method search_location_by_level" % key
                )
            params[key] = val
        del params["kwargs"]
        # verify the required parameter 'level' is set
        if "level" not in params or params["level"] is None:
            raise ValueError(
                "Missing the required parameter `level` when calling `search_location_by_level`"
            )  # noqa: E501

        path_params = {}
        if "level" in params:
            path_params["level"] = params["level"]  # noqa: E501

        query_params = []
        if "name" in params:
            query_params.append(("name", params["name"]))  # noqa: E501

        header_params = {}

        body_params = None

        return self.api_client.call_api(
            "/v1/search/location/level/{level}",
            "GET",
            path_params,
            query_params,
            header_params,
            body=body_params,
        )

    def search_location_count_by_level(self, level, **kwargs):  # noqa: E501
        """Lists Region or District based on the input provided by the user.  # noqa: E501

        Lists Region or District based on the input provided by the user.  # noqa: E501
        :param str level: Identifies the level for which information will be provided.  (required)
        :param str name: Name of the region or district that is used to search.
        """

        all_params = ["level", "name"]  # noqa: E501

        params = locals()
        for key, val in params["kwargs"].items():
            if key not in all_params:
                raise TypeError(
                    "Got an unexpected keyword argument '%s'"
                    " to method search_location_count_by_level" % key
                )
            params[key] = val
        del params["kwargs"]
        # verify the required parameter 'level' is set
        if "level" not in params or params["level"] is None:
            raise ValueError(
                "Missing the required parameter `level` when calling `search_location_count_by_level`"
            )  # noqa: E501

        path_params = {}
        if "level" in params:
            path_params["level"] = params["level"]  # noqa: E501

        query_params = []
        if "name" in params:
            query_params.append(("name", params["name"]))  # noqa: E501

        header_params = {}

        body_params = None

        return self.api_client.call_api(
            "/v1/search/count/location/level/{level}",
            "GET",
            path_params,
            query_params,
            header_params,
            body=body_params,
        )

    def search_parent_by_level(self, level, **kwargs):  # noqa: E501
        """Provides the list of NetApp Global Parent(NAGP), or Domestic Parent(DP) based on the input provided by the user.  # noqa: E501

        Provides the list of NAGP, DP details based on the value entered by the user. The system displays only the names that start with the entered text. For example: If the user searches for 'xyz', then the search displays only NAGP starting with 'xyz'.   # noqa: E501
        :param str level: Unique identifier for the level. (required)
        :param str name: The NAGP or DP that is used to search.

        """

        all_params = ["level", "name"]  # noqa: E501

        params = locals()
        for key, val in params["kwargs"].items():
            if key not in all_params:
                raise TypeError(
                    "Got an unexpected keyword argument '%s'"
                    " to method search_parent_by_level" % key
                )
            params[key] = val
        del params["kwargs"]
        # verify the required parameter 'level' is set
        if "level" not in params or params["level"] is None:
            raise ValueError(
                "Missing the required parameter `level` when calling `search_parent_by_level`"
            )  # noqa: E501

        path_params = {}
        if "level" in params:
            path_params["level"] = params["level"]  # noqa: E501

        query_params = []
        if "name" in params:
            query_params.append(("name", params["name"]))  # noqa: E501

        header_params = {}

        body_params = None

        return self.api_client.call_api(
            "/v1/search/parent/level/{level}",
            "GET",
            path_params,
            query_params,
            header_params,
            body=body_params,
        )

    def search_parent_count_by_level(self, level, **kwargs):  # noqa: E501
        """Lists NAGP or DP based on the input provided by the user.  # noqa: E501

        Searches and lists NAGP or DP based on the value provided by the user.  # noqa: E501
        :param str level: Identifies the level for which information will be provided. Valid values are NAGP and Domestic Parent(DP)  (required)
        :param str name: Name of the NAGP or DP that is used to search.
        """

        all_params = ["level", "name"]  # noqa: E501

        params = locals()
        for key, val in params["kwargs"].items():
            if key not in all_params:
                raise TypeError(
                    "Got an unexpected keyword argument '%s'"
                    " to method search_parent_count_by_level" % key
                )
            params[key] = val
        del params["kwargs"]
        # verify the required parameter 'level' is set
        if "level" not in params or params["level"] is None:
            raise ValueError(
                "Missing the required parameter `level` when calling `search_parent_count_by_level`"
            )  # noqa: E501

        path_params = {}
        if "level" in params:
            path_params["level"] = params["level"]  # noqa: E501

        query_params = []
        if "name" in params:
            query_params.append(("name", params["name"]))  # noqa: E501

        header_params = {}

        body_params = None

        return self.api_client.call_api(
            "/v1/search/count/parent/level/{level}",
            "GET",
            path_params,
            query_params,
            header_params,
            body=body_params,
        )

    def search_system_by_level(self, level, **kwargs):  # noqa: E501
        """Provides the system details based on the input provided by the user.  # noqa: E501

        Searches and list system details based on the value provided by the user. The system displays serial number,hostname and system ID of the input that have the specified value in the beginning of the input value. For example: If the user searches for '71141000027' system ID, then the search displays only systems starting with '71141000027'   # noqa: E501
        :param str level: Unique identifier for the level.  (required)
        :param str name: Serial number, hostname, and system ID used to search.
        """

        all_params = ["level", "name"]  # noqa: E501

        params = locals()
        for key, val in params["kwargs"].items():
            if key not in all_params:
                raise TypeError(
                    "Got an unexpected keyword argument '%s'"
                    " to method search_system_by_level" % key
                )
            params[key] = val
        del params["kwargs"]
        # verify the required parameter 'level' is set
        if "level" not in params or params["level"] is None:
            raise ValueError(
                "Missing the required parameter `level` when calling `search_system_by_level`"
            )  # noqa: E501

        path_params = {}
        if "level" in params:
            path_params["level"] = params["level"]  # noqa: E501

        query_params = []
        if "name" in params:
            query_params.append(("name", params["name"]))  # noqa: E501

        header_params = {}

        body_params = None

        return self.api_client.call_api(
            "/v1/search/system/level/{level}",
            "GET",
            path_params,
            query_params,
            header_params,
            body=body_params,
        )

    def search_system_by_level_v2(self, level, **kwargs):  # noqa: E501
        """Provides the system details based on the input provided by the user.  # noqa: E501

        Searches and list system details based on the value provided by the user. The system displays serial number,hostname and system ID of the input that have the specified value in the beginning of the input value. For example: If the user searches for '71141000027' system ID, then the search displays only systems starting with '71141000027'   # noqa: E501
        :param str level: Unique identifier for the level.  (required)
        :param str name: Serial number, hostname, and system ID used to search.
        """

        all_params = ["level", "name"]  # noqa: E501

        params = locals()
        for key, val in params["kwargs"].items():
            if key not in all_params:
                raise TypeError(
                    "Got an unexpected keyword argument '%s'"
                    " to method search_system_by_level_v2" % key
                )
            params[key] = val
        del params["kwargs"]
        # verify the required parameter 'level' is set
        if "level" not in params or params["level"] is None:
            raise ValueError(
                "Missing the required parameter `level` when calling `search_system_by_level_v2`"
            )  # noqa: E501

        path_params = {}
        if "level" in params:
            path_params["level"] = params["level"]  # noqa: E501

        query_params = []
        if "name" in params:
            query_params.append(("name", params["name"]))  # noqa: E501

        header_params = {}

        body_params = None

        return self.api_client.call_api(
            "/v2/search/system/level/{level}",
            "GET",
            path_params,
            query_params,
            header_params,
            body=body_params,
        )

    def search_system_by_level_with_tier(self, level, **kwargs):  # noqa: E501
        """Provides the system details based on the input provided by the user.  # noqa: E501

        Searches and list system details based on the value provided by the user. The system displays serial number,hostname and system ID of the input that have the specified value in the beginning of the input value with service tiering. For example: If the user searches for '71141000027' system ID, then the search displays only systems starting with '71141000027'   # noqa: E501
        :param str level: Unique identifier for the level.  (required)
        :param str platform_type: Unique identifier for the platform type. Multiple platform type can be listed with comma separator.
        :param str service_tier: Unique identifier for the service_tier. config_drift supports AIQADVISOR,AIQEXPERT service tier types. Default is none.
        :param str version: Unique identifier for the ontap version. List the systems which are greater than input version
        :param str name: Serial number, hostname, and system ID used to search.
        """

        all_params = [
            "level",
            "platform_type",
            "service_tier",
            "version",
            "name",
        ]  # noqa: E501

        params = locals()
        for key, val in params["kwargs"].items():
            if key not in all_params:
                raise TypeError(
                    "Got an unexpected keyword argument '%s'"
                    " to method search_system_by_level_with_tier" % key
                )
            params[key] = val
        del params["kwargs"]
        # verify the required parameter 'level' is set
        if "level" not in params or params["level"] is None:
            raise ValueError(
                "Missing the required parameter `level` when calling `search_system_by_level_with_tier`"
            )  # noqa: E501

        path_params = {}

        query_params = []
        if "level" in params:
            query_params.append(("level", params["level"]))  # noqa: E501
        if "platform_type" in params:
            query_params.append(("platformType", params["platform_type"]))  # noqa: E501
        if "service_tier" in params:
            query_params.append(("serviceTier", params["service_tier"]))  # noqa: E501
        if "version" in params:
            query_params.append(("version", params["version"]))  # noqa: E501
        if "name" in params:
            query_params.append(("name", params["name"]))  # noqa: E501

        header_params = {}

        body_params = None

        return self.api_client.call_api(
            "/v1/search/system/tier",
            "GET",
            path_params,
            query_params,
            header_params,
            body=body_params,
        )
