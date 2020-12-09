# coding: utf-8

from .api_client import ApiClient


class SystemApi:
    def __init__(self, api_client=None):
        if api_client is None:
            api_client = ApiClient()
        self.api_client = api_client

    def get_inventory_details_by_level(self, id, level, **kwargs):  # noqa: E501
        """Provides the configuration of systems, for a customer, site, group,watchlist or a set of serial numbers by pagination.  # noqa: E501

        Provides the configuration of systems, for a customer, site, group, watchlist or a set of serial numbers by pagination.  # noqa: E501
        :param str id: Unique identifier of the level. Valid values are customer ID, site ID, watchlist ID, group name and serial numbers. (required)
        :param str level: Identifies the level for which information will be provided. Valid values are customer, site, group, watchlist and serial_numbers.  (required)
        :param float start: Specifies the number of the first system displayed on the page.
        :param float limit: Specifies the number of systems to be displayed on a page. The default value is 50.
        :param str filter_by_platform: Provides information about the platform type. System details are filtered based on the selected platform type.
        :param str filter_by_subtype: Provides information about the system subtype. System details are filtered based on the selected subtype. For example: aff, flexpod, and others.
        :param str sort_column: Provides information about the column name. System details are sorted based on the selected column.
        :param str sort_order: Provides the name for the sort order for the column. System details are sorted based on the sort order applied on the column.
        """

        all_params = [
            "id",
            "level",
            "start",
            "limit",
            "filter_by_platform",
            "filter_by_subtype",
            "sort_column",
            "sort_order",
        ]  # noqa: E501

        params = locals()
        for key, val in params["kwargs"].items():
            if key not in all_params:
                raise TypeError(
                    "Got an unexpected keyword argument '%s'"
                    " to method get_inventory_details_by_level" % key
                )
            params[key] = val
        del params["kwargs"]
        # verify the required parameter 'id' is set
        if "id" not in params or params["id"] is None:
            raise ValueError(
                "Missing the required parameter `id` when calling `get_inventory_details_by_level`"
            )  # noqa: E501
        # verify the required parameter 'level' is set
        if "level" not in params or params["level"] is None:
            raise ValueError(
                "Missing the required parameter `level` when calling `get_inventory_details_by_level`"
            )  # noqa: E501

        path_params = {}
        if "id" in params:
            path_params["id"] = params["id"]  # noqa: E501
        if "level" in params:
            path_params["level"] = params["level"]  # noqa: E501

        query_params = []
        if "start" in params:
            query_params.append(("start", params["start"]))  # noqa: E501
        if "limit" in params:
            query_params.append(("limit", params["limit"]))  # noqa: E501
        if "filter_by_platform" in params:
            query_params.append(
                ("filterByPlatform", params["filter_by_platform"])
            )  # noqa: E501
        if "filter_by_subtype" in params:
            query_params.append(
                ("filterBySubtype", params["filter_by_subtype"])
            )  # noqa: E501
        if "sort_column" in params:
            query_params.append(("sortColumn", params["sort_column"]))  # noqa: E501
        if "sort_order" in params:
            query_params.append(("sortOrder", params["sort_order"]))  # noqa: E501

        header_params = {}

        body_params = None

        return self.api_client.call_api(
            "/v1/system/inventory/details/level/{level}/id/{id}",
            "GET",
            path_params,
            query_params,
            header_params,
            body=body_params,
        )

    def get_list_by_level(self, level, **kwargs):  # noqa: E501
        """Lists customers, sites, or groups.  # noqa: E501

        Lists customers, sites, or groups.  # noqa: E501
        :param str level: Identifies the level for which information will be provided. Valid values are customer, site, and group.  (required)
        """

        all_params = ["level"]  # noqa: E501

        params = locals()
        for key, val in params["kwargs"].items():
            if key not in all_params:
                raise TypeError(
                    "Got an unexpected keyword argument '%s'"
                    " to method get_list_by_level" % key
                )
            params[key] = val
        del params["kwargs"]
        # verify the required parameter 'level' is set
        if "level" not in params or params["level"] is None:
            raise ValueError(
                "Missing the required parameter `level` when calling `get_list_by_level`"
            )  # noqa: E501

        path_params = {}
        if "level" in params:
            path_params["level"] = params["level"]  # noqa: E501

        query_params = []

        header_params = {}

        body_params = None

        return self.api_client.call_api(
            "/v1/system/list/level/{level}",
            "GET",
            path_params,
            query_params,
            header_params,
            body=body_params,
        )

    def get_system_details_by_level(self, id, level, **kwargs):  # noqa: E501
        """Provides the configuration of systems, for a customer, site, group, or a set of serial numbers by pagination.  # noqa: E501

        Provides the configuration of systems, for a customer, site, group, or a set of serial numbers by pagination.  # noqa: E501
        :param str id: Unique identifier of the level. Valid values are customer ID, site ID, group name and serial numbers. (required)
        :param str level: Identifies the level for which information will be provided. Valid values are customer, site, group, and serial_numbers.  (required)
        :param float start: Specifies the number of the first system displayed on the page.
        :param float limit: Specifies the number of systems to be displayed on a page. The default value is 1000.
        """

        all_params = ["id", "level", "start", "limit"]  # noqa: E501

        params = locals()
        for key, val in params["kwargs"].items():
            if key not in all_params:
                raise TypeError(
                    "Got an unexpected keyword argument '%s'"
                    " to method get_system_details_by_level" % key
                )
            params[key] = val
        del params["kwargs"]
        # verify the required parameter 'id' is set
        if "id" not in params or params["id"] is None:
            raise ValueError(
                "Missing the required parameter `id` when calling `get_system_details_by_level`"
            )  # noqa: E501
        # verify the required parameter 'level' is set
        if "level" not in params or params["level"] is None:
            raise ValueError(
                "Missing the required parameter `level` when calling `get_system_details_by_level`"
            )  # noqa: E501

        path_params = {}
        if "id" in params:
            path_params["id"] = params["id"]  # noqa: E501
        if "level" in params:
            path_params["level"] = params["level"]  # noqa: E501

        query_params = []
        if "start" in params:
            query_params.append(("start", params["start"]))  # noqa: E501
        if "limit" in params:
            query_params.append(("limit", params["limit"]))  # noqa: E501

        header_params = {}

        body_params = None

        return self.api_client.call_api(
            "/v2/system/details/level/{level}/id/{id}",
            "GET",
            path_params,
            query_params,
            header_params,
            body=body_params,
        )

    def search_systems_by_level(self, level, **kwargs):  # noqa: E501
        """Lists customers, sites, or groups based on the input provided by the user.  # noqa: E501

        Searches and lists customers, sites, or groups based on the value provided by the user. The system displays only the names that have the specified value in the beginning of the name. For example: If the user searches for 'xyz' customers, then the search displays only customers starting with 'xyz'.  # noqa: E501
        :param str level: Identifies the level for which information will be provided. Valid values are customer, site, and group.  (required)
        :param str name: Name of the customer, site, or group that is used to search.
        """

        all_params = ["level", "name"]  # noqa: E501

        params = locals()
        for key, val in params["kwargs"].items():
            if key not in all_params:
                raise TypeError(
                    "Got an unexpected keyword argument '%s'"
                    " to method search_systems_by_level" % key
                )
            params[key] = val
        del params["kwargs"]
        # verify the required parameter 'level' is set
        if "level" not in params or params["level"] is None:
            raise ValueError(
                "Missing the required parameter `level` when calling `search_systems_by_level`"
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
            "/v1/system/search/level/{level}",
            "GET",
            path_params,
            query_params,
            header_params,
            body=body_params,
        )

    def get_system_summary_by_level(
        self, id, level, **kwargs
    ):  # noqa: E501
        """Provides the number of products for a customer, site, group, or a set of serial numbers.  # noqa: E501

        Provides the number of ONTAP, E-Series, AltaVault, StorageGrid, SolidFire, other systems, sites, and clusters for a customer, site, group, or a set of serial numbers.  # noqa: E501
        :param str id: Unique identifier for the level. Valid values are customer ID, site ID, group name, and serial numbers. (required)
        :param str level: Identifies the level for which the information will be provided. Valid values are customer, site, group, and serial_numbers.  (required)
        """

        all_params = ["id", "level"]  # noqa: E501

        params = locals()
        for key, val in params["kwargs"].items():
            if key not in all_params:
                raise TypeError(
                    "Got an unexpected keyword argument '%s'"
                    " to method get_system_summary_by_level" % key
                )
            params[key] = val
        del params["kwargs"]
        # verify the required parameter 'id' is set
        if "id" not in params or params["id"] is None:
            raise ValueError(
                "Missing the required parameter `id` when calling `get_system_summary_by_level`"
            )  # noqa: E501
        # verify the required parameter 'level' is set
        if "level" not in params or params["level"] is None:
            raise ValueError(
                "Missing the required parameter `level` when calling `get_system_summary_by_level`"
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
            "/v2/system/summary/level/{level}/id/{id}",
            "GET",
            path_params,
            query_params,
            header_params,
            body=body_params,
        )
