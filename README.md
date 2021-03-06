# netapp-activeiq-api-swagger

- API version: v1 en v2
- Package version: 0.0.1

## Sponsor 

[![Proact Belgium](https://proact.eu/wp-content/uploads/2020/03/proact-logo.png)](https://proact.eu) 

Building and improving this package have been sponsored by my employer **Proact Belgium**.

## Requirements.

Python 3.8+

## Installation & Usage
### pip install

If the python package is hosted on Github, you can install directly from Github

```sh
pip install git+https://github.com/woutercoppens/netapp-activeiq-api.git
```
(you may need to run `pip` with root permission: `sudo pip install git+https://github.com/woutercoppens/netapp-activeiq-api.git`)

Then import the package:
```python
import netapp_activeiq_api 
```

### Setuptools

Install via [Setuptools](http://pypi.python.org/pypi/setuptools).

```sh
python setup.py install --user
```
(or `sudo python setup.py install` to install the package for all users)

Then import the package:
```python
import netapp-activeiq-api
```

## Getting Started

Please follow the [installation procedure](#installation--usage) and then run the following:

```python
import netapp_activeiq_api
from pprint import pprint

# create an instance of the API class
aiq = netapp_activeiq_api.ActiveIQClient(request_token='123456789abc...', access_token='123456789abc...')

try:
    # Generates a new access token using a valid refresh token.
    api_response = aiq.SystemApi.get_list_by_level('customers')
    pprint(api_response)
except Exception as e:
    print("Exception when calling SystemApi.get_list_by_level('customers'): %s\n" % e)

```

## Documentation for API Endpoints

All URIs are relative to *https://api.activeiq.netapp.com*

Class | Method | HTTP request | Description
------------ | ------------- | ------------- | -------------
*AccessTokenApi* | [**get_access_token**]() | **POST** /v1/tokens/accessToken | Generates a new access token using a valid refresh token.
*StorageEfficiencyApi* | [**get_efficiency_details_by_level**]() | **GET** /v1/efficiency/details/level/{level}/id/{id} | Provides information about system efficiency based on different parameters at the customer,site,group,cluster or system level.
*StorageEfficiencyApi* | [**get_efficiency_summary_by_level**]() | **GET** /v1/efficiency/summary/level/{level}/id/{id} | Provides details about the systems with maximum capacity savings for a customer, site, group, or a set of serial numbers.
*StorageEfficiencyApi* | [**get_efficiency_summary**]() | **GET** /v2/efficiency/summary | Provides details about the systems with maximum capacity savings for a customer, site, group, or a set of serial numbers.
*CapacityApi* | [**get_capacity_details_by_level**]() | **GET** /v2/capacity/details/level/{level}/id/{id} | Provides the details about the systems nearing allocated capacity limit for a customer, site, group, cluster, watchlist or a set of serial numbers. 
*CapacityApi* | [**get_capacity_summary_by_level**]() | **GET** /v2/capacity/summary/level/{level}/id/{id} | Provides the number of systems nearing allocated capacity limit for a customer, site, group, cluster watchlist or a set of serial numbers.
*CapacityApi* | [**get_capacity_trend_details_by_level**]() | **GET** /v1/capacity/trend/level/{level}/id/{id} | Provides the capacity trending details about the systems for a customer, site, group, or a set of serial numbers.
*ClusterAnalyticsApi* | [**get_adapter_interface**]() | **GET** /v1/clusterview/get-adapter-interface/{serial_no} | Provides Adapter Interface data.
*ClusterAnalyticsApi* | [**get_aggregate_efficiency**]() | **GET** /v1/clusterview/get-aggregate-efficiency/{serial_no} | Provides data for the Local Tier Efficiency.
*ClusterAnalyticsApi* | [**get_aggregate_summary**]() | **GET** /v1/clusterview/get-aggregate-summary/{serial_no} | Provides data for the Local Tier Summary.
*ClusterAnalyticsApi* | [**get_cable_visualization**]() | **GET** /v1/clusterview/get-cable-visualization/{serial_no} | Provides Cable Visualization data.
*ClusterAnalyticsApi* | [**get_capacity_headroom_details**]() | **GET** /v1/clusterview/get-capacity-headroom/{serial_no} | Provides Capacity Headroom table data.
*ClusterAnalyticsApi* | [**get_cluster_configuration**]() | **GET** /v1/clusterview/get-cluster-configuration/{uuid} | Provides the cluster IP address, node, and release version data of a specific cluster UUID.
*ClusterAnalyticsApi* | [**get_cluster_summary**]() | **GET** /v1/clusterview/get-cluster-summary/{serial_no} | Provides the data for the Cluster Summary.
*ClusterAnalyticsApi* | [**get_disk_details**]() | **GET** /v1/clusterview/get-disk-details/{serial_no} | Provides Disk Details.
*ClusterAnalyticsApi* | [**get_free_slot_details**]() | **GET** /v1/clusterview/get-free-slot-details/{serial_no} | Provides free slots data.
*ClusterAnalyticsApi* | [**get_max_supported_capacity_details**]() | **GET** /v1/clusterview/get-max-supported-capacity/{serial_no} | Provides Max Supported Capacity data.
*ClusterAnalyticsApi* | [**get_module_overview**]() | **GET** /v1/clusterview/get-module-overview/{serial_no} | Provides data for the Module Overview.
*ClusterAnalyticsApi* | [**get_network_interfaces**]() | **GET** /v1/clusterview/get-network-interfaces/{serial_no} | Provides data for the Network Interface.
*ClusterAnalyticsApi* | [**get_network_ports**]() | **GET** /v1/clusterview/get-network-ports/{serial_no} | Provides data for the Network Ports.
*ClusterAnalyticsApi* | [**get_node_slot_map**]() | **GET** /v1/clusterview/get-node-slot-map/{serial_no} | Provides data for the Hardware Slot Map.
*ClusterAnalyticsApi* | [**get_node_summary**]() | **GET** /v1/clusterview/get-node-summary/{serial_no} | Provides data for the Node Summary.
*ClusterAnalyticsApi* | [**get_node_summary_count**]() | **GET** /v1/clusterview/get-node-summary-count/{serial_no} | Provides data of the systems running 7-Mode and presented in the Node Summary Count table.
*ClusterAnalyticsApi* | [**get_raid_disk_visualization**]() | **GET** /v1/clusterview/get-disk-visualization/{serial_no} | Provides Raid Disk Visualization data.
*ClusterAnalyticsApi* | [**get_resolver**]() | **GET** /v1/clusterview/resolver/{serial_no} | Provides information about a cluster and node for a specific Serial number, Cluster ID, and Job ID.
*ClusterAnalyticsApi* | [**get_shelf_adp_data**]() | **GET** /v1/clusterview/get-shelf-adp-data/{serial_no} | Provides data for the Shelf and Drive Summary for ADP.
*ClusterAnalyticsApi* | [**get_shelf_and_drive_count**]() | **GET** /v1/clusterview/get-shelf-drive-count/{serial_no} | Provides data for the Shelf and Drive Count.
*ClusterAnalyticsApi* | [**get_shelf_data**]() | **GET** /v1/clusterview/get-shelf-data/{serial_no} | Provides data for the Shelf and Drive Summary.
*ClusterAnalyticsApi* | [**get_stack_details**]() | **GET** /v1/clusterview/get-stack-details/{serial_no} | Provides stack and shelf data for the Stack Diagram.
*ClusterAnalyticsApi* | [**get_stack_visualization**]() | **GET** /v1/clusterview/get-stack-visualization/{serial_no} | Provides Stack Visualization data.
*ClusterAnalyticsApi* | [**get_switch_details**]() | **GET** /v1/clusterview/get-switch-details/{serial_no} | Provides data for the Switch Details.
*ClusterAnalyticsApi* | [**get_system_options**]() | **GET** /v1/clusterview/get-system-options/{serial_no} | Provides System Options data.
*ClusterAnalyticsApi* | [**get_volume_efficiency**]() | **GET** /v1/clusterview/get-volume-efficiency/{serial_no} | Provides data for the Volume Efficiency.
*ClusterAnalyticsApi* | [**get_volume_summary**]() | **GET** /v1/clusterview/get-volume-summary/{serial_no} | Provides data for the Volume Summary.
*DataAvailabilityApi* | [**data_availability**]() | **GET** /v1/interop-advisor/data-availability/{level}/{id} | Provides OC availability and InteropAdvisor URL for the given customer, site, group, node or cluster
*DatacenterInsightsApi* | [**get_cluster_details_for_topology**]() | **GET** /v1/datacenter/topology/{level}/{level_id}/clusters/{cluster_name} | Provides cluster details for topology view for given given level, level_id and cluster_name
*DatacenterInsightsApi* | [**get_clusters_for_level**]() | **GET** /v1/datacenter/clusters/{level}/{level_id} | Provides listing of clusters for given level and level_id
*DatacenterInsightsApi* | [**get_devices_for_level**]() | **GET** /v1/datacenter/devices/{level}/{level_id} | Provides listing of devices for given level and level_id
*DatacenterInsightsApi* | [**get_host_details_for_topology**]() | **GET** /v1/datacenter/topology/{level}/{level_id}/hosts/{hostname} | Provides host details for topology view for given given level, level_id and hostname
*DatacenterInsightsApi* | [**get_hosts_with_snapmirrors**]() | **GET** /v1/datacenter/snapmirrors/{level}/{level_id}/hosts | Provides listing of hosts linked to snapmirrors for given level, level_id
*DatacenterInsightsApi* | [**get_snapmirrors_for_level_and_cluster**]() | **GET** /v1/datacenter/snapmirrors/{level}/{level_id}/clusters/{cluster_name} | Provides listing of snapmirrors for given level, level_id and cluster_name
*DatacenterInsightsApi* | [**get_snapmirrors_for_level_and_hostname**]() | **GET** /v1/datacenter/snapmirrors/{level}/{level_id}/hosts/{hostname} | Provides listing of snapmirrors for given level, level_id and hostname
*DatacenterInsightsApi* | [**get_topology_clusters_for_level**]() | **GET** /v1/datacenter/topology/{level}/{level_id} | Provides mapping of cluster to host for level and level_id
*DatacenterInsightsApi* | [**get_volumes_for_cluster**]() | **GET** /v1/datacenter/volumes/{level}/{level_id}/clusters/{cluster_name} | Provides listing of volumes for given level, level_id and cluster_name
*DatacenterInsightsApi* | [**get_volumes_summary_for_level**]() | **GET** /v1/datacenter/volumes/{level}/{level_id} | Provides count of protected, unprotected volumes for given level and level_id
*DiskRemediationApi* | [**get_firmware_count**]() | **GET** /v1/disk-rem/fw-sys-count/{context}/{search_id}/type/{search_type} | Returns the ONTAP system count and details for disk/shelf/sp firmware upgrades.
*DiskRemediationApi* | [**get_firmware_details**]() | **GET** /v1/disk-rem/fw-file-details/{context}/{search_id}/type/{search_type} | Returns the MySupport URLs and URL count for firmware upgrade files.
*DiskRemediationApi* | [**get_firmware_details_risk**]() | **GET** /v1/disk-rem/fw-file-details/{context}/{search_id}/burtid/{burt_id}/type/{search_type} | Returns the MySupport URLs and URL count for firmware upgrade files at burt level.
*DiskRemediationApi* | [**get_inventory**]() | **GET** /v1/disk-rem/inventory/{context}/{search_id}/type/{search_type} | Provides inventory and playbook zip file to remediate disk/shelf/sp firmware risks.
*DiskRemediationApi* | [**get_inventory_post**]() | **POST** /v1/disk-rem/inventory/ | Provides inventory and playbook zip file from a pre-defined inventory output.
*DiskRemediationApi* | [**get_inventory_risk**]() | **GET** /v1/disk-rem/inventory/{context}/{search_id}/burtid/{burt_id}/type/{search_type} | Provides inventory and playbook zip file to remediate disk/shelf/sp firmware risks at burt level.
*DiskRemediationApi* | [**get_playbook**]() | **GET** /v1/disk-rem/playbook/type/{search_type} | Provides playbook files for disk/shelf/SP firmware upgrades
*HealthApi* | [**get_health_details_by_level**]() | **GET** /v1/health/details/level/{level}/id/{id} | Provides details about the risks for a customer, site, group, or a set of serial numbers
*HealthApi* | [**risk_instances**]() | **GET** /v2/health/risks | Returns information about risk occurrences
*HealthApi* | [**get_health_summary_by_level**]() | **GET** /v1/health/summary/level/{level}/id/{id} | Provides the number of risks for a customer, site, group, or a set of serial numbers.
*InteropSummaryCountApi* | [**interop_summary_count**]() | **GET** /v1/interop-advisor/summary-count/{level}/{id} | Provides supported, unsupported, remediation available count of a given ONTAP
*InteropSummaryDetailsApi* | [**interop_summary_details**]() | **GET** /v1/interop-advisor/summary-details/{level}/{id} | Provides supported, unsupported, remediation details of a given ONTAP
*PerformanceGraphsApi* | [**aggr_vol_list**]() | **GET** /v1/performance-data/aggr-volumes | Provides information about Aggregates and Volumes for a  cluster or system .
*PerformanceGraphsApi* | [**performance_graph**]() | **GET** /v1/performance-data/graphs | Provides counter data for different performance graphs.
*SearchApi* | [**search_aggregate_by_level**]() | **GET** /v1/search/aggregate/level/{level} | Infers information about the customer, site, cluster, or group based on the entered keywords
*SearchApi* | [**search_aggregate_count_by_level**]() | **GET** /v1/search/count/aggregate/level/{level} | Provides the aggregate count based on the input provided by the user.
*SearchApi* | [**search_location_by_level**]() | **GET** /v1/search/location/level/{level} | Provides the list of regions, or districts based on the input provided by the user.
*SearchApi* | [**search_location_count_by_level**]() | **GET** /v1/search/count/location/level/{level} | Lists Region or District based on the input provided by the user.
*SearchApi* | [**search_parent_by_level**]() | **GET** /v1/search/parent/level/{level} | Provides the list of NetApp Global Parent(NAGP), or Domestic Parent(DP) based on the input provided by the user.
*SearchApi* | [**search_parent_count_by_level**]() | **GET** /v1/search/count/parent/level/{level} | Lists NAGP or DP based on the input provided by the user.
*SearchApi* | [**search_system_by_level**]() | **GET** /v1/search/system/level/{level} | Provides the system details based on the input provided by the user.
*SearchApi* | [**search_system_by_level_v2**]() | **GET** /v2/search/system/level/{level} | Provides the system details based on the input provided by the user.
*SearchApi* | [**search_system_by_level_with_tier**]() | **GET** /v1/search/system/tier | Provides the system details based on the input provided by the user.
*SystemApi* | [**get_inventory_details_by_level**]() | **GET** /v1/system/inventory/details/level/{level}/id/{id} | Provides the configuration of systems, for a customer, site, group,watchlist or a set of serial numbers by pagination.
*SystemApi* | [**get_list_by_level**]() | **GET** /v1/system/list/level/{level} | Lists customers, sites, or groups.
*SystemApi* | [**get_system_details_by_level**]() | **GET** /v2/system/details/level/{level}/id/{id} | Provides the configuration of systems, for a customer, site, group, or a set of serial numbers by pagination.
*SystemApi* | [**search_systems_by_level**]() | **GET** /v1/system/search/level/{level} | Lists customers, sites, or groups based on the input provided by the user.
*SystemApi* | [**get_system_summary_by_level**]() | **GET** /v2/system/summary/level/{level}/id/{id} | Provides the number of products for a customer, site, group, or a set of serial numbers.
*SystemListApi* | [**get_system_count_partner_by_level**]() | **GET** /v2/systemList/partnerSystemCount/level/{level}/id/{id} | Provides the list of systems for a partner.
*SystemListApi* | [**get_system_count_sales_rep_by_level**]() | **GET** /v2/systemList/salesRepSystemCount/level/{level}/id/{id} | Provides the list of systems for a sales representative.
*SystemListApi* | [**get_system_list_aggregate_by_level**]() | **GET** /v1/systemList/aggregate/level/{level}/id/{id} | Provides the list of system for a customer, site, or group by pagination.
*SystemListApi* | [**get_system_list_location_by_level**]() | **GET** /v1/systemList/location/level/{level}/id/{id} | Provides the list of system for a region, or district by pagination.
*SystemListApi* | [**get_system_list_parent_by_level**]() | **GET** /v1/systemList/parent/level/{level}/id/{id} | Provides the list of system for a NetApp Global Parent(NAGP), or Domestic Parent(DP) by pagination.
*UpgradeApi* | [**get_disk_fw_upgrade_details_by_level**]() | **GET** /v1/upgrade/details/level/{level}/id/{id}/category/disk_fw | Provides details about systems where firmware is not up to date and needs to be upgraded for a customer, site, group, or a set of serial numbers. 
*UpgradeApi* | [**get_firmware_details**]() | **GET** /v1/firmware/details | Provides firmware details for nodes, shelves, and drives.
*UpgradeApi* | [**get_mb_fw_upgrade_details_by_level**]() | **GET** /v1/upgrade/details/level/{level}/id/{id}/category/mb_fw | Provides details about systems where firmware is not up to date and needs to be upgraded for a customer, site, group, or a set of serial numbers. 
*UpgradeApi* | [**get_upgrade_details_by_level_v2**]() | **GET** /v2/upgrade/details | Provides details about the systems where firmware is not up to date and needs to be upgraded for a customer, site, group, or a set of serial numbers. 
*UpgradeApi* | [**get_upgrade_summary_by_level**]() | **GET** /v1/upgrade/summary/level/{level}/id/{id} | Provides the number of systems where firmware is not up to date and needs to be upgraded for a customer, site, group, or a set of serial numbers. 
*ValueReportApi* | [**get_value_report_summary_by_level**]() | **GET** /v1/value-report/summary/level/{level} | Provides the aggregated value report details for set of serial numbers.
*ValueReportApi* | [**get_value_report_summary_by_id**]() | **GET** /v1/value-report/summary/level/{level}/id/{id} | Provides the aggregated value report details for a customer, site, group, cluster or serial number.
*WatchlistApi* | [**create_watchlist**]() | **POST** /v1/watchlist/create | Creates a watchlist with customers, sites, groups, global parents, domestic parents, districts, regions, serial numbers, partners, and sales representatives.
*WatchlistApi* | [**default_watchlist**]() | **PUT** /v1/watchlist/default/watchlistId/{watchlistId} | Update one of the created watchlist as default, based on the user input.
*WatchlistApi* | [**delete_watchlist**]() | **DELETE** /v1/watchlist/delete/watchlistId/{watchlistId} | Specifies the watchlist to be deleted by given Watchlist ID.
*WatchlistApi* | [**list_watchlist**]() | **GET** /v1/watchlist/all | Provide list of watchlist details for the user.
*WatchlistApi* | [**share_watchlist**]() | **PUT** /v1/watchlist/share | The created watchlist, user can share among internal other users.
*WatchlistApi* | [**system_count**]() | **GET** /v1/watchlist/count/watchlistId/{watchlistId} | Get the total system count for the given Watchlist ID.
*WatchlistApi* | [**update_watchlist**]() | **PUT** /v1/watchlist/update | Updates a watchlist with customers, sites, groups, global parents, domestic parents, districts, regions, serial numbers, partners, and sales representatives.
*WatchlistApi* | [**view_watchlist**]() | **GET** /v1/watchlist/id/{id} | Provides details about the watchlists that a user created by using customers, sites, groups, global parents, domestic parents, districts, regions, serial numbers, partners, and sales representatives.
*WellnessApi* | [**acknowledge_risk**]() | **POST** /v1/wellness/acknowledgeRisk | Acknowledge or Unacknowledge a risk for a number of systems.
*SearchRecordValidationApi* | [**search_system_validation_by_level**]() | **GET** /v1/search/system/validation/level/{level} | Validate search record details based on the input provided by the user.
*SupportCasesApi* | [**get_support_cases_by_id**]() | **GET** /v1/support/cases/{level}/{id} | Provides the information about open support cases for a customer, site, group or set of serial_numbers.
*SupportCasesApi* | [**get_support_rma_by_id**]() | **GET** /v1/support/rma/{level}/{id} | Provides information about RMA cases for a customer, site, group, or set of serial_numbers.
*UpgradeDetailsApi* | [**get_upgrade_action_details**]() | **GET** /v1/upgrades/details/level/{level}/id/{id} | Provides system count and  upgrade count.
*UpgradePercgeApi* | [**upgrade_percge**]() | **GET** /v1/upgrades/sys_version_adoption/sys_version/{sys_version}/_gte/{_gte} | Provides the percentage of ONTAP systems that have been adopted.
*UpgradeRiskCountsApi* | [**upgrade_risk_counts**]() | **GET** /v1/upgrades/riskcount/level/{level}/id/{id} | Provide risks count.
*UpgradeRiskDetailsApi* | [**upgrade_risk_details**]() | **GET** /v1/upgrades/riskdetails/level/{level}/id/{id} | Provides risk details count.
*Upgradev2Api* | [**details**]() | **GET** /v1/upgrades2/details | Provides systems details with recommended version.
*Upgradev2Api* | [**list_ontap**]() | **GET** /v1/upgrades2/ontapversion | Provides list of unique ONTAP version.
*Upgradev2Api* | [**ontap_compat**]() | **POST** /v1/upgrades2/ontap/compatibility | Provides list of compatible ONTAP version.
*Upgradev2Api* | [**upgrade_counts**]() | **GET** /v1/upgrades2/count | Provides systems count, and upgrades count.
*Upgradev2Api* | [**get_upgrade_advisor_by_ontap_id**]() | **GET** /v1/upgrades2/advisor/level/{level}/id/{id}/ontap/{ontap} | Provides the risk summary for a specific ONTAP ID.



## Documentation For Authorization


## CustomAuthorizer

- **Type**: API key
- **API key parameter name**: AuthorizationToken
- **Location**: HTTP header
