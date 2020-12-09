# coding: utf-8

from .api_client import ApiClient


class InteropSummaryCountApi:
    def __init__(self, api_client=None):
        if api_client is None:
            api_client = ApiClient()
        self.api_client = api_client

    def interop_summary_count(self, level, id, **kwargs):  # noqa: E501
        """Provides supported, unsupported, remediation available count of a given ONTAP  # noqa: E501

        This API returns the count of configurations for a given customer aggregate that are supported by NetApp. It also returns summary count of configurations unsuppotred or that can be remediated.   # noqa: E501
        :param str level: Required. Value should be one of customer, partner or internal user (required)
        :param str id: Required. Value should be ID of the customer, partner or internal user (required)
        """

        all_params = ["level", "id"]  # noqa: E501

        params = locals()
        for key, val in params["kwargs"].items():
            if key not in all_params:
                raise TypeError(
                    "Got an unexpected keyword argument '%s'"
                    " to method interop_summary_count" % key
                )
            params[key] = val
        del params["kwargs"]
        # verify the required parameter 'level' is set
        if "level" not in params or params["level"] is None:
            raise ValueError(
                "Missing the required parameter `level` when calling `interop_summary_count`"
            )  # noqa: E501
        # verify the required parameter 'id' is set
        if "id" not in params or params["id"] is None:
            raise ValueError(
                "Missing the required parameter `id` when calling `interop_summary_count`"
            )  # noqa: E501

        path_params = {}
        if "level" in params:
            path_params["level"] = params["level"]  # noqa: E501
        if "id" in params:
            path_params["id"] = params["id"]  # noqa: E501

        query_params = []

        header_params = {}

        body_params = None

        return self.api_client.call_api(
            "/v1/interop-advisor/summary-count/{level}/{id}",
            "GET",
            path_params,
            query_params,
            header_params,
            body=body_params,
        )
