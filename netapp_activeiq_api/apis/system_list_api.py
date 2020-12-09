# coding: utf-8
from .api_client import ApiClient


class SystemListApi:
    def __init__(self, api_client=None):
        if api_client is None:
            api_client = ApiClient()
        self.api_client = api_client

    def get_system_count_partner_by_level(self, id, level, **kwargs):  # noqa: E501
        """Provides the list of systems for a partner.  # noqa: E501

        Provides the list of systems for a partner.  # noqa: E501
        :param str id: Unique identifier of the level. Valid value is partner ID . (required)
        :param str level: Identifies the level for which information will be provided. Valid value is partner.  (required)
        """

        all_params = ["id", "level"]  # noqa: E501

        params = locals()
        for key, val in params["kwargs"].items():
            if key not in all_params:
                raise TypeError(
                    "Got an unexpected keyword argument '%s'"
                    " to method get_system_count_partner_by_level" % key
                )
            params[key] = val
        del params["kwargs"]
        # verify the required parameter 'id' is set
        if "id" not in params or params["id"] is None:
            raise ValueError(
                "Missing the required parameter `id` when calling `get_system_count_partner_by_level`"
            )  # noqa: E501
        # verify the required parameter 'level' is set
        if "level" not in params or params["level"] is None:
            raise ValueError(
                "Missing the required parameter `level` when calling `get_system_count_partner_by_level`"
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
            "/v2/systemList/partnerSystemCount/level/{level}/id/{id}",
            "GET",
            path_params,
            query_params,
            header_params,
            body=body_params,
        )

    def get_system_count_sales_rep_by_level(self, id, level, **kwargs):  # noqa: E501
        """Provides the list of systems for a sales representative.  # noqa: E501

        Provides the list of systems for a sales representative.  # noqa: E501
        :param str id: Unique identifier of the level. Valid value is sales representative ID. (required)
        :param str level: Identifies the level for which information will be provided. Valid value is salesrep.  (required)
        """

        all_params = ["id", "level"]  # noqa: E501

        params = locals()
        for key, val in params["kwargs"].items():
            if key not in all_params:
                raise TypeError(
                    "Got an unexpected keyword argument '%s'"
                    " to method get_system_count_sales_rep_by_level" % key
                )
            params[key] = val
        del params["kwargs"]
        # verify the required parameter 'id' is set
        if "id" not in params or params["id"] is None:
            raise ValueError(
                "Missing the required parameter `id` when calling `get_system_count_sales_rep_by_level`"
            )  # noqa: E501
        # verify the required parameter 'level' is set
        if "level" not in params or params["level"] is None:
            raise ValueError(
                "Missing the required parameter `level` when calling `get_system_count_sales_rep_by_level`"
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
            "/v2/systemList/salesRepSystemCount/level/{level}/id/{id}",
            "GET",
            path_params,
            query_params,
            header_params,
            body=body_params,
        )

    def get_system_list_aggregate_by_level(self, id, level, **kwargs):  # noqa: E501
        """Provides the list of system for a customer, site, or group by pagination.  # noqa: E501

        Provides the list of system for a customer, site, or group by pagination.  # noqa: E501
        :param str id: Unique identifier of the level. Valid values are customer ID, site ID, or group name. (required)
        :param str level: Identifies the level for which information will be provided. Valid values are customer, site, and group.  (required)
        :param float start: Specifies the number of the first system that is displayed on the page.
        :param float limit: Specifies the number of systems to be displayed on a page. The default value is 1000.
        """

        all_params = ["id", "level", "start", "limit"]  # noqa: E501

        params = locals()
        for key, val in params["kwargs"].items():
            if key not in all_params:
                raise TypeError(
                    "Got an unexpected keyword argument '%s'"
                    " to method get_system_list_aggregate_by_level" % key
                )
            params[key] = val
        del params["kwargs"]
        # verify the required parameter 'id' is set
        if "id" not in params or params["id"] is None:
            raise ValueError(
                "Missing the required parameter `id` when calling `get_system_list_aggregate_by_level`"
            )  # noqa: E501
        # verify the required parameter 'level' is set
        if "level" not in params or params["level"] is None:
            raise ValueError(
                "Missing the required parameter `level` when calling `get_system_list_aggregate_by_level`"
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
            "/v1/systemList/aggregate/level/{level}/id/{id}",
            "GET",
            path_params,
            query_params,
            header_params,
            body=body_params,
        )

    def get_system_list_location_by_level(self, id, level, **kwargs):  # noqa: E501
        """Provides the list of system for a region, or district by pagination.  # noqa: E501

        Provides the list of system for a region, or district by pagination.  # noqa: E501
        :param str id: Unique identifier of the level. Valid values are region name and district name. (required)
        :param str level: Identifies the level for which information will be provided. Valid values are region and district.  (required)
        :param float start: Specifies the number of the first system that is displayed on the page.
        :param float limit: Specifies the number of systems to be displayed on a page. The default value is 1000.
        """

        all_params = ["id", "level", "start", "limit"]  # noqa: E501

        params = locals()
        for key, val in params["kwargs"].items():
            if key not in all_params:
                raise TypeError(
                    "Got an unexpected keyword argument '%s'"
                    " to method get_system_list_location_by_level" % key
                )
            params[key] = val
        del params["kwargs"]
        # verify the required parameter 'id' is set
        if "id" not in params or params["id"] is None:
            raise ValueError(
                "Missing the required parameter `id` when calling `get_system_list_location_by_level`"
            )  # noqa: E501
        # verify the required parameter 'level' is set
        if "level" not in params or params["level"] is None:
            raise ValueError(
                "Missing the required parameter `level` when calling `get_system_list_location_by_level`"
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
            "/v1/systemList/location/level/{level}/id/{id}",
            "GET",
            path_params,
            query_params,
            header_params,
            body=body_params,
        )

    def get_system_list_parent_by_level(self, id, level, **kwargs):  # noqa: E501
        """Provides the list of system for a NetApp Global Parent(NAGP), or Domestic Parent(DP) by pagination.  # noqa: E501

        Provides the list of system for a NetApp Global Parent(NAGP), or Domestic Parent(DP) by pagination.  # noqa: E501
        :param str id: Unique identifier of the level. Valid values are NAGP ID and DP ID. (required)
        :param str level: Identifies the level for which information will be provided. Valid values are global and domestic. (its enum static variable name)  (required)
        :param float start: Specifies the number of the first system that is displayed on the page.
        :param float limit: Specifies the number of systems to be displayed on a page. The default value is 1000.
        """

        all_params = ["id", "level", "start", "limit"]  # noqa: E501

        params = locals()
        for key, val in params["kwargs"].items():
            if key not in all_params:
                raise TypeError(
                    "Got an unexpected keyword argument '%s'"
                    " to method get_system_list_parent_by_level" % key
                )
            params[key] = val
        del params["kwargs"]
        # verify the required parameter 'id' is set
        if "id" not in params or params["id"] is None:
            raise ValueError(
                "Missing the required parameter `id` when calling `get_system_list_parent_by_level`"
            )  # noqa: E501
        # verify the required parameter 'level' is set
        if "level" not in params or params["level"] is None:
            raise ValueError(
                "Missing the required parameter `level` when calling `get_system_list_parent_by_level`"
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
            "/v1/systemList/parent/level/{level}/id/{id}",
            "GET",
            path_params,
            query_params,
            header_params,
            body=body_params,
        )
