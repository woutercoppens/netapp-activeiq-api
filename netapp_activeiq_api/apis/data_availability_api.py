# coding: utf-8

from .api_client import ApiClient


class DataAvailabilityApi:
    def __init__(self, api_client=None):
        if api_client is None:
            api_client = ApiClient()
        self.api_client = api_client

    def data_availability(self, level, id, **kwargs):  # noqa: E501
        """Provides OC availability and InteropAdvisor URL for the given customer, site, group, node or cluster  # noqa: E501

        This API checks availibility of OC ASUPs. If available, returns the InteropAdvisor URL for given customer, site, group, cluster or node   # noqa: E501
        :param str level: Required. Value should be one of customer | site | group | system | cluster (required)
        :param str id: Required. Value should be ID of the customer or site or group or system or cluster (required)
        """

        all_params = ["level", "id"]  # noqa: E501

        params = locals()
        for key, val in params["kwargs"].items():
            if key not in all_params:
                raise TypeError(
                    "Got an unexpected keyword argument '%s'"
                    " to method data_availability" % key
                )
            params[key] = val
        del params["kwargs"]
        # verify the required parameter 'level' is set
        if "level" not in params or params["level"] is None:
            raise ValueError(
                "Missing the required parameter `level` when calling `data_availability`"
            )  # noqa: E501
        # verify the required parameter 'id' is set
        if "id" not in params or params["id"] is None:
            raise ValueError(
                "Missing the required parameter `id` when calling `data_availability`"
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
            "/v1/interop-advisor/data-availability/{level}/{id}",
            "GET",
            path_params,
            query_params,
            header_params,
            body=body_params,
        )
