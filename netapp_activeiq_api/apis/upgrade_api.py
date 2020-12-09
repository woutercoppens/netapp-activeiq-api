# coding: utf-8

from .api_client import ApiClient


class UpgradeApi:
    def __init__(self, api_client=None):
        if api_client is None:
            api_client = ApiClient()
        self.api_client = api_client

    def get_disk_fw_upgrade_details_by_level(self, id, level, **kwargs):  # noqa: E501
        """Provides details about systems where firmware is not up to date and needs to be upgraded for a customer, site, group, or a set of serial numbers.   # noqa: E501

        Provides information about systems that can be upgraded for disk firmware for a customer, site, group, or a set of serial numbers. The results are provided in a paginated manner.   # noqa: E501
        :param str id: Unique identifier for the level. Valid values are customer ID, site ID, group name and serial numbers. (required)
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
                    " to method get_disk_fw_upgrade_details_by_level" % key
                )
            params[key] = val
        del params["kwargs"]
        # verify the required parameter 'id' is set
        if "id" not in params or params["id"] is None:
            raise ValueError(
                "Missing the required parameter `id` when calling `get_disk_fw_upgrade_details_by_level`"
            )  # noqa: E501
        # verify the required parameter 'level' is set
        if "level" not in params or params["level"] is None:
            raise ValueError(
                "Missing the required parameter `level` when calling `get_disk_fw_upgrade_details_by_level`"
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
            "/v1/upgrade/details/level/{level}/id/{id}/category/disk_fw",
            "GET",
            path_params,
            query_params,
            header_params,
            body=body_params,
        )

    def get_firmware_details(self, **kwargs):  # noqa: E501
        """Provides firmware details for nodes, shelves, and drives.  # noqa: E501

        Returns available data regarding firmware versions of storage controllers, compute nodes, shelves, shelf modules, and drives. Requires an input of either customer ID, site ID, group name, or set of serial numbers (choose only one of these types).   # noqa: E501
        :param str customer: Customer ID for which data is to be returned.
        :param float site: Site ID for which data is to be returned.
        :param str group: Name of the group for which data is to be returned.
        :param str serial_numbers: Comma-separated list of serial numbers for which data is to be returned.
        """

        all_params = ["customer", "site", "group", "serial_numbers"]  # noqa: E501

        params = locals()
        for key, val in params["kwargs"].items():
            if key not in all_params:
                raise TypeError(
                    "Got an unexpected keyword argument '%s'"
                    " to method get_firmware_details" % key
                )
            params[key] = val
        del params["kwargs"]

        path_params = {}

        query_params = []
        if "customer" in params:
            query_params.append(("customer", params["customer"]))  # noqa: E501
        if "site" in params:
            query_params.append(("site", params["site"]))  # noqa: E501
        if "group" in params:
            query_params.append(("group", params["group"]))  # noqa: E501
        if "serial_numbers" in params:
            query_params.append(
                ("serialNumbers", params["serial_numbers"])
            )  # noqa: E501

        header_params = {}

        body_params = None

        return self.api_client.call_api(
            "/v1/firmware/details",
            "GET",
            path_params,
            query_params,
            header_params,
            body=body_params,
        )

    def get_mb_fw_upgrade_details_by_level(self, id, level, **kwargs):  # noqa: E501
        """Provides details about systems where firmware is not up to date and needs to be upgraded for a customer, site, group, or a set of serial numbers.   # noqa: E501

        Provides information about systems that can be upgraded for motherboard firmware for a customer, site, group, or a set of serial numbers. The results are provided in a paginated manner.   # noqa: E501
        :param str id: Unique identifier for the level. Valid values are customer ID, site ID, group name and serial numbers. (required)
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
                    " to method get_mb_fw_upgrade_details_by_level" % key
                )
            params[key] = val
        del params["kwargs"]
        # verify the required parameter 'id' is set
        if "id" not in params or params["id"] is None:
            raise ValueError(
                "Missing the required parameter `id` when calling `get_mb_fw_upgrade_details_by_level`"
            )  # noqa: E501
        # verify the required parameter 'level' is set
        if "level" not in params or params["level"] is None:
            raise ValueError(
                "Missing the required parameter `level` when calling `get_mb_fw_upgrade_details_by_level`"
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
            "/v1/upgrade/details/level/{level}/id/{id}/category/mb_fw",
            "GET",
            path_params,
            query_params,
            header_params,
            body=body_params,
        )

    def get_upgrade_details_by_level_v2(self, **kwargs):  # noqa: E501
        """Provides details about the systems where firmware is not up to date and needs to be upgraded for a customer, site, group, or a set of serial numbers.   # noqa: E501

        Lists the information about the systems that can be upgraded for ONTAP version, motherboard firmware, disk firmware, and shelf firmware for a customer, site, group, or a set of serial numbers.   # noqa: E501
        :param str customer: Customer ID for which data is to be returned.
        :param str site: Site ID for which data is to be returned.
        :param str group: Name of the group for which data is to be returned.
        :param str cluster: Cluster ID for which data is to be returned.
        :param str serial_numbers: Comma-separated list of serial numbers for which data is to be returned.
        """

        all_params = [
            "customer",
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
                    " to method get_upgrade_details_by_level_v2" % key
                )
            params[key] = val
        del params["kwargs"]

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

        header_params = {}

        body_params = None

        return self.api_client.call_api(
            "/v2/upgrade/details",
            "GET",
            path_params,
            query_params,
            header_params,
            body=body_params,
        )

    def get_upgrade_summary_by_level(self, id, level, **kwargs):  # noqa: E501
        """Provides the number of systems where firmware is not up to date and needs to be upgraded for a customer, site, group, or a set of serial numbers.   # noqa: E501

        Lists the number of systems that can be upgraded for ONTAP version, motherboard firmware, disk firmware, and shelf firmware, for a customer, site, group, or a set of serial numbers.   # noqa: E501
        :param str id: Unique identifier for the level. Valid values are customer ID, site ID, group name, and serial numbers. (required)
        :param str level: Identifies the level for which information will be provided. Valid values are customer, site, group, and serial_numbers.  (required)
        """

        all_params = ["id", "level"]  # noqa: E501

        params = locals()
        for key, val in params["kwargs"].items():
            if key not in all_params:
                raise TypeError(
                    "Got an unexpected keyword argument '%s'"
                    " to method get_upgrade_summary_by_level" % key
                )
            params[key] = val
        del params["kwargs"]
        # verify the required parameter 'id' is set
        if "id" not in params or params["id"] is None:
            raise ValueError(
                "Missing the required parameter `id` when calling `get_upgrade_summary_by_level`"
            )  # noqa: E501
        # verify the required parameter 'level' is set
        if "level" not in params or params["level"] is None:
            raise ValueError(
                "Missing the required parameter `level` when calling `get_upgrade_summary_by_level`"
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
            "/v1/upgrade/summary/level/{level}/id/{id}",
            "GET",
            path_params,
            query_params,
            header_params,
            body=body_params,
        )
