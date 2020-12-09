# coding: utf-8

from .api_client import ApiClient


class StorageEfficiencyApi:
    def __init__(self, api_client=None):
        if api_client is None:
            api_client = ApiClient()
        self.api_client = api_client

    def se_details(self, source, id, level, **kwargs):  # noqa: E501
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
                "Missing the required parameter `source` when calling `se_details`"
            )  # noqa: E501
        # verify the required parameter 'id' is set
        if "id" not in params or params["id"] is None:
            raise ValueError(
                "Missing the required parameter `id` when calling `se_details`"
            )  # noqa: E501
        # verify the required parameter 'level' is set
        if "level" not in params or params["level"] is None:
            raise ValueError(
                "Missing the required parameter `level` when calling `se_details`"
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
