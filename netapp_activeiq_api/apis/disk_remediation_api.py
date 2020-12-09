# coding: utf-8
from .api_client import ApiClient


class DiskRemediationApi:
    def __init__(self, api_client=None):
        if api_client is None:
            api_client = ApiClient()
        self.api_client = api_client

    def get_firmware_count_api(
        self, context, search_id, search_type, **kwargs
    ):  # noqa: E501
        """Returns the ONTAP system count and details for disk/shelf/sp firmware upgrades.  # noqa: E501

        Returns the ONTAP system count and details for disk/shelf/sp firmware upgrades.   # noqa: E501
        :param str context: Specifies the required context_level field. (required)
        :param str search_id: Specifies the required search parameter for that context. (required)
        :param str search_type: Specifies the type of the mitigation action to capture the cluster management LIFs. (required)
        """

        all_params = ["context", "search_id", "search_type"]  # noqa: E501

        params = locals()
        for key, val in params["kwargs"].items():
            if key not in all_params:
                raise TypeError(
                    "Got an unexpected keyword argument '%s'"
                    " to method get_firmware_count_api" % key
                )
            params[key] = val
        del params["kwargs"]
        # verify the required parameter 'context' is set
        if "context" not in params or params["context"] is None:
            raise ValueError(
                "Missing the required parameter `context` when calling `get_firmware_count_api`"
            )  # noqa: E501
        # verify the required parameter 'search_id' is set
        if "search_id" not in params or params["search_id"] is None:
            raise ValueError(
                "Missing the required parameter `search_id` when calling `get_firmware_count_api`"
            )  # noqa: E501
        # verify the required parameter 'search_type' is set
        if "search_type" not in params or params["search_type"] is None:
            raise ValueError(
                "Missing the required parameter `search_type` when calling `get_firmware_count_api`"
            )  # noqa: E501

        path_params = {}
        if "context" in params:
            path_params["context"] = params["context"]  # noqa: E501
        if "search_id" in params:
            path_params["search_id"] = params["search_id"]  # noqa: E501
        if "search_type" in params:
            path_params["search_type"] = params["search_type"]  # noqa: E501

        query_params = []

        header_params = {}

        body_params = None

        return self.api_client.call_api(
            "/v1/disk-rem/fw-sys-count/{context}/{search_id}/type/{search_type}",
            "GET",
            path_params,
            query_params,
            header_params,
            body=body_params,
        )

    def get_firmware_details_api(
        self, context, search_id, search_type, **kwargs
    ):  # noqa: E501
        """Returns the MySupport URLs and URL count for firmware upgrade files.  # noqa: E501

        Returns the MySupport URLs and URL count for firmware upgrade files.   # noqa: E501
        :param str context: Specifies the required context_level field. (required)
        :param str search_id: Specifies the required search parameter for that context. (required)
        :param str search_type: Specifies the type of the mitigation action to capture the cluster management LIFs. (required)
        """

        all_params = ["context", "search_id", "search_type"]  # noqa: E501

        params = locals()
        for key, val in params["kwargs"].items():
            if key not in all_params:
                raise TypeError(
                    "Got an unexpected keyword argument '%s'"
                    " to method get_firmware_details_api" % key
                )
            params[key] = val
        del params["kwargs"]
        # verify the required parameter 'context' is set
        if "context" not in params or params["context"] is None:
            raise ValueError(
                "Missing the required parameter `context` when calling `get_firmware_details_api`"
            )  # noqa: E501
        # verify the required parameter 'search_id' is set
        if "search_id" not in params or params["search_id"] is None:
            raise ValueError(
                "Missing the required parameter `search_id` when calling `get_firmware_details_api`"
            )  # noqa: E501
        # verify the required parameter 'search_type' is set
        if "search_type" not in params or params["search_type"] is None:
            raise ValueError(
                "Missing the required parameter `search_type` when calling `get_firmware_details_api`"
            )  # noqa: E501

        path_params = {}
        if "context" in params:
            path_params["context"] = params["context"]  # noqa: E501
        if "search_id" in params:
            path_params["search_id"] = params["search_id"]  # noqa: E501
        if "search_type" in params:
            path_params["search_type"] = params["search_type"]  # noqa: E501

        query_params = []

        header_params = {}

        body_params = None

        return self.api_client.call_api(
            "/v1/disk-rem/fw-file-details/{context}/{search_id}/type/{search_type}",
            "GET",
            path_params,
            query_params,
            header_params,
            body=body_params,
        )

    def get_firmware_details_risk_api(
        self, context, search_id, burt_id, search_type, **kwargs
    ):  # noqa: E501
        """Returns the MySupport URLs and URL count for firmware upgrade files at burt level.  # noqa: E501

        Returns the MySupport URLs and URL count for firmware upgrade files at burt level.   # noqa: E501
        :param str context: Specifies the required context_level field. (required)
        :param str search_id: Specifies the required search parameter for that context. (required)
        :param str burt_id: Specifies the burt_id which to filter the API responses on. (required)
        :param str search_type: Specifies the type of the mitigation action to capture the cluster management LIFs. (required)
        """

        all_params = ["context", "search_id", "burt_id", "search_type"]  # noqa: E501

        params = locals()
        for key, val in params["kwargs"].items():
            if key not in all_params:
                raise TypeError(
                    "Got an unexpected keyword argument '%s'"
                    " to method get_firmware_details_risk_api" % key
                )
            params[key] = val
        del params["kwargs"]
        # verify the required parameter 'context' is set
        if "context" not in params or params["context"] is None:
            raise ValueError(
                "Missing the required parameter `context` when calling `get_firmware_details_risk_api`"
            )  # noqa: E501
        # verify the required parameter 'search_id' is set
        if "search_id" not in params or params["search_id"] is None:
            raise ValueError(
                "Missing the required parameter `search_id` when calling `get_firmware_details_risk_api`"
            )  # noqa: E501
        # verify the required parameter 'burt_id' is set
        if "burt_id" not in params or params["burt_id"] is None:
            raise ValueError(
                "Missing the required parameter `burt_id` when calling `get_firmware_details_risk_api`"
            )  # noqa: E501
        # verify the required parameter 'search_type' is set
        if "search_type" not in params or params["search_type"] is None:
            raise ValueError(
                "Missing the required parameter `search_type` when calling `get_firmware_details_risk_api`"
            )  # noqa: E501

        path_params = {}
        if "context" in params:
            path_params["context"] = params["context"]  # noqa: E501
        if "search_id" in params:
            path_params["search_id"] = params["search_id"]  # noqa: E501
        if "burt_id" in params:
            path_params["burt_id"] = params["burt_id"]  # noqa: E501
        if "search_type" in params:
            path_params["search_type"] = params["search_type"]  # noqa: E501

        query_params = []

        header_params = {}

        body_params = None

        return self.api_client.call_api(
            "/v1/disk-rem/fw-file-details/{context}/{search_id}/burtid/{burt_id}/type/{search_type}",
            "GET",
            path_params,
            query_params,
            header_params,
            body=body_params,
        )

    def get_inventory_api(
        self, context, search_id, search_type, **kwargs
    ):  # noqa: E501
        """Provides inventory and playbook zip file to remediate disk/shelf/sp firmware risks.  # noqa: E501

        Returns the zip file containing inventory and playbook files for ONTAP Firmware Upgrades.   # noqa: E501
        :param str context: Specifies the required context_level field. (required)
        :param str search_id: Specifies the required search parameter for that context. (required)
        :param str search_type: Specifies the type of the mitigation action to capture the cluster management LIFs. (required)
        """

        all_params = ["context", "search_id", "search_type"]  # noqa: E501

        params = locals()
        for key, val in params["kwargs"].items():
            if key not in all_params:
                raise TypeError(
                    "Got an unexpected keyword argument '%s'"
                    " to method get_inventory_api" % key
                )
            params[key] = val
        del params["kwargs"]
        # verify the required parameter 'context' is set
        if "context" not in params or params["context"] is None:
            raise ValueError(
                "Missing the required parameter `context` when calling `get_inventory_api`"
            )  # noqa: E501
        # verify the required parameter 'search_id' is set
        if "search_id" not in params or params["search_id"] is None:
            raise ValueError(
                "Missing the required parameter `search_id` when calling `get_inventory_api`"
            )  # noqa: E501
        # verify the required parameter 'search_type' is set
        if "search_type" not in params or params["search_type"] is None:
            raise ValueError(
                "Missing the required parameter `search_type` when calling `get_inventory_api`"
            )  # noqa: E501

        path_params = {}
        if "context" in params:
            path_params["context"] = params["context"]  # noqa: E501
        if "search_id" in params:
            path_params["search_id"] = params["search_id"]  # noqa: E501
        if "search_type" in params:
            path_params["search_type"] = params["search_type"]  # noqa: E501

        query_params = []

        header_params = {}

        body_params = None

        return self.api_client.call_api(
            "/v1/disk-rem/inventory/{context}/{search_id}/type/{search_type}",
            "GET",
            path_params,
            query_params,
            header_params,
            body=body_params,
        )

    def get_inventory_post_api(self, request_body, **kwargs):  # noqa: E501
        """Provides inventory and playbook zip file from a pre-defined inventory output.  # noqa: E501

        Returns the zip file containing inventory and playbook files for ONTAP Firmware Upgrades.   # noqa: E501

        :param object request_body: (required)
        """

        all_params = ["request_body"]  # noqa: E501

        params = locals()
        for key, val in params["kwargs"].items():
            if key not in all_params:
                raise TypeError(
                    "Got an unexpected keyword argument '%s'"
                    " to method get_inventory_post_api" % key
                )
            params[key] = val
        del params["kwargs"]
        # verify the required parameter 'request_body' is set
        if "request_body" not in params or params["request_body"] is None:
            raise ValueError(
                "Missing the required parameter `request_body` when calling `get_inventory_post_api`"
            )  # noqa: E501

        path_params = {}

        query_params = []

        header_params = {}

        body_params = None
        if "request_body" in params:
            body_params = params["request_body"]

        # Authentication setting
        auth_settings = ["SsoServiceOrApiKey"]  # noqa: E501

        return self.api_client.call_api(
            "/v1/disk-rem/inventory/",
            "POST",
            path_params,
            query_params,
            header_params,
            body=body_params,
        )

    def get_inventory_risk_api(
        self, context, search_id, burt_id, search_type, **kwargs
    ):  # noqa: E501
        """Provides inventory and playbook zip file to remediate disk/shelf/sp firmware risks at burt level.  # noqa: E501

        Returns the zip file containing inventory and playbook files for ONTAP Firmware Upgrades.   # noqa: E501
        :param str context: Specifies the required context_level field. (required)
        :param str search_id: Specifies the required search parameter for that context. (required)
        :param str burt_id: Specifies the burt_id which to filter the API responses on. (required)
        :param str search_type: Specifies the type of the mitigation action to capture the cluster management LIFs. (required)
        """

        all_params = ["context", "search_id", "burt_id", "search_type"]  # noqa: E501

        params = locals()
        for key, val in params["kwargs"].items():
            if key not in all_params:
                raise TypeError(
                    "Got an unexpected keyword argument '%s'"
                    " to method get_inventory_risk_api" % key
                )
            params[key] = val
        del params["kwargs"]
        # verify the required parameter 'context' is set
        if "context" not in params or params["context"] is None:
            raise ValueError(
                "Missing the required parameter `context` when calling `get_inventory_risk_api`"
            )  # noqa: E501
        # verify the required parameter 'search_id' is set
        if "search_id" not in params or params["search_id"] is None:
            raise ValueError(
                "Missing the required parameter `search_id` when calling `get_inventory_risk_api`"
            )  # noqa: E501
        # verify the required parameter 'burt_id' is set
        if "burt_id" not in params or params["burt_id"] is None:
            raise ValueError(
                "Missing the required parameter `burt_id` when calling `get_inventory_risk_api`"
            )  # noqa: E501
        # verify the required parameter 'search_type' is set
        if "search_type" not in params or params["search_type"] is None:
            raise ValueError(
                "Missing the required parameter `search_type` when calling `get_inventory_risk_api`"
            )  # noqa: E501

        path_params = {}
        if "context" in params:
            path_params["context"] = params["context"]  # noqa: E501
        if "search_id" in params:
            path_params["search_id"] = params["search_id"]  # noqa: E501
        if "burt_id" in params:
            path_params["burt_id"] = params["burt_id"]  # noqa: E501
        if "search_type" in params:
            path_params["search_type"] = params["search_type"]  # noqa: E501

        query_params = []

        header_params = {}

        body_params = None

        return self.api_client.call_api(
            "/v1/disk-rem/inventory/{context}/{search_id}/burtid/{burt_id}/type/{search_type}",
            "GET",
            path_params,
            query_params,
            header_params,
            body=body_params,
        )

    def get_playbook_api(self, search_type, **kwargs):  # noqa: E501
        """Provides playbook files for disk/shelf/SP firmware upgrades  # noqa: E501

        Returns playbook YAML file for ONTAP Firmware Upgrades.   # noqa: E501
        :param str search_type: Specifies the type of Firmware Upgrade (required)
        """

        all_params = ["search_type"]  # noqa: E501

        params = locals()
        for key, val in params["kwargs"].items():
            if key not in all_params:
                raise TypeError(
                    "Got an unexpected keyword argument '%s'"
                    " to method get_playbook_api" % key
                )
            params[key] = val
        del params["kwargs"]
        # verify the required parameter 'search_type' is set
        if "search_type" not in params or params["search_type"] is None:
            raise ValueError(
                "Missing the required parameter `search_type` when calling `get_playbook_api`"
            )  # noqa: E501

        path_params = {}
        if "search_type" in params:
            path_params["search_type"] = params["search_type"]  # noqa: E501

        query_params = []

        header_params = {}

        body_params = None

        return self.api_client.call_api(
            "/v1/disk-rem/playbook/type/{search_type}",
            "GET",
            path_params,
            query_params,
            header_params,
            body=body_params,
        )
