# coding: utf-8
from .api_client import ApiClient


class DatacenterInsightsApi:
    def __init__(self, api_client=None):
        if api_client is None:
            api_client = ApiClient()
        self.api_client = api_client

    def get_cluster_details_for_topology(
        self, level, level_id, cluster_name, **kwargs
    ):  # noqa: E501
        """Provides cluster details for topology view for given given level, level_id and cluster_name  # noqa: E501

        Provides cluster details for topology view for given given level, level_id and cluster_name   # noqa: E501
        :param str level: Required level to fetch relevant data (required)
        :param str level_id: Required level_id appropriate to level (required)
        :param str cluster_name: Required cluster_name appropriate to level (required)
        """

        all_params = ["level", "level_id", "cluster_name"]  # noqa: E501

        params = locals()
        for key, val in params["kwargs"].items():
            if key not in all_params:
                raise TypeError(
                    "Got an unexpected keyword argument '%s'"
                    " to method get_cluster_details_for_topology" % key
                )
            params[key] = val
        del params["kwargs"]
        # verify the required parameter 'level' is set
        if "level" not in params or params["level"] is None:
            raise ValueError(
                "Missing the required parameter `level` when calling `get_cluster_details_for_topology`"
            )  # noqa: E501
        # verify the required parameter 'level_id' is set
        if "level_id" not in params or params["level_id"] is None:
            raise ValueError(
                "Missing the required parameter `level_id` when calling `get_cluster_details_for_topology`"
            )  # noqa: E501
        # verify the required parameter 'cluster_name' is set
        if "cluster_name" not in params or params["cluster_name"] is None:
            raise ValueError(
                "Missing the required parameter `cluster_name` when calling `get_cluster_details_for_topology`"
            )  # noqa: E501

        path_params = {}
        if "level" in params:
            path_params["level"] = params["level"]  # noqa: E501
        if "level_id" in params:
            path_params["level_id"] = params["level_id"]  # noqa: E501
        if "cluster_name" in params:
            path_params["cluster_name"] = params["cluster_name"]  # noqa: E501

        query_params = []

        header_params = {}

        body_params = None

        return self.api_client.call_api(
            "/v1/datacenter/topology/{level}/{level_id}/clusters/{cluster_name}",
            "GET",
            path_params,
            query_params,
            header_params,
            body=body_params,
        )

    def get_clusters_for_level(self, level, level_id, **kwargs):  # noqa: E501
        """Provides listing of clusters for given level and level_id  # noqa: E501

        Provides listing of clusters for given level and level_id   # noqa: E501
        :param str level: Required level to fetch relevant data (required)
        :param str level_id: Required level_id appropriate to level (required)
        """

        all_params = ["level", "level_id"]  # noqa: E501

        params = locals()
        for key, val in params["kwargs"].items():
            if key not in all_params:
                raise TypeError(
                    "Got an unexpected keyword argument '%s'"
                    " to method get_clusters_for_level" % key
                )
            params[key] = val
        del params["kwargs"]

        # verify the required parameter 'level' is set
        if "level" not in params or params["level"] is None:
            raise ValueError(
                "Missing the required parameter `level` when calling `get_clusters_for_level`"
            )  # noqa: E501
        # verify the required parameter 'level_id' is set
        if "level_id" not in params or params["level_id"] is None:
            raise ValueError(
                "Missing the required parameter `level_id` when calling `get_clusters_for_level`"
            )  # noqa: E501

        path_params = {}
        if "level" in params:
            path_params["level"] = params["level"]  # noqa: E501
        if "level_id" in params:
            path_params["level_id"] = params["level_id"]  # noqa: E501

        query_params = []

        header_params = {}

        body_params = None

        return self.api_client.call_api(
            "/v1/datacenter/clusters/{level}/{level_id}",
            "GET",
            path_params,
            query_params,
            header_params,
            body=body_params,
        )

    def get_devices_for_level(self, level, level_id, **kwargs):  # noqa: E501
        """Provides listing of devices for given level and level_id  # noqa: E501

        List the OneCollect devices relevant to a given level and level_id where hosts, switches and mappings to controllers are available   # noqa: E501
        :param str level: Required level to fetch relevant data (required)
        :param str level_id: Required level_id appropriate to level (required)
        """

        all_params = ["level", "level_id"]  # noqa: E501

        params = locals()
        for key, val in params["kwargs"].items():
            if key not in all_params:
                raise TypeError(
                    "Got an unexpected keyword argument '%s'"
                    " to method get_devices_for_level" % key
                )
            params[key] = val
        del params["kwargs"]
        # verify the required parameter 'level' is set
        if "level" not in params or params["level"] is None:
            raise ValueError(
                "Missing the required parameter `level` when calling `get_devices_for_level`"
            )  # noqa: E501
        # verify the required parameter 'level_id' is set
        if "level_id" not in params or params["level_id"] is None:
            raise ValueError(
                "Missing the required parameter `level_id` when calling `get_devices_for_level`"
            )  # noqa: E501

        path_params = {}
        if "level" in params:
            path_params["level"] = params["level"]  # noqa: E501
        if "level_id" in params:
            path_params["level_id"] = params["level_id"]  # noqa: E501

        query_params = []

        header_params = {}

        body_params = None

        return self.api_client.call_api(
            "/v1/datacenter/devices/{level}/{level_id}",
            "GET",
            path_params,
            query_params,
            header_params,
            body=body_params,
        )

    def get_host_details_for_topology(
        self, level, level_id, hostname, **kwargs
    ):  # noqa: E501
        """Provides host details for topology view for given given level, level_id and hostname  # noqa: E501

        Provides host details for topology view for given given level, level_id and hostname   # noqa: E501
        :param str level: Required level to fetch relevant data (required)
        :param str level_id: Required level_id appropriate to level (required)
        :param str hostname: Required hostname appropriate to level (required)
        """

        all_params = ["level", "level_id", "hostname"]  # noqa: E501

        params = locals()
        for key, val in params["kwargs"].items():
            if key not in all_params:
                raise TypeError(
                    "Got an unexpected keyword argument '%s'"
                    " to method get_host_details_for_topology" % key
                )
            params[key] = val
        del params["kwargs"]
        # verify the required parameter 'level' is set
        if "level" not in params or params["level"] is None:
            raise ValueError(
                "Missing the required parameter `level` when calling `get_host_details_for_topology`"
            )  # noqa: E501
        # verify the required parameter 'level_id' is set
        if "level_id" not in params or params["level_id"] is None:
            raise ValueError(
                "Missing the required parameter `level_id` when calling `get_host_details_for_topology`"
            )  # noqa: E501
        # verify the required parameter 'hostname' is set
        if "hostname" not in params or params["hostname"] is None:
            raise ValueError(
                "Missing the required parameter `hostname` when calling `get_host_details_for_topology`"
            )  # noqa: E501

        path_params = {}
        if "level" in params:
            path_params["level"] = params["level"]  # noqa: E501
        if "level_id" in params:
            path_params["level_id"] = params["level_id"]  # noqa: E501
        if "hostname" in params:
            path_params["hostname"] = params["hostname"]  # noqa: E501

        query_params = []

        header_params = {}

        body_params = None

        return self.api_client.call_api(
            "/v1/datacenter/topology/{level}/{level_id}/hosts/{hostname}",
            "GET",
            path_params,
            query_params,
            header_params,
            body=body_params,
        )

    def get_hosts_with_snapmirrors(self, level, level_id, **kwargs):  # noqa: E501
        """Provides listing of hosts linked to snapmirrors for given level, level_id  # noqa: E501

        Provides listing of hosts linked to snapmirrors for given level, level_id   # noqa: E501
        :param str level: Required level to fetch relevant data (required)
        :param str level_id: Required level_id appropriate to level (required)
        """

        all_params = ["level", "level_id"]  # noqa: E501

        params = locals()
        for key, val in params["kwargs"].items():
            if key not in all_params:
                raise TypeError(
                    "Got an unexpected keyword argument '%s'"
                    " to method get_hosts_with_snapmirrors" % key
                )
            params[key] = val
        del params["kwargs"]
        # verify the required parameter 'level' is set
        if "level" not in params or params["level"] is None:
            raise ValueError(
                "Missing the required parameter `level` when calling `get_hosts_with_snapmirrors`"
            )  # noqa: E501
        # verify the required parameter 'level_id' is set
        if "level_id" not in params or params["level_id"] is None:
            raise ValueError(
                "Missing the required parameter `level_id` when calling `get_hosts_with_snapmirrors`"
            )  # noqa: E501

        path_params = {}
        if "level" in params:
            path_params["level"] = params["level"]  # noqa: E501
        if "level_id" in params:
            path_params["level_id"] = params["level_id"]  # noqa: E501

        query_params = []

        header_params = {}

        body_params = None

        return self.api_client.call_api(
            "/v1/datacenter/snapmirrors/{level}/{level_id}/hosts",
            "GET",
            path_params,
            query_params,
            header_params,
            body=body_params,
        )

    def get_snapmirrors_for_level_and_cluster(
        self, level, level_id, cluster_name, **kwargs
    ):  # noqa: E501
        """Provides listing of snapmirrors for given level, level_id and cluster_name  # noqa: E501

        Provides listing of snapmirrors for given level, level_id and cluster_name   # noqa: E501
        :param str level: Required level to fetch relevant data (required)
        :param str level_id: Required level_id appropriate to level (required)
        :param str cluster_name: Required cluster_name appropriate to level (required)
        """

        all_params = ["level", "level_id", "cluster_name"]  # noqa: E501

        params = locals()
        for key, val in params["kwargs"].items():
            if key not in all_params:
                raise TypeError(
                    "Got an unexpected keyword argument '%s'"
                    " to method get_snapmirrors_for_level_and_cluster" % key
                )
            params[key] = val
        del params["kwargs"]
        # verify the required parameter 'level' is set
        if "level" not in params or params["level"] is None:
            raise ValueError(
                "Missing the required parameter `level` when calling `get_snapmirrors_for_level_and_cluster`"
            )  # noqa: E501
        # verify the required parameter 'level_id' is set
        if "level_id" not in params or params["level_id"] is None:
            raise ValueError(
                "Missing the required parameter `level_id` when calling `get_snapmirrors_for_level_and_cluster`"
            )  # noqa: E501
        # verify the required parameter 'cluster_name' is set
        if "cluster_name" not in params or params["cluster_name"] is None:
            raise ValueError(
                "Missing the required parameter `cluster_name` when calling `get_snapmirrors_for_level_and_cluster`"
            )  # noqa: E501

        path_params = {}
        if "level" in params:
            path_params["level"] = params["level"]  # noqa: E501
        if "level_id" in params:
            path_params["level_id"] = params["level_id"]  # noqa: E501
        if "cluster_name" in params:
            path_params["cluster_name"] = params["cluster_name"]  # noqa: E501

        query_params = []

        header_params = {}

        body_params = None

        return self.api_client.call_api(
            "/v1/datacenter/snapmirrors/{level}/{level_id}/clusters/{cluster_name}",
            "GET",
            path_params,
            query_params,
            header_params,
            body=body_params,
        )

    def get_snapmirrors_for_level_and_hostname(
        self, level, level_id, hostname, **kwargs
    ):  # noqa: E501
        """Provides listing of snapmirrors for given level, level_id and hostname  # noqa: E501

        Provides listing of snapmirrors for given level, level_id and hostname   # noqa: E501
        :param str level: Required level to fetch relevant data (required)
        :param str level_id: Required level_id appropriate to level (required)
        :param str hostname: Required hostname appropriate to level (required)
        """

        all_params = ["level", "level_id", "hostname"]  # noqa: E501

        params = locals()
        for key, val in params["kwargs"].items():
            if key not in all_params:
                raise TypeError(
                    "Got an unexpected keyword argument '%s'"
                    " to method get_snapmirrors_for_level_and_hostname" % key
                )
            params[key] = val
        del params["kwargs"]
        # verify the required parameter 'level' is set
        if "level" not in params or params["level"] is None:
            raise ValueError(
                "Missing the required parameter `level` when calling `get_snapmirrors_for_level_and_hostname`"
            )  # noqa: E501
        # verify the required parameter 'level_id' is set
        if "level_id" not in params or params["level_id"] is None:
            raise ValueError(
                "Missing the required parameter `level_id` when calling `get_snapmirrors_for_level_and_hostname`"
            )  # noqa: E501
        # verify the required parameter 'hostname' is set
        if "hostname" not in params or params["hostname"] is None:
            raise ValueError(
                "Missing the required parameter `hostname` when calling `get_snapmirrors_for_level_and_hostname`"
            )  # noqa: E501

        path_params = {}
        if "level" in params:
            path_params["level"] = params["level"]  # noqa: E501
        if "level_id" in params:
            path_params["level_id"] = params["level_id"]  # noqa: E501
        if "hostname" in params:
            path_params["hostname"] = params["hostname"]  # noqa: E501

        query_params = []

        header_params = {}

        body_params = None

        return self.api_client.call_api(
            "/v1/datacenter/snapmirrors/{level}/{level_id}/hosts/{hostname}",
            "GET",
            path_params,
            query_params,
            header_params,
            body=body_params,
        )

    def get_topology_clusters_for_level(self, level, level_id, **kwargs):  # noqa: E501
        """Provides mapping of cluster to host for level and level_id  # noqa: E501

        Provides mapping of cluster to host for level and level_id   # noqa: E501
        :param str level: Required level to fetch relevant data (required)
        :param str level_id: Required level_id appropriate to level (required)
        """

        all_params = ["level", "level_id"]  # noqa: E501

        params = locals()
        for key, val in params["kwargs"].items():
            if key not in all_params:
                raise TypeError(
                    "Got an unexpected keyword argument '%s'"
                    " to method get_topology_clusters_for_level" % key
                )
            params[key] = val
        del params["kwargs"]
        # verify the required parameter 'level' is set
        if "level" not in params or params["level"] is None:
            raise ValueError(
                "Missing the required parameter `level` when calling `get_topology_clusters_for_level`"
            )  # noqa: E501
        # verify the required parameter 'level_id' is set
        if "level_id" not in params or params["level_id"] is None:
            raise ValueError(
                "Missing the required parameter `level_id` when calling `get_topology_clusters_for_level`"
            )  # noqa: E501

        path_params = {}
        if "level" in params:
            path_params["level"] = params["level"]  # noqa: E501
        if "level_id" in params:
            path_params["level_id"] = params["level_id"]  # noqa: E501

        query_params = []

        header_params = {}

        body_params = None

        return self.api_client.call_api(
            "/v1/datacenter/topology/{level}/{level_id}",
            "GET",
            path_params,
            query_params,
            header_params,
            body=body_params,
        )

    def get_volumes_for_cluster(
        self, level, level_id, cluster_name, **kwargs
    ):  # noqa: E501
        """Provides listing of volumes for given level, level_id and cluster_name  # noqa: E501

        Provides listing of volumes for given level, level_id and cluster_name   # noqa: E501
        :param str level: Required level to fetch relevant data (required)
        :param str level_id: Required level_id appropriate to level (required)
        :param str cluster_name: Required cluster_name appropriate to level (required)
        """

        all_params = ["level", "level_id", "cluster_name"]  # noqa: E501

        params = locals()
        for key, val in params["kwargs"].items():
            if key not in all_params:
                raise TypeError(
                    "Got an unexpected keyword argument '%s'"
                    " to method get_volumes_for_cluster" % key
                )
            params[key] = val
        del params["kwargs"]
        # verify the required parameter 'level' is set
        if "level" not in params or params["level"] is None:
            raise ValueError(
                "Missing the required parameter `level` when calling `get_volumes_for_cluster`"
            )  # noqa: E501
        # verify the required parameter 'level_id' is set
        if "level_id" not in params or params["level_id"] is None:
            raise ValueError(
                "Missing the required parameter `level_id` when calling `get_volumes_for_cluster`"
            )  # noqa: E501
        # verify the required parameter 'cluster_name' is set
        if "cluster_name" not in params or params["cluster_name"] is None:
            raise ValueError(
                "Missing the required parameter `cluster_name` when calling `get_volumes_for_cluster`"
            )  # noqa: E501

        path_params = {}
        if "level" in params:
            path_params["level"] = params["level"]  # noqa: E501
        if "level_id" in params:
            path_params["level_id"] = params["level_id"]  # noqa: E501
        if "cluster_name" in params:
            path_params["cluster_name"] = params["cluster_name"]  # noqa: E501

        query_params = []

        header_params = {}

        body_params = None

        return self.api_client.call_api(
            "/v1/datacenter/volumes/{level}/{level_id}/clusters/{cluster_name}",
            "GET",
            path_params,
            query_params,
            header_params,
            body=body_params,
        )

    def get_volumes_summary_for_level(self, level, level_id, **kwargs):  # noqa: E501
        """Provides count of protected, unprotected volumes for given level and level_id  # noqa: E501

        Provides count of protected, unprotected volumes for given level and level_id   # noqa: E501
        :param str level: Required level to fetch relevant data (required)
        :param str level_id: Required level_id appropriate to level (required)
        """

        all_params = ["level", "level_id"]  # noqa: E501

        params = locals()
        for key, val in params["kwargs"].items():
            if key not in all_params:
                raise TypeError(
                    "Got an unexpected keyword argument '%s'"
                    " to method get_volumes_summary_for_level" % key
                )
            params[key] = val
        del params["kwargs"]
        # verify the required parameter 'level' is set
        if "level" not in params or params["level"] is None:
            raise ValueError(
                "Missing the required parameter `level` when calling `get_volumes_summary_for_level`"
            )  # noqa: E501
        # verify the required parameter 'level_id' is set
        if "level_id" not in params or params["level_id"] is None:
            raise ValueError(
                "Missing the required parameter `level_id` when calling `get_volumes_summary_for_level`"
            )  # noqa: E501

        path_params = {}
        if "level" in params:
            path_params["level"] = params["level"]  # noqa: E501
        if "level_id" in params:
            path_params["level_id"] = params["level_id"]  # noqa: E501

        query_params = []

        header_params = {}

        body_params = None

        return self.api_client.call_api(
            "/v1/datacenter/volumes/{level}/{level_id}",
            "GET",
            path_params,
            query_params,
            header_params,
            body=body_params,
        )
