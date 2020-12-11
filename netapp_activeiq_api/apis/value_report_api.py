# coding: utf-8

from .api_client import ApiClient


class ValueReportApi:
    def __init__(self, api_client=None):
        if api_client is None:
            api_client = ApiClient()
        self.api_client = api_client

    def get_value_report_summary_by_level(
        self, level, serialno, **kwargs
    ):  # noqa: E501
        """Provides the aggregated value report details for set of serial numbers.  # noqa: E501

        Total aggregated value report count for set of serial numbers . Counts are provided for the following categories: software upgrades count, performance risk count, autocases count, unique applications count, contract renewal expriy days, storage efficiency savings, configuration risk count, capacity risk count, security risk count, protection risk count, risk checked count, risk mitigated count   # noqa: E501
        :param str level: Identifies the level for which information will be provided. Valid values are customer, site, group, watchlist, cluster or serial_numbers. (required)
        :param str serialno: Valid values with comma separated serial numbers. (required)
        """

        all_params = ["level", "serialno"]  # noqa: E501

        params = locals()
        for key, val in params["kwargs"].items():
            if key not in all_params:
                raise TypeError(
                    "Got an unexpected keyword argument '%s'"
                    " to method get_value_report_summary_by_level" % key
                )
            params[key] = val
        del params["kwargs"]
        # verify the required parameter 'level' is set
        if "level" not in params or params["level"] is None:
            raise ValueError(
                "Missing the required parameter `level` when calling `get_value_report_summary_by_level`"
            )  # noqa: E501
        # verify the required parameter 'serialno' is set
        if "serialno" not in params or params["serialno"] is None:
            raise ValueError(
                "Missing the required parameter `serialno` when calling `get_value_report_summary_by_level`"
            )  # noqa: E501

        path_params = {}
        if "level" in params:
            path_params["level"] = params["level"]  # noqa: E501

        query_params = []
        if "serialno" in params:
            query_params.append(("serialno", params["serialno"]))  # noqa: E501

        header_params = {}

        body_params = None

        return self.api_client.call_api(
            "/v1/value-report/summary/level/{level}",
            "GET",
            path_params,
            query_params,
            header_params,
            body=body_params,
        )

    def get_value_report_summary_by_id(self, level, id, **kwargs):  # noqa: E501
        """Provides the aggregated value report details for a customer, site, group, cluster or serial number.  # noqa: E501

        Total aggregated value report count for a customer, site, group, watchlist, cluster or serial numbers . Counts are provided for the following categories: software upgrades count, performance risk count, autocases count, unique applications count, contract renewal expriy days, storage efficiency savings, configuration risk count, capacity risk count, security risk count, protection risk count, risk checked count, risk mitigated count   # noqa: E501
        :param str level: Identifies the level for which information will be provided. Valid values are customer, site, group, watchlist, cluster or serial_numbers. (required)
        :param str id: Unique identifier for the level. Valid values are customer ID, site ID, watchlist ID, group name, cluster ID or serial numbers. (required)
        """

        all_params = ["level", "id"]  # noqa: E501

        params = locals()
        for key, val in params["kwargs"].items():
            if key not in all_params:
                raise TypeError(
                    "Got an unexpected keyword argument '%s'"
                    " to method get_value_report_summary_by_id" % key
                )
            params[key] = val
        del params["kwargs"]
        # verify the required parameter 'level' is set
        if "level" not in params or params["level"] is None:
            raise ValueError(
                "Missing the required parameter `level` when calling `get_value_report_summary_by_id`"
            )  # noqa: E501
        # verify the required parameter 'id' is set
        if "id" not in params or params["id"] is None:
            raise ValueError(
                "Missing the required parameter `id` when calling `get_value_report_summary_by_id`"
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
            "/v1/value-report/summary/level/{level}/id/{id}",
            "GET",
            path_params,
            query_params,
            header_params,
            body=body_params,
        )
