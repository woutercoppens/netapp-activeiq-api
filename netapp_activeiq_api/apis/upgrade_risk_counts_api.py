# coding: utf-8


from .api_client import ApiClient


class UpgradeRiskCountsApi:
    def __init__(self, api_client=None):
        if api_client is None:
            api_client = ApiClient()
        self.api_client = api_client

    def upgrade_risk_counts(self, level, id, **kwargs):  # noqa: E501
        """Provide risks count.  # noqa: E501

        Provides all issue fixed count (risk count).   # noqa: E501
        :param str level: customer, site, group, cluster, watchlist, or serial_numbers that is used for search. (required)
        :param str id: (required)
        """

        all_params = ["level", "id"]  # noqa: E501

        params = locals()
        for key, val in params["kwargs"].items():
            if key not in all_params:
                raise TypeError(
                    "Got an unexpected keyword argument '%s'"
                    " to method upgrade_risk_counts" % key
                )
            params[key] = val
        del params["kwargs"]
        # verify the required parameter 'level' is set
        if "level" not in params or params["level"] is None:
            raise ValueError(
                "Missing the required parameter `level` when calling `upgrade_risk_counts`"
            )  # noqa: E501
        # verify the required parameter 'id' is set
        if "id" not in params or params["id"] is None:
            raise ValueError(
                "Missing the required parameter `id` when calling `upgrade_risk_counts`"
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
            "/v1/upgrades/riskcount/level/{level}/id/{id}",
            "GET",
            path_params,
            query_params,
            header_params,
            body=body_params,
        )
