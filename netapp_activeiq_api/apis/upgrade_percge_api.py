# coding: utf-8


from .api_client import ApiClient


class UpgradePercgeApi:
    def __init__(self, api_client=None):
        if api_client is None:
            api_client = ApiClient()
        self.api_client = api_client

    def upgrade_percge(self, sys_version, gte, **kwargs):  # noqa: E501
        """Provides the percentage of ONTAP systems that have been adopted.  # noqa: E501

        Provides percentage of ONTAP systems that have been adopted for a specified version of an operating system, and that version is later than the specified _gte version.   # noqa: E501
        :param str sys_version: Percentage of adoption for this ONTAP version is required. The valid versions are 8x, 9x, and 10x. (required)
        :param str gte: Systems with this ONTAP version and later are considered for calculation. The valid versions are 8x, 9x, and 10x. (required)
        """

        all_params = ["sys_version", "gte"]  # noqa: E501

        params = locals()
        for key, val in params["kwargs"].items():
            if key not in all_params:
                raise TypeError(
                    "Got an unexpected keyword argument '%s'"
                    " to method upgrade_percge" % key
                )
            params[key] = val
        del params["kwargs"]
        # verify the required parameter 'sys_version' is set
        if "sys_version" not in params or params["sys_version"] is None:
            raise ValueError(
                "Missing the required parameter `sys_version` when calling `upgrade_percge`"
            )  # noqa: E501
        # verify the required parameter 'gte' is set
        if "gte" not in params or params["gte"] is None:
            raise ValueError(
                "Missing the required parameter `gte` when calling `upgrade_percge`"
            )  # noqa: E501

        path_params = {}
        if "sys_version" in params:
            path_params["sys_version"] = params["sys_version"]  # noqa: E501
        if "gte" in params:
            path_params["_gte"] = params["gte"]  # noqa: E501

        query_params = []

        header_params = {}

        body_params = None

        return self.api_client.call_api(
            "/v1/upgrades/sys_version_adoption/sys_version/{sys_version}/_gte/{_gte}",
            "GET",
            path_params,
            query_params,
            header_params,
            body=body_params,
        )
