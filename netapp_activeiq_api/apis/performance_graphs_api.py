# coding: utf-8

from .api_client import ApiClient


class PerformanceGraphsApi:
    def __init__(self, api_client=None):
        if api_client is None:
            api_client = ApiClient()
        self.api_client = api_client

    def aggr_vol_list(self, cluster, **kwargs):  # noqa: E501
        """Provides information about Aggregates and Volumes for a  cluster or system .  # noqa: E501

        Provides information about Aggregates and Volumes for a  cluster or system .\"   # noqa: E501
        :param str cluster: Cluster ID for which aggregates, volumes info should be returned. (required)
        :param str exclude_root_vol: Specifies if the root volume to be exluded
        :param str svm_type: Specifies  the type of svm ,supports comma separated input
        :param str serial_numbers: Comma-separated list of serial numbers for which aggregates, volumes info should be returned.
        """

        all_params = [
            "cluster",
            "exclude_root_vol",
            "svm_type",
            "serial_numbers",
        ]  # noqa: E501

        params = locals()
        for key, val in params["kwargs"].items():
            if key not in all_params:
                raise TypeError(
                    "Got an unexpected keyword argument '%s'"
                    " to method aggr_vol_list" % key
                )
            params[key] = val
        del params["kwargs"]
        # verify the required parameter 'cluster' is set
        if "cluster" not in params or params["cluster"] is None:
            raise ValueError(
                "Missing the required parameter `cluster` when calling `aggr_vol_list`"
            )  # noqa: E501

        path_params = {}

        query_params = []
        if "exclude_root_vol" in params:
            query_params.append(
                ("excludeRootVol", params["exclude_root_vol"])
            )  # noqa: E501
        if "svm_type" in params:
            query_params.append(("svmType", params["svm_type"]))  # noqa: E501
        if "cluster" in params:
            query_params.append(("cluster", params["cluster"]))  # noqa: E501
        if "serial_numbers" in params:
            query_params.append(
                ("serialNumbers", params["serial_numbers"])
            )  # noqa: E501

        header_params = {}

        body_params = None

        return self.api_client.call_api(
            "/v1/performance-data/aggr-volumes",
            "GET",
            path_params,
            query_params,
            header_params,
            body=body_params,
        )

    def performance_graph(
        self, graph_name, start_date, end_date, **kwargs
    ):  # noqa: E501
        """Provides counter data for different performance graphs.  # noqa: E501

        Specifies the graph name, which is a counter name for a graph.   # noqa: E501
        :param str graph_name: Specifies the graph name that is the counter name for a graph.  Valid values for Node based graphs:  * node_protocol_iops  * node_network_throughput  * node_avg_iops  * node_latency  * node_headroom_cpu_utilization  * aggr_throughput  * node_headroom_aggr_utilization  Valid values for Cluster based graphs:  * cluster_avg_iops  * cluster_network_throughput  * volume_latency  * volume_iops  (required)
        :param str start_date: Specifies the start date for counter data for a specified duration. The valid date should be represented in the YYYY-MM-DD format, for example, 2020-01-19.  (required)
        :param str end_date: Specifies the end date for a counter data for a specified duration. The valid date should be later than the start date. It should be represented in the YYYY-MM-DD format, for example, 2020-05-15.  (required)
        :param str cluster: Specifies the cluster identifier for graph.
        :param str serial_number: Specifies the serial number of the node.
        :param str system_id: Specifies the system ID of a node.
        :param str aggregate_uuid: Specifies the universally unique identifier (UUID) for an aggregate. This parameter is mandatory for either \"aggr_throughput\" or \"node_headroom_aggr_utilization\" graph.
        :param str vol_instance_uuid: Specifies the universally unique identifier (UUID) for the volume. This parameter is mandatory for either \"volume_latency\" or \"volume_iops\" graph.
        """

        all_params = [
            "graph_name",
            "start_date",
            "end_date",
            "cluster",
            "serial_number",
            "system_id",
            "aggregate_uuid",
            "vol_instance_uuid",
        ]  # noqa: E501

        params = locals()
        for key, val in params["kwargs"].items():
            if key not in all_params:
                raise TypeError(
                    "Got an unexpected keyword argument '%s'"
                    " to method performance_graph" % key
                )
            params[key] = val
        del params["kwargs"]
        # verify the required parameter 'graph_name' is set
        if "graph_name" not in params or params["graph_name"] is None:
            raise ValueError(
                "Missing the required parameter `graph_name` when calling `performance_graph`"
            )  # noqa: E501
        # verify the required parameter 'start_date' is set
        if "start_date" not in params or params["start_date"] is None:
            raise ValueError(
                "Missing the required parameter `start_date` when calling `performance_graph`"
            )  # noqa: E501
        # verify the required parameter 'end_date' is set
        if "end_date" not in params or params["end_date"] is None:
            raise ValueError(
                "Missing the required parameter `end_date` when calling `performance_graph`"
            )  # noqa: E501

        path_params = {}

        query_params = []
        if "graph_name" in params:
            query_params.append(("graphName", params["graph_name"]))  # noqa: E501
        if "cluster" in params:
            query_params.append(("cluster", params["cluster"]))  # noqa: E501
        if "serial_number" in params:
            query_params.append(("serialNumber", params["serial_number"]))  # noqa: E501
        if "system_id" in params:
            query_params.append(("systemId", params["system_id"]))  # noqa: E501
        if "start_date" in params:
            query_params.append(("startDate", params["start_date"]))  # noqa: E501
        if "end_date" in params:
            query_params.append(("endDate", params["end_date"]))  # noqa: E501
        if "aggregate_uuid" in params:
            query_params.append(
                ("aggregateUuid", params["aggregate_uuid"])
            )  # noqa: E501
        if "vol_instance_uuid" in params:
            query_params.append(
                ("volInstanceUuid", params["vol_instance_uuid"])
            )  # noqa: E501

        header_params = {}

        body_params = None

        return self.api_client.call_api(
            "/v1/performance-data/graphs",
            "GET",
            path_params,
            query_params,
            header_params,
            body=body_params,
        )
