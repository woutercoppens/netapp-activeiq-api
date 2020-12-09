# coding: utf-8


from .api_client import ApiClient


class Upgradev2Api:
    def __init__(self, api_client=None):
        if api_client is None:
            api_client = ApiClient()
        self.api_client = api_client

    def details(self, **kwargs):  # noqa: E501
        """Provides systems details with recommended version.  # noqa: E501

        Provides systems details with recommended version. Exactly one of the following parameters must be specified in the request: customer, site, group, cluster, watchlist or serialNumbers.   # noqa: E501
        :param float customer: Specifies the customer ID for which data should be returned.
        :param str watchlist: The watchlist ID for which data should be returned.
        :param float site: The site ID for which data should be returned.
        :param str group: Specifies the name of the group for which data should be returned.
        :param str cluster: Specifies the cluster ID for which data should be returned.
        :param str serial_numbers: The comma-separated list of serial numbers for which data should be returned.
        :param str os_version: The OSVersion for which data should be returned.
        """

        all_params = [
            "customer",
            "watchlist",
            "site",
            "group",
            "cluster",
            "serial_numbers",
            "os_version",
        ]  # noqa: E501

        params = locals()
        for key, val in params["kwargs"].items():
            if key not in all_params:
                raise TypeError(
                    "Got an unexpected keyword argument '%s'" " to method details" % key
                )
            params[key] = val
        del params["kwargs"]

        path_params = {}

        query_params = []
        if "customer" in params:
            query_params.append(("customer", params["customer"]))  # noqa: E501
        if "watchlist" in params:
            query_params.append(("watchlist", params["watchlist"]))  # noqa: E501
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
        if "os_version" in params:
            query_params.append(("OSVersion", params["os_version"]))  # noqa: E501

        header_params = {}

        body_params = None

        return self.api_client.call_api(
            "/v1/upgrades2/details",
            "GET",
            path_params,
            query_params,
            header_params,
            body=body_params,
        )

    def list_ontap(self, **kwargs):  # noqa: E501
        """Provides list of unique ONTAP version.  # noqa: E501

        Provides list of unique ONTAP version.  # noqa: E501
        """

        all_params = []  # noqa: E501

        params = locals()
        for key, val in params["kwargs"].items():
            if key not in all_params:
                raise TypeError(
                    "Got an unexpected keyword argument '%s'"
                    " to method list_ontap" % key
                )
            params[key] = val
        del params["kwargs"]

        path_params = {}

        query_params = []

        header_params = {}

        body_params = None
        return self.api_client.call_api(
            "/v1/upgrades2/ontapversion",
            "GET",
            path_params,
            query_params,
            header_params,
            body=body_params,
        )

    def ontap_compat(self, request_body, **kwargs):  # noqa: E501
        """Provides list of compatible ONTAP version.  # noqa: E501

        Provides list of compatible ONTAP version.  # noqa: E501
        :param RequestBody1 request_body: (required)
        """

        all_params = ["request_body"]  # noqa: E501

        params = locals()
        for key, val in params["kwargs"].items():
            if key not in all_params:
                raise TypeError(
                    "Got an unexpected keyword argument '%s'"
                    " to method ontap_compat" % key
                )
            params[key] = val
        del params["kwargs"]
        # verify the required parameter 'request_body' is set
        if "request_body" not in params or params["request_body"] is None:
            raise ValueError(
                "Missing the required parameter `request_body` when calling `ontap_compat`"
            )  # noqa: E501

        path_params = {}

        query_params = []

        header_params = {}

        body_params = None
        if "request_body" in params:
            body_params = params["request_body"]

        return self.api_client.call_api(
            "/v1/upgrades2/ontap/compatibility",
            "POST",
            path_params,
            query_params,
            header_params,
            body=body_params,
        )

    def upgrade_counts(self, **kwargs):  # noqa: E501
        """Provides systems count, and upgrades count.  # noqa: E501

        Provides systems count, and upgrades count. Exactly one of the following parameters must be specified in the request: customer, site, group, cluster, watchlist or serialNumbers.   # noqa: E501
        :param float customer: Specifies the customer ID for which data should be returned.
        :param str watchlist: The watchlist ID for which data should be returned.
        :param float site: The site ID for which data should be returned.
        :param str group: Specifies the name of the group for which data should be returned.
        :param str cluster: Specifies the cluster ID for which data should be returned.
        :param str serial_numbers: The comma-separated list of serial numbers for which data should be returned.
        """

        all_params = [
            "customer",
            "watchlist",
            "site",
            "group",
            "cluster",
            "serial_numbers",
        ]  # noqa: E501

        params = locals()
        for key, val in params["kwargs"].items():
            if key not in all_params:
                raise TypeError(
                    "Got an unexpected keyword argument '%s'"
                    " to method upgrade_counts" % key
                )
            params[key] = val
        del params["kwargs"]

        path_params = {}

        query_params = []
        if "customer" in params:
            query_params.append(("customer", params["customer"]))  # noqa: E501
        if "watchlist" in params:
            query_params.append(("watchlist", params["watchlist"]))  # noqa: E501
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

        header_params = {}

        body_params = None

        return self.api_client.call_api(
            "/v1/upgrades2/count",
            "GET",
            path_params,
            query_params,
            header_params,
            body=body_params,
        )

    def v1_upgrades2_advisor_level_level_id_id_ontap_ontap_get(
        self, id, level, ontap, **kwargs
    ):  # noqa: E501
        """Provides the risk summary for a specific ONTAP ID.  # noqa: E501

        Lists the risk summary for a specific customer/site/watchlist ID and for a specific ONTAP ID.  # noqa: E501
        :param str id: Unique identifier of the level. Valid value is customer ID,site ID,group Name,watchlist ID,serial Numbers,cluster ID. (required)
        :param str level: Provides information for the identified level. Valid values are customer,site,group,watchlist,serial_numbers,cluster.  (required)
        :param str ontap: Risk is displayed for the indentified ONTAP ID.  (required)
        """

        all_params = ["id", "level", "ontap"]  # noqa: E501

        params = locals()
        for key, val in params["kwargs"].items():
            if key not in all_params:
                raise TypeError(
                    "Got an unexpected keyword argument '%s'"
                    " to method v1_upgrades2_advisor_level_level_id_id_ontap_ontap_get"
                    % key
                )
            params[key] = val
        del params["kwargs"]
        # verify the required parameter 'id' is set
        if "id" not in params or params["id"] is None:
            raise ValueError(
                "Missing the required parameter `id` when calling `v1_upgrades2_advisor_level_level_id_id_ontap_ontap_get`"
            )  # noqa: E501
        # verify the required parameter 'level' is set
        if "level" not in params or params["level"] is None:
            raise ValueError(
                "Missing the required parameter `level` when calling `v1_upgrades2_advisor_level_level_id_id_ontap_ontap_get`"
            )  # noqa: E501
        # verify the required parameter 'ontap' is set
        if "ontap" not in params or params["ontap"] is None:
            raise ValueError(
                "Missing the required parameter `ontap` when calling `v1_upgrades2_advisor_level_level_id_id_ontap_ontap_get`"
            )  # noqa: E501

        path_params = {}
        if "id" in params:
            path_params["id"] = params["id"]  # noqa: E501
        if "level" in params:
            path_params["level"] = params["level"]  # noqa: E501
        if "ontap" in params:
            path_params["ontap"] = params["ontap"]  # noqa: E501

        query_params = []

        header_params = {}

        body_params = None

        return self.api_client.call_api(
            "/v1/upgrades2/advisor/level/{level}/id/{id}/ontap/{ontap}",
            "GET",
            path_params,
            query_params,
            header_params,
            body=body_params,
        )
