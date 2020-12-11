# coding: utf-8
from .api_client import ApiClient


class HealthApi:
    def __init__(self, api_client=None):
        if api_client is None:
            api_client = ApiClient()
        self.api_client = api_client

    def get_health_details_by_level(self, id, level, **kwargs):  # noqa: E501
        """Provides details about the risks for a customer, site, group, or a set of serial numbers  # noqa: E501

        Provides details about the health of the systems for a customer, site, group, or a set of serial numbers. It also provides information about the recommendations and steps to mitigate risks to improve your risk profile. The results are provided in a paginated manner.   # noqa: E501
        :param str id: Unique identifier for the level. Valid values are customer ID, site ID, group name, and serial numbers. (required)
        :param str level: Identifies the level for which information will be provided. Valid values are customer, site, group, and serial_numbers.  (required)
        :param float start: Specifies the number of the first system displayed on the page.
        :param float limit: Specifies the number of systems to be displayed on a page. The default limit is 1000.
        """

        all_params = ["id", "level", "start", "limit"]  # noqa: E501

        params = locals()
        for key, val in params["kwargs"].items():
            if key not in all_params:
                raise TypeError(
                    "Got an unexpected keyword argument '%s'"
                    " to method get_health_details_by_level" % key
                )
            params[key] = val
        del params["kwargs"]
        # verify the required parameter 'id' is set
        if "id" not in params or params["id"] is None:
            raise ValueError(
                "Missing the required parameter `id` when calling `get_health_details_by_level`"
            )  # noqa: E501
        # verify the required parameter 'level' is set
        if "level" not in params or params["level"] is None:
            raise ValueError(
                "Missing the required parameter `level` when calling `get_health_details_by_level`"
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
            "/v1/health/details/level/{level}/id/{id}",
            "GET",
            path_params,
            query_params,
            header_params,
            body=body_params,
        )

    def risk_instances(self, **kwargs):  # noqa: E501
        """Returns information about risk occurrences  # noqa: E501

        Provides details about health risks including information about different occurrences for a set of systems identified by serial numbers, cluster ID, customer ID, site ID, or group name. Exactly one of the following parameters must be specified in the request: customer, site, group, cluster, or serialNumbers. Please note that the API only pulls risk instance data that has a startDate of at most 30 days prior.   # noqa: E501

        :param float customer: Customer ID for which data is to be returned.
        :param float site: Site ID for which data is to be returned.
        :param str group: Name of the group for which data is to be returned.
        :param str cluster: Cluster ID for which data is to be returned.
        :param str serial_numbers: Comma-separated list of serial numbers for which data is to be returned.
        :param str risk_status: Comma-separated list of risk status for which data is to be returned. The default is to return risks with any status.
        :param float start: Specifies the index of the first risk to be returned.
        :param float limit: Specifies the maximum number of risks to be returned in a response. The default limit is 1000.
        """

        all_params = [
            "customer",
            "site",
            "group",
            "cluster",
            "serial_numbers",
            "risk_status",
            "start",
            "limit",
        ]  # noqa: E501

        params = locals()
        for key, val in params["kwargs"].items():
            if key not in all_params:
                raise TypeError(
                    "Got an unexpected keyword argument '%s'"
                    " to method risk_instances" % key
                )
            params[key] = val
        del params["kwargs"]
        # verify the required parameter 'authorization_token' is set

        path_params = {}

        query_params = []
        if "customer" in params:
            query_params.append(("customer", params["customer"]))  # noqa: E501
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
        if "risk_status" in params:
            query_params.append(("riskStatus", params["risk_status"]))  # noqa: E501
        if "start" in params:
            query_params.append(("start", params["start"]))  # noqa: E501
        if "limit" in params:
            query_params.append(("limit", params["limit"]))  # noqa: E501

        header_params = {}

        body_params = None

        return self.api_client.call_api(
            "/v2/health/risks",
            "GET",
            path_params,
            query_params,
            header_params,
            body=body_params,
        )

    def get_health_summary_by_level(self, id, level, **kwargs):  # noqa: E501
        """Provides the number of risks for a customer, site, group, or a set of serial numbers.  # noqa: E501

        Provides the number of risks for each severity level (high, medium, and low) for a customer, site, group, or a set of serial numbers.   # noqa: E501
        :param str id: Unique identifier for the level. Valid values are customer ID, site ID, group name, and serial numbers. (required)
        :param str level: Identifies the level for which information will be provided. Valid values are customer, site, group, and serial_numbers.  (required)
        """

        all_params = ["id", "level"]  # noqa: E501

        params = locals()
        for key, val in params["kwargs"].items():
            if key not in all_params:
                raise TypeError(
                    "Got an unexpected keyword argument '%s'"
                    " to method get_health_summary_by_level" % key
                )
            params[key] = val
        del params["kwargs"]
        # verify the required parameter 'id' is set
        if "id" not in params or params["id"] is None:
            raise ValueError(
                "Missing the required parameter `id` when calling `get_health_summary_by_level`"
            )  # noqa: E501
        # verify the required parameter 'level' is set
        if "level" not in params or params["level"] is None:
            raise ValueError(
                "Missing the required parameter `level` when calling `get_health_summary_by_level`"
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
            "/v1/health/summary/level/{level}/id/{id}",
            "GET",
            path_params,
            query_params,
            header_params,
            body=body_params,
        )
