# coding: utf-8


from .api_client import ApiClient


class SupportCasesApi:
    def __init__(self, api_client=None):
        if api_client is None:
            api_client = ApiClient()
        self.api_client = api_client

    def v1_support_cases_level_id_get(self, level, id, **kwargs):  # noqa: E501
        """Provides the information about open support cases for a customer, site, group or set of serial_numbers.  # noqa: E501

        This API returns key parameters related to each active support case. Requested data set can be for a customer, site, group, or set of serial numbers. Please note that the data received through this interface may lag up to 24 hours from the source application for Support Cases.   # noqa: E501
        :param str level: Identifies the level for which information will be provided. Valid values are customer, site, group, and serial_numbers.  (required)
        :param str id: Unique identifier for the level. Valid values are customer ID, site ID, group name, and serial numbers. (required)
        :param float start: Specifies the number of the first result returned.
        :param float limit: Specifies the maximum number of results to be returned at a time. Defaults to 1000.
        """

        all_params = ["level", "id", "start", "limit"]  # noqa: E501

        params = locals()
        for key, val in params["kwargs"].items():
            if key not in all_params:
                raise TypeError(
                    "Got an unexpected keyword argument '%s'"
                    " to method v1_support_cases_level_id_get" % key
                )
            params[key] = val
        del params["kwargs"]
        # verify the required parameter 'level' is set
        if "level" not in params or params["level"] is None:
            raise ValueError(
                "Missing the required parameter `level` when calling `v1_support_cases_level_id_get`"
            )  # noqa: E501
        # verify the required parameter 'id' is set
        if "id" not in params or params["id"] is None:
            raise ValueError(
                "Missing the required parameter `id` when calling `v1_support_cases_level_id_get`"
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
            "/v1/support/cases/{level}/{id}",
            "GET",
            path_params,
            query_params,
            header_params,
            body=body_params,
        )

    def v1_support_rma_level_id_get(self, level, id, **kwargs):  # noqa: E501
        """Provides information about RMA cases for a customer, site, group, or set of serial_numbers.  # noqa: E501

        Provides information about RMA cases for a customer, site, group, or set of serial_numbers.   # noqa: E501
        :param str level: Identifies the level for which information will be provided. Valid values are customer, site, group, and serial_numbers.  (required)
        :param str id: Unique identifier for the level. Valid values are customer ID, site ID, group name, and serial numbers. (required)
        :param float start: Specifies the number of the first result returned.
        :param float limit: Specifies the maximum number of results to be returned at a time. Defaults to 1000.
        """

        all_params = ["level", "id", "start", "limit"]  # noqa: E501

        params = locals()
        for key, val in params["kwargs"].items():
            if key not in all_params:
                raise TypeError(
                    "Got an unexpected keyword argument '%s'"
                    " to method v1_support_rma_level_id_get" % key
                )
            params[key] = val
        del params["kwargs"]
        # verify the required parameter 'level' is set
        if "level" not in params or params["level"] is None:
            raise ValueError(
                "Missing the required parameter `level` when calling `v1_support_rma_level_id_get`"
            )  # noqa: E501
        # verify the required parameter 'id' is set
        if "id" not in params or params["id"] is None:
            raise ValueError(
                "Missing the required parameter `id` when calling `v1_support_rma_level_id_get`"
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
            "/v1/support/rma/{level}/{id}",
            "GET",
            path_params,
            query_params,
            header_params,
            body=body_params,
        )
