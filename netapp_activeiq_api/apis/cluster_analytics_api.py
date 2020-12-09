from .api_client import ApiClient


class ClusterAnalyticsApi:
    def __init__(self, api_client=None):
        if api_client is None:
            api_client = ApiClient()
        self.api_client = api_client

    def get_adapter_interface(self, serial_no, **kwargs):  # noqa: E501
        """Provides Adapter Interface data.  # noqa: E501

        Provides Adapter Interface data.   # noqa: E501

        :param str serial_no: Specifies the required serial number field. (required)
        :param str lang: Value representing a language
        """
        all_params = ["serial_no", "lang"]  # noqa: E501

        params = locals()
        for key, val in params["kwargs"].items():
            if key not in all_params:
                raise TypeError(
                    "Got an unexpected keyword argument '%s'"
                    " to method get_adapter_interface" % key
                )
            params[key] = val
        del params["kwargs"]
        # verify the required parameter 'serial_no' is set
        if "serial_no" not in params or params["serial_no"] is None:
            raise ValueError(
                "Missing the required parameter `serial_no` when calling `get_adapter_interface`"
            )  # noqa: E501

        path_params = {}
        if "serial_no" in params:
            path_params["serial_no"] = params["serial_no"]  # noqa: E501

        query_params = []
        if "lang" in params:
            query_params.append(("lang", params["lang"]))  # noqa: E501

        header_params = {}

        body_params = None

        return self.api_client.call_api(
            "/v1/clusterview/get-adapter-interface/{serial_no}",
            "GET",
            path_params,
            query_params,
            header_params,
            body=body_params,
        )

    def get_aggregate_efficiency(self, serial_no, **kwargs):  # noqa: E501
        """Provides data for the Local Tier Efficiency.  # noqa: E501

        Displays the efficiency data using 'AGGR-EFFICIENCY.XML' section.   # noqa: E501

        :param str serial_no: Specifies the required serial number field. (required)
        :param str lang: Value representing a language
        """

        all_params = ["serial_no", "lang"]  # noqa: E501

        params = locals()
        for key, val in params["kwargs"].items():
            if key not in all_params:
                raise TypeError(
                    "Got an unexpected keyword argument '%s'"
                    " to method get_aggregate_efficiency" % key
                )
            params[key] = val
        del params["kwargs"]
        # verify the required parameter 'serial_no' is set
        if "serial_no" not in params or params["serial_no"] is None:
            raise ValueError(
                "Missing the required parameter `serial_no` when calling `get_aggregate_efficiency`"
            )  # noqa: E501

        path_params = {}
        if "serial_no" in params:
            path_params["serial_no"] = params["serial_no"]  # noqa: E501

        query_params = []
        if "lang" in params:
            query_params.append(("lang", params["lang"]))  # noqa: E501

        header_params = {}

        body_params = None

        return self.api_client.call_api(
            "/v1/clusterview/get-aggregate-efficiency/{serial_no}",
            "GET",
            path_params,
            query_params,
            header_params,
            body=body_params,
        )

    def get_aggregate_summary(self, serial_no, **kwargs):  # noqa: E501
        """Provides data for the Local Tier Summary.  # noqa: E501

        Displays the data for the Local Tier Summary represented in the categories provided below:   Local Tier Name,   Local Tier Type,   RAID Type,   Disk Count,   Data Disk Count,   Usable Capacity (TiB),   Used Capacity (TiB),   Available Capacity (TiB),   Physical Capacity (TiB),   Logical Capacity (TiB),   Used Data Percentage,   Number of RAID Groups,   RAID Group Size,   # noqa: E501
        :param str serial_no: Specifies the required serial number field. (required)
        :param str lang: Value representing a language
        """

        all_params = ["serial_no", "lang"]  # noqa: E501

        params = locals()
        for key, val in params["kwargs"].items():
            if key not in all_params:
                raise TypeError(
                    "Got an unexpected keyword argument '%s'"
                    " to method get_aggregate_summary" % key
                )
            params[key] = val
        del params["kwargs"]
        # verify the required parameter 'serial_no' is set
        if "serial_no" not in params or params["serial_no"] is None:
            raise ValueError(
                "Missing the required parameter `serial_no` when calling `get_aggregate_summary`"
            )  # noqa: E501

        path_params = {}
        if "serial_no" in params:
            path_params["serial_no"] = params["serial_no"]  # noqa: E501

        query_params = []
        if "lang" in params:
            query_params.append(("lang", params["lang"]))  # noqa: E501

        header_params = {}

        body_params = None

        return self.api_client.call_api(
            "/v1/clusterview/get-aggregate-summary/{serial_no}",
            "GET",
            path_params,
            query_params,
            header_params,
            body=body_params,
        )

    def get_cable_visualization(self, serial_no, **kwargs):  # noqa: E501
        """Provides Cable Visualization data.  # noqa: E501

        Cable visualization shows data for controller, shelves, switches and auto bridges and it also shows connection between them. Shelves are grouped into stack.   # noqa: E501
        :param str serial_no: Specifies the required serial number field. (required)
        :param str lang: Value representing a language
        """

        all_params = ["serial_no", "lang"]  # noqa: E501

        params = locals()
        for key, val in params["kwargs"].items():
            if key not in all_params:
                raise TypeError(
                    "Got an unexpected keyword argument '%s'"
                    " to method get_cable_visualization" % key
                )
            params[key] = val
        del params["kwargs"]
        # verify the required parameter 'serial_no' is set
        if "serial_no" not in params or params["serial_no"] is None:
            raise ValueError(
                "Missing the required parameter `serial_no` when calling `get_cable_visualization`"
            )  # noqa: E501

        collection_formats = {}

        path_params = {}
        if "serial_no" in params:
            path_params["serial_no"] = params["serial_no"]  # noqa: E501

        query_params = []
        if "lang" in params:
            query_params.append(("lang", params["lang"]))  # noqa: E501

        header_params = {}

        body_params = None

        return self.api_client.call_api(
            "/v1/clusterview/get-cable-visualization/{serial_no}",
            "GET",
            path_params,
            query_params,
            header_params,
            body=body_params,
        )

    def get_capacity_headroom_details(self, serial_no, **kwargs):  # noqa: E501
        """Provides Capacity Headroom table data.  # noqa: E501

        Provides Capacity Headroom table data.   # noqa: E501
        :param str serial_no: Specifies the required serial number field. (required)
        :param str lang: Value representing a language
        """

        all_params = ["serial_no", "lang"]  # noqa: E501

        params = locals()
        for key, val in params["kwargs"].items():
            if key not in all_params:
                raise TypeError(
                    "Got an unexpected keyword argument '%s'"
                    " to method get_capacity_headroom_details" % key
                )
            params[key] = val
        del params["kwargs"]
        # verify the required parameter 'serial_no' is set
        if "serial_no" not in params or params["serial_no"] is None:
            raise ValueError(
                "Missing the required parameter `serial_no` when calling `get_capacity_headroom_details`"
            )  # noqa: E501

        path_params = {}
        if "serial_no" in params:
            path_params["serial_no"] = params["serial_no"]  # noqa: E501

        query_params = []
        if "lang" in params:
            query_params.append(("lang", params["lang"]))  # noqa: E501

        header_params = {}
        if "authorization_token" in params:
            header_params["authorizationToken"] = params[
                "authorization_token"
            ]  # noqa: E501

        body_params = None

        return self.api_client.call_api(
            "/v1/clusterview/get-capacity-headroom/{serial_no}",
            "GET",
            path_params,
            query_params,
            header_params,
            body=body_params,
        )

    def get_cluster_configuration(self, uuid, **kwargs):  # noqa: E501
        """Provides the cluster IP address, node, and release version data of a specific cluster UUID.  # noqa: E501

        Displays the cluster IP address, node, and release version data of a specific cluster UUID.   # noqa: E501
        :param str uuid: Specifies the required cluster ID or UUID. (required)
        :param str lang: Value representing a language
        """

        all_params = ["uuid", "lang"]  # noqa: E501

        params = locals()
        for key, val in params["kwargs"].items():
            if key not in all_params:
                raise TypeError(
                    "Got an unexpected keyword argument '%s'"
                    " to method get_cluster_configuration" % key
                )
            params[key] = val
        del params["kwargs"]
        # verify the required parameter 'uuid' is set
        if "uuid" not in params or params["uuid"] is None:
            raise ValueError(
                "Missing the required parameter `uuid` when calling `get_cluster_configuration`"
            )  # noqa: E501

        path_params = {}
        if "uuid" in params:
            path_params["uuid"] = params["uuid"]  # noqa: E501

        query_params = []
        if "lang" in params:
            query_params.append(("lang", params["lang"]))  # noqa: E501

        header_params = {}

        body_params = None

        return self.api_client.call_api(
            "/v1/clusterview/get-cluster-configuration/{uuid}",
            "GET",
            path_params,
            query_params,
            header_params,
            body=body_params,
        )

    def get_cluster_summary(self, serial_no, **kwargs):  # noqa: E501
        """Provides the data for the Cluster Summary.  # noqa: E501

        Displays the data for the Cluster Summary represented in the categories provided below:   Cluster Name,   Cluster Management IP Address,   Raw Capacity (TiB),   Usable Capacity (TiB),   Used Capacity (TiB),   Available Capacity (TiB),   Physical Capacity (TiB),   Logical Capacity (TiB),   High-Availability Configured,   Node Storage VMs,   Data Storage VMs,   Local Tiers,   Volumes,   LUNs,   Qtrees,   SnapMirror   # noqa: E501
        :param str serial_no: Specifies the required serial number field. (required)
        :param str lang: Value representing a language
        """

        all_params = ["serial_no", "lang"]  # noqa: E501

        params = locals()
        for key, val in params["kwargs"].items():
            if key not in all_params:
                raise TypeError(
                    "Got an unexpected keyword argument '%s'"
                    " to method get_cluster_summary" % key
                )
            params[key] = val
        del params["kwargs"]
        # verify the required parameter 'serial_no' is set
        if "serial_no" not in params or params["serial_no"] is None:
            raise ValueError(
                "Missing the required parameter `serial_no` when calling `get_cluster_summary`"
            )  # noqa: E501

        path_params = {}
        if "serial_no" in params:
            path_params["serial_no"] = params["serial_no"]  # noqa: E501

        query_params = []
        if "lang" in params:
            query_params.append(("lang", params["lang"]))  # noqa: E501

        header_params = {}

        body_params = None

        return self.api_client.call_api(
            "/v1/clusterview/get-cluster-summary/{serial_no}",
            "GET",
            path_params,
            query_params,
            header_params,
            body=body_params,
        )

    def get_disk_details(self, serial_no, **kwargs):  # noqa: E501
        """Provides Disk Details.  # noqa: E501

        It provides each disk details and raid group details.   # noqa: E501
        :param str serial_no: Specifies the required serial number field. (required)
        :param str lang: Value representing a language
        """

        all_params = ["serial_no", "lang"]  # noqa: E501

        params = locals()
        for key, val in params["kwargs"].items():
            if key not in all_params:
                raise TypeError(
                    "Got an unexpected keyword argument '%s'"
                    " to method get_disk_details" % key
                )
            params[key] = val
        del params["kwargs"]
        # verify the required parameter 'serial_no' is set
        if "serial_no" not in params or params["serial_no"] is None:
            raise ValueError(
                "Missing the required parameter `serial_no` when calling `get_disk_details`"
            )  # noqa: E501

        path_params = {}
        if "serial_no" in params:
            path_params["serial_no"] = params["serial_no"]  # noqa: E501

        query_params = []
        if "lang" in params:
            query_params.append(("lang", params["lang"]))  # noqa: E501

        header_params = {}

        body_params = None

        return self.api_client.call_api(
            "/v1/clusterview/get-disk-details/{serial_no}",
            "GET",
            path_params,
            query_params,
            header_params,
            body=body_params,
        )

    def get_free_slot_details(self, serial_no, **kwargs):  # noqa: E501
        """Provides free slots data.  # noqa: E501

        Provides free slots data.   # noqa: E501
        :param str serial_no: Specifies the required serial number field. (required)
        :param str lang: Value representing a language
        """

        all_params = ["serial_no", "lang"]  # noqa: E501

        params = locals()
        for key, val in params["kwargs"].items():
            if key not in all_params:
                raise TypeError(
                    "Got an unexpected keyword argument '%s'"
                    " to method get_free_slot_details" % key
                )
            params[key] = val
        del params["kwargs"]
        # verify the required parameter 'authorization_token' is set
        if "authorization_token" not in params or params["authorization_token"] is None:
            raise ValueError(
                "Missing the required parameter `authorization_token` when calling `get_free_slot_details`"
            )  # noqa: E501
        # verify the required parameter 'serial_no' is set
        if "serial_no" not in params or params["serial_no"] is None:
            raise ValueError(
                "Missing the required parameter `serial_no` when calling `get_free_slot_details`"
            )  # noqa: E501

        collection_formats = {}

        path_params = {}
        if "serial_no" in params:
            path_params["serial_no"] = params["serial_no"]  # noqa: E501

        query_params = []
        if "lang" in params:
            query_params.append(("lang", params["lang"]))  # noqa: E501

        header_params = {}

        body_params = None

        return self.api_client.call_api(
            "/v1/clusterview/get-free-slot-details/{serial_no}",
            "GET",
            path_params,
            query_params,
            header_params,
            body=body_params,
        )

    def get_max_supported_capacity_details(self, serial_no, **kwargs):  # noqa: E501
        """Provides Max Supported Capacity data.  # noqa: E501

        Provides Max Supported Capacity data.   # noqa: E501
        :param str serial_no: Specifies the required serial number field. (required)
        :param str lang: Value representing a language
        """

        all_params = ["serial_no", "lang"]  # noqa: E501

        params = locals()
        for key, val in params["kwargs"].items():
            if key not in all_params:
                raise TypeError(
                    "Got an unexpected keyword argument '%s'"
                    " to method get_max_supported_capacity_details" % key
                )
            params[key] = val
        del params["kwargs"]
        # verify the required parameter 'serial_no' is set
        if "serial_no" not in params or params["serial_no"] is None:
            raise ValueError(
                "Missing the required parameter `serial_no` when calling `get_max_supported_capacity_details`"
            )  # noqa: E501

        path_params = {}
        if "serial_no" in params:
            path_params["serial_no"] = params["serial_no"]  # noqa: E501

        query_params = []
        if "lang" in params:
            query_params.append(("lang", params["lang"]))  # noqa: E501

        header_params = {}

        body_params = None

        return self.api_client.call_api(
            "/v1/clusterview/get-max-supported-capacity/{serial_no}",
            "GET",
            path_params,
            query_params,
            header_params,
            body=body_params,
        )

    def get_module_overview(self, serial_no, **kwargs):  # noqa: E501
        """Provides data for the Module Overview.  # noqa: E501

        Displays the data for the Module Overview represented in the categories provided below:   Module Type,   Number of Shelf Modules   # noqa: E501
        :param str serial_no: Specifies the required serial number field. (required)
        :param str lang: Value representing a language
        """

        all_params = ["serial_no", "lang"]  # noqa: E501

        params = locals()
        for key, val in params["kwargs"].items():
            if key not in all_params:
                raise TypeError(
                    "Got an unexpected keyword argument '%s'"
                    " to method get_module_overview" % key
                )
            params[key] = val
        del params["kwargs"]
        # verify the required parameter 'serial_no' is set
        if "serial_no" not in params or params["serial_no"] is None:
            raise ValueError(
                "Missing the required parameter `serial_no` when calling `get_module_overview`"
            )  # noqa: E501

        path_params = {}
        if "serial_no" in params:
            path_params["serial_no"] = params["serial_no"]  # noqa: E501

        query_params = []
        if "lang" in params:
            query_params.append(("lang", params["lang"]))  # noqa: E501

        header_params = {}

        body_params = None

        return self.api_client.call_api(
            "/v1/clusterview/get-module-overview/{serial_no}",
            "GET",
            path_params,
            query_params,
            header_params,
            body=body_params,
        )

    def get_network_interfaces(self, serial_no, **kwargs):  # noqa: E501
        """Provides data for the Network Interface.  # noqa: E501

        Displays the data for the Network Interface represented in the categories provided below:   Storage Virtual Machine,   Logical Interface,   Role,   Status(Admin/Operational),   Network Address,   Current Port,   Is Home,   Failover Group Name   # noqa: E501
        :param str serial_no: Specifies the required serial number field. (required)
        :param str lang: Value representing a language
        """

        all_params = ["serial_no", "lang"]  # noqa: E501

        params = locals()
        for key, val in params["kwargs"].items():
            if key not in all_params:
                raise TypeError(
                    "Got an unexpected keyword argument '%s'"
                    " to method get_network_interfaces" % key
                )
            params[key] = val
        del params["kwargs"]
        # verify the required parameter 'serial_no' is set
        if "serial_no" not in params or params["serial_no"] is None:
            raise ValueError(
                "Missing the required parameter `serial_no` when calling `get_network_interfaces`"
            )  # noqa: E501

        path_params = {}
        if "serial_no" in params:
            path_params["serial_no"] = params["serial_no"]  # noqa: E501

        query_params = []
        if "lang" in params:
            query_params.append(("lang", params["lang"]))  # noqa: E501

        header_params = {}

        body_params = None

        return self.api_client.call_api(
            "/v1/clusterview/get-network-interfaces/{serial_no}",
            "GET",
            path_params,
            query_params,
            header_params,
            body=body_params,
        )

    def get_network_ports(self, serial_no, **kwargs):  # noqa: E501
        """Provides data for the Network Ports.  # noqa: E501

        Displays the data for the Network Ports represented in the categories provided below:   Port,   Role,   Link,   Maximum Transmission Unit (MTU),   MAC Address,   Operational Speed,   IPspace Name,   Broadcast Domain,   Interface Group Owner   # noqa: E501
        :param str serial_no: Specifies the required serial number field. (required)
        :param str lang: Value representing a language
        """

        all_params = ["serial_no", "lang"]  # noqa: E501

        params = locals()
        for key, val in params["kwargs"].items():
            if key not in all_params:
                raise TypeError(
                    "Got an unexpected keyword argument '%s'"
                    " to method get_network_ports" % key
                )
            params[key] = val
        del params["kwargs"]
        # verify the required parameter 'serial_no' is set
        if "serial_no" not in params or params["serial_no"] is None:
            raise ValueError(
                "Missing the required parameter `serial_no` when calling `get_network_ports`"
            )  # noqa: E501

        path_params = {}
        if "serial_no" in params:
            path_params["serial_no"] = params["serial_no"]  # noqa: E501

        query_params = []
        if "lang" in params:
            query_params.append(("lang", params["lang"]))  # noqa: E501

        header_params = {}

        body_params = None

        return self.api_client.call_api(
            "/v1/clusterview/get-network-ports/{serial_no}",
            "GET",
            path_params,
            query_params,
            header_params,
            body=body_params,
        )

    def get_node_slot_map(self, serial_no, **kwargs):  # noqa: E501
        """Provides data for the Hardware Slot Map.  # noqa: E501

        Displays the data for the Hardware Slot Map represented in the categories provided below:   Slot Number,   Description,   Part Number,   Serial Number   # noqa: E501
        :param str serial_no: Specifies the required serial number field. (required)
        :param str lang: Value representing a language
        """

        all_params = ["serial_no", "lang"]  # noqa: E501

        params = locals()
        for key, val in params["kwargs"].items():
            if key not in all_params:
                raise TypeError(
                    "Got an unexpected keyword argument '%s'"
                    " to method get_node_slot_map" % key
                )
            params[key] = val
        del params["kwargs"]
        # verify the required parameter 'serial_no' is set
        if "serial_no" not in params or params["serial_no"] is None:
            raise ValueError(
                "Missing the required parameter `serial_no` when calling `get_node_slot_map`"
            )  # noqa: E501

        collection_formats = {}

        path_params = {}
        if "serial_no" in params:
            path_params["serial_no"] = params["serial_no"]  # noqa: E501

        query_params = []
        if "lang" in params:
            query_params.append(("lang", params["lang"]))  # noqa: E501

        header_params = {}

        body_params = None

        return self.api_client.call_api(
            "/v1/clusterview/get-node-slot-map/{serial_no}",
            "GET",
            path_params,
            query_params,
            header_params,
            body=body_params,
        )

    def get_node_summary(self, serial_no, **kwargs):  # noqa: E501
        """Provides data for the Node Summary.  # noqa: E501

        Displays the data for the Node Summary represented in the categories provided below:   Device Type,   System Operating Mode,   Cluster Name,   Hostname,   Serial Number,   System ID,   Release Version,   Model,   Configuration,   IP Address,   High-Availability Partner Hostname,   High-Availability Partner System ID,   Raw Capacity (TiB),   Usable Capacity (TiB),   Used Capacity (TiB),   Available Capacity (TiB),   Physical Capacity (TiB),   Logical Capacity (TiB),   Installed Licenses   # noqa: E501
        :param str serial_no: Specifies the required serial number field. (required)
        :param str lang: Value representing a language
        """

        all_params = ["serial_no", "lang"]  # noqa: E501

        params = locals()
        for key, val in params["kwargs"].items():
            if key not in all_params:
                raise TypeError(
                    "Got an unexpected keyword argument '%s'"
                    " to method get_node_summary" % key
                )
            params[key] = val
        del params["kwargs"]
        # verify the required parameter 'serial_no' is set
        if "serial_no" not in params or params["serial_no"] is None:
            raise ValueError(
                "Missing the required parameter `serial_no` when calling `get_node_summary`"
            )  # noqa: E501

        path_params = {}
        if "serial_no" in params:
            path_params["serial_no"] = params["serial_no"]  # noqa: E501

        query_params = []
        if "lang" in params:
            query_params.append(("lang", params["lang"]))  # noqa: E501

        header_params = {}

        body_params = None

        return self.api_client.call_api(
            "/v1/clusterview/get-node-summary/{serial_no}",
            "GET",
            path_params,
            query_params,
            header_params,
            body=body_params,
        )

    def get_node_summary_count(self, serial_no, **kwargs):  # noqa: E501
        """Provides data of the systems running 7-Mode and presented in the Node Summary Count table.  # noqa: E501

        Displays data in the Node Summary Count represented by the categories provided below:   Local Tiers,   Volumes,   LUNs   # noqa: E501
        :param str serial_no: Specifies the required serial number field. (required)
        :param str lang: Value representing a language
        """

        all_params = ["serial_no", "lang"]  # noqa: E501

        params = locals()
        for key, val in params["kwargs"].items():
            if key not in all_params:
                raise TypeError(
                    "Got an unexpected keyword argument '%s'"
                    " to method get_node_summary_count" % key
                )
            params[key] = val
        del params["kwargs"]
        # verify the required parameter 'serial_no' is set
        if "serial_no" not in params or params["serial_no"] is None:
            raise ValueError(
                "Missing the required parameter `serial_no` when calling `get_node_summary_count`"
            )  # noqa: E501

        path_params = {}
        if "serial_no" in params:
            path_params["serial_no"] = params["serial_no"]  # noqa: E501

        query_params = []
        if "lang" in params:
            query_params.append(("lang", params["lang"]))  # noqa: E501

        header_params = {}

        body_params = None

        return self.api_client.call_api(
            "/v1/clusterview/get-node-summary-count/{serial_no}",
            "GET",
            path_params,
            query_params,
            header_params,
            body=body_params,
        )

    def get_raid_disk_visualization(self, serial_no, **kwargs):  # noqa: E501
        """Provides Raid Disk Visualization data.  # noqa: E501

        Raid Disk Visualization provides disk data for each shelf that is grouped under stack. It provides aggregate data with color coding to diffrentiate the disks on UI.   # noqa: E501
        :param str serial_no: Specifies the required serial number field. (required)
        :param str lang: Value representing a language
        """

        all_params = ["serial_no", "lang"]  # noqa: E501

        params = locals()
        for key, val in params["kwargs"].items():
            if key not in all_params:
                raise TypeError(
                    "Got an unexpected keyword argument '%s'"
                    " to method get_raid_disk_visualization" % key
                )
            params[key] = val
        del params["kwargs"]
        # verify the required parameter 'serial_no' is set
        if "serial_no" not in params or params["serial_no"] is None:
            raise ValueError(
                "Missing the required parameter `serial_no` when calling `get_raid_disk_visualization`"
            )  # noqa: E501

        path_params = {}
        if "serial_no" in params:
            path_params["serial_no"] = params["serial_no"]  # noqa: E501

        query_params = []
        if "lang" in params:
            query_params.append(("lang", params["lang"]))  # noqa: E501

        header_params = {}

        body_params = None

        return self.api_client.call_api(
            "/v1/clusterview/get-disk-visualization/{serial_no}",
            "GET",
            path_params,
            query_params,
            header_params,
            body=body_params,
        )

    def get_resolver(self, serial_no, **kwargs):  # noqa: E501
        """Provides information about a cluster and node for a specific Serial number, Cluster ID, and Job ID.  # noqa: E501

        Provides information about a cluster and node for a specific Serial number, Cluster ID, and Job ID.   # noqa: E501
        :param str serial_no: Specifies the serial number field. (required)
        :param str lang: Value representing a language
        """

        all_params = ["serial_no", "lang"]  # noqa: E501

        params = locals()
        for key, val in params["kwargs"].items():
            if key not in all_params:
                raise TypeError(
                    "Got an unexpected keyword argument '%s'"
                    " to method get_resolver" % key
                )
            params[key] = val
        del params["kwargs"]
        # verify the required parameter 'serial_no' is set
        if "serial_no" not in params or params["serial_no"] is None:
            raise ValueError(
                "Missing the required parameter `serial_no` when calling `get_resolver`"
            )  # noqa: E501

        path_params = {}
        if "serial_no" in params:
            path_params["serial_no"] = params["serial_no"]  # noqa: E501

        query_params = []
        if "lang" in params:
            query_params.append(("lang", params["lang"]))  # noqa: E501

        header_params = {}

        body_params = None

        return self.api_client.call_api(
            "/v1/clusterview/resolver/{serial_no}",
            "GET",
            path_params,
            query_params,
            header_params,
            body=body_params,
        )

    def get_shelf_adp_data(self, serial_no, **kwargs):  # noqa: E501
        """Provides data for the Shelf and Drive Summary for ADP.  # noqa: E501

        Displays the data for the Shelf and Drive Summary ADP represented in the categories provided below:   Shelf Type,   Shelf Serial Number,   Drive Type,   Drive Model,   Drive RPM,   Disk Marketing Size (GiB),   Number of Owned Partitions,   Number of Data Partitions,   Number of Parity Partitions,   Number of Spare Partitions,   Number of ADP Drives,   Number of Unowned Drives   # noqa: E501
        :param str serial_no: Specifies the required serial number field. (required)
        :param str lang: Value representing a language
        """

        all_params = ["serial_no", "lang"]  # noqa: E501

        params = locals()
        for key, val in params["kwargs"].items():
            if key not in all_params:
                raise TypeError(
                    "Got an unexpected keyword argument '%s'"
                    " to method get_shelf_adp_data" % key
                )
            params[key] = val
        del params["kwargs"]
        if "serial_no" not in params or params["serial_no"] is None:
            raise ValueError(
                "Missing the required parameter `serial_no` when calling `get_shelf_adp_data`"
            )  # noqa: E501

        path_params = {}
        if "serial_no" in params:
            path_params["serial_no"] = params["serial_no"]  # noqa: E501

        query_params = []
        if "lang" in params:
            query_params.append(("lang", params["lang"]))  # noqa: E501

        header_params = {}

        body_params = None

        return self.api_client.call_api(
            "/v1/clusterview/get-shelf-adp-data/{serial_no}",
            "GET",
            path_params,
            query_params,
            header_params,
            body=body_params,
        )

    def get_shelf_and_drive_count(self, serial_no, **kwargs):  # noqa: E501
        """Provides data for the Shelf and Drive Count.  # noqa: E501

        Displays the data for the Shelf and Drive count represented in the categories provided below:   Shelf Count,   Drive Count   # noqa: E501
        :param str serial_no: Specifies the required serial number field. (required)
        :param str lang: Value representing a language
        """

        all_params = ["serial_no", "lang"]  # noqa: E501

        params = locals()
        for key, val in params["kwargs"].items():
            if key not in all_params:
                raise TypeError(
                    "Got an unexpected keyword argument '%s'"
                    " to method get_shelf_and_drive_count" % key
                )
            params[key] = val
        del params["kwargs"]
        # verify the required parameter 'serial_no' is set
        if "serial_no" not in params or params["serial_no"] is None:
            raise ValueError(
                "Missing the required parameter `serial_no` when calling `get_shelf_and_drive_count`"
            )  # noqa: E501

        path_params = {}
        if "serial_no" in params:
            path_params["serial_no"] = params["serial_no"]  # noqa: E501

        query_params = []
        if "lang" in params:
            query_params.append(("lang", params["lang"]))  # noqa: E501

        header_params = {}

        body_params = None

        return self.api_client.call_api(
            "/v1/clusterview/get-shelf-drive-count/{serial_no}",
            "GET",
            path_params,
            query_params,
            header_params,
            body=body_params,
        )

    def get_shelf_data(self, serial_no, **kwargs):  # noqa: E501
        """Provides data for the Shelf and Drive Summary.  # noqa: E501

        Displays the data for the Shelf and Drive Summary represented in the categories provided below:   Shelf Type,   Shelf Serial Number,   Disk Type,   Disk Model,   Disk RPM,   Disk Marketing Size (GiB),   Number of Owned Disks,   Number of Data Drives,   Number of Parity Drives,   Number of Spare Disks,   Number of Unowned Disks   # noqa: E501
        :param str serial_no: Specifies the required serial number field. (required)
        :param str lang: Value representing a language
        """

        all_params = ["serial_no", "lang"]  # noqa: E501

        params = locals()
        for key, val in params["kwargs"].items():
            if key not in all_params:
                raise TypeError(
                    "Got an unexpected keyword argument '%s'"
                    " to method get_shelf_data" % key
                )
            params[key] = val
        del params["kwargs"]
        # verify the required parameter 'serial_no' is set
        if "serial_no" not in params or params["serial_no"] is None:
            raise ValueError(
                "Missing the required parameter `serial_no` when calling `get_shelf_data`"
            )  # noqa: E501

        path_params = {}
        if "serial_no" in params:
            path_params["serial_no"] = params["serial_no"]  # noqa: E501

        query_params = []
        if "lang" in params:
            query_params.append(("lang", params["lang"]))  # noqa: E501

        header_params = {}

        body_params = None

        return self.api_client.call_api(
            "/v1/clusterview/get-shelf-data/{serial_no}",
            "GET",
            path_params,
            query_params,
            header_params,
            body=body_params,
        )

    def get_stack_details(self, serial_no, **kwargs):  # noqa: E501
        """Provides stack and shelf data for the Stack Diagram.  # noqa: E501

        Provides stack and shelf data for the Stack Diagram table. Disks will be grouped under shelf and shelves will be grouped under stack.   # noqa: E501
        :param str serial_no: Specifies the required serial number field. (required)
        :param str lang: Value representing a language
        """

        all_params = ["serial_no", "lang"]  # noqa: E501

        params = locals()
        for key, val in params["kwargs"].items():
            if key not in all_params:
                raise TypeError(
                    "Got an unexpected keyword argument '%s'"
                    " to method get_stack_details" % key
                )
            params[key] = val
        del params["kwargs"]
        # verify the required parameter 'serial_no' is set
        if "serial_no" not in params or params["serial_no"] is None:
            raise ValueError(
                "Missing the required parameter `serial_no` when calling `get_stack_details`"
            )  # noqa: E501

        path_params = {}
        if "serial_no" in params:
            path_params["serial_no"] = params["serial_no"]  # noqa: E501

        query_params = []
        if "lang" in params:
            query_params.append(("lang", params["lang"]))  # noqa: E501

        header_params = {}

        body_params = None

        return self.api_client.call_api(
            "/v1/clusterview/get-stack-details/{serial_no}",
            "GET",
            path_params,
            query_params,
            header_params,
            body=body_params,
        )

    def get_stack_visualization(self, serial_no, **kwargs):  # noqa: E501
        """Provides Stack Visualization data.  # noqa: E501

        Stack Visualization provides stack and shelf data.   # noqa: E501
        :param str serial_no: Specifies the required serial number field. (required)
        :param str lang: Value representing a language
        """

        all_params = ["serial_no", "lang"]  # noqa: E501

        params = locals()
        for key, val in params["kwargs"].items():
            if key not in all_params:
                raise TypeError(
                    "Got an unexpected keyword argument '%s'"
                    " to method get_stack_visualization" % key
                )
            params[key] = val
        del params["kwargs"]
        # verify the required parameter 'serial_no' is set
        if "serial_no" not in params or params["serial_no"] is None:
            raise ValueError(
                "Missing the required parameter `serial_no` when calling `get_stack_visualization`"
            )  # noqa: E501

        path_params = {}
        if "serial_no" in params:
            path_params["serial_no"] = params["serial_no"]  # noqa: E501

        query_params = []
        if "lang" in params:
            query_params.append(("lang", params["lang"]))  # noqa: E501

        header_params = {}

        body_params = None

        return self.api_client.call_api(
            "/v1/clusterview/get-stack-visualization/{serial_no}",
            "GET",
            path_params,
            query_params,
            header_params,
            body=body_params,
        )

    def get_switch_details(self, serial_no, **kwargs):  # noqa: E501
        """Provides data for the Switch Details.  # noqa: E501

        Displays the data for the Switch Details represented in the categories provided below:   Switch Name,   Serial Number,   IP Address,   Model Number,   Switch Network,   Software Version,   SNMP Version,   Community String,   Is Discovered,   Switch Monitoring Status   # noqa: E501
        :param str serial_no: Specifies the required serial number field. (required)
        :param str lang: Value representing a language
        """

        all_params = ["serial_no", "lang"]  # noqa: E501

        params = locals()
        for key, val in params["kwargs"].items():
            if key not in all_params:
                raise TypeError(
                    "Got an unexpected keyword argument '%s'"
                    " to method get_switch_details" % key
                )
            params[key] = val
        del params["kwargs"]
        # verify the required parameter 'serial_no' is set
        if "serial_no" not in params or params["serial_no"] is None:
            raise ValueError(
                "Missing the required parameter `serial_no` when calling `get_switch_details`"
            )  # noqa: E501

        path_params = {}
        if "serial_no" in params:
            path_params["serial_no"] = params["serial_no"]  # noqa: E501

        query_params = []
        if "lang" in params:
            query_params.append(("lang", params["lang"]))  # noqa: E501

        header_params = {}

        body_params = None

        return self.api_client.call_api(
            "/v1/clusterview/get-switch-details/{serial_no}",
            "GET",
            path_params,
            query_params,
            header_params,
            body=body_params,
        )

    def get_system_options(self, serial_no, **kwargs):  # noqa: E501
        """Provides System Options data.  # noqa: E501

        Provides System Options data.   # noqa: E501
        :param str serial_no: Specifies the required serial number field. (required)
        :param str lang: Value representing a language
        """

        all_params = ["serial_no", "lang"]  # noqa: E501

        params = locals()
        for key, val in params["kwargs"].items():
            if key not in all_params:
                raise TypeError(
                    "Got an unexpected keyword argument '%s'"
                    " to method get_system_options" % key
                )
            params[key] = val
        del params["kwargs"]
        # verify the required parameter 'serial_no' is set
        if "serial_no" not in params or params["serial_no"] is None:
            raise ValueError(
                "Missing the required parameter `serial_no` when calling `get_system_options`"
            )  # noqa: E501

        path_params = {}
        if "serial_no" in params:
            path_params["serial_no"] = params["serial_no"]  # noqa: E501

        query_params = []
        if "lang" in params:
            query_params.append(("lang", params["lang"]))  # noqa: E501

        header_params = {}

        body_params = None

        return self.api_client.call_api(
            "/v1/clusterview/get-system-options/{serial_no}",
            "GET",
            path_params,
            query_params,
            header_params,
            body=body_params,
        )

    def get_volume_efficiency(self, serial_no, **kwargs):  # noqa: E501
        """Provides data for the Volume Efficiency.  # noqa: E501

        Displays the data for the Volume Efficiency represented in the categories provided below:   SVM Name,   Volume Name,   Volume Efficiency Ratio,   Logical Used (GiB),   Physical Used (GiB),   Snapshot Used (GiB),   Total Saved (GiB),   Total Saved Percentage,   Deduplicated (GiB),   Deduplicated Percentage,   Compressed (GiB),   Compressed Percentage,   Enabled Efficiency Features   # noqa: E501
        :param str serial_no: Specifies the required serial number field. (required)
        :param str lang: Value representing a language
        """

        all_params = ["serial_no", "lang"]  # noqa: E501

        params = locals()
        for key, val in params["kwargs"].items():
            if key not in all_params:
                raise TypeError(
                    "Got an unexpected keyword argument '%s'"
                    " to method get_volume_efficiency" % key
                )
            params[key] = val
        del params["kwargs"]
        # verify the required parameter 'serial_no' is set
        if "serial_no" not in params or params["serial_no"] is None:
            raise ValueError(
                "Missing the required parameter `serial_no` when calling `get_volume_efficiency`"
            )  # noqa: E501

        path_params = {}
        if "serial_no" in params:
            path_params["serial_no"] = params["serial_no"]  # noqa: E501

        query_params = []
        if "lang" in params:
            query_params.append(("lang", params["lang"]))  # noqa: E501

        header_params = {}

        body_params = None

        return self.api_client.call_api(
            "/v1/clusterview/get-volume-efficiency/{serial_no}",
            "GET",
            path_params,
            query_params,
            header_params,
            body=body_params,
        )

    def get_volume_summary(self, serial_no, **kwargs):  # noqa: E501
        """Provides data for the Volume Summary.  # noqa: E501

        Displays the data for the Volume Summary represented in the categories provided below:   Volume Name,   SVM Name,   Local Tier Name,   Volume Capacity (GiB),   Used Capacity (GiB),   Available Capacity (GiB),   Physical Capacity (GiB),   Logical Capacity (GiB),   Used Data Percentage,   Snapshot Reserve Used Percentage,   Snapshots,   Volume Thin Provisioned?,   Volume Type   # noqa: E501
        :param str serial_no: Specifies the required serial number field. (required)
        :param str lang: Value representing a language
        """

        all_params = ["serial_no", "lang"]  # noqa: E501

        params = locals()
        for key, val in params["kwargs"].items():
            if key not in all_params:
                raise TypeError(
                    "Got an unexpected keyword argument '%s'"
                    " to method get_volume_summary" % key
                )
            params[key] = val
        del params["kwargs"]
        # verify the required parameter 'serial_no' is set
        if "serial_no" not in params or params["serial_no"] is None:
            raise ValueError(
                "Missing the required parameter `serial_no` when calling `get_volume_summary`"
            )  # noqa: E501

        path_params = {}
        if "serial_no" in params:
            path_params["serial_no"] = params["serial_no"]  # noqa: E501

        query_params = []
        if "lang" in params:
            query_params.append(("lang", params["lang"]))  # noqa: E501

        header_params = {}

        body_params = None

        return self.api_client.call_api(
            "/v1/clusterview/get-volume-summary/{serial_no}",
            "GET",
            path_params,
            query_params,
            header_params,
            body=body_params,
        )
