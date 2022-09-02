import os
import time
import json
import requests
import netapp_activeiq_api

import logging

import csv
from csv import reader
from csv import DictReader

import pandas as pd
from pprint import pprint

from flatten_dict import flatten
from flatten_dict.reducers import make_reducer

# logging.basicConfig(level=os.environ.get("LOGLEVEL", "DEBUG"))


def write2file(filename, data):
    # write json data to file
    with open(filename, "w") as outfile:
        json.dump(data, outfile)


def write2csv(filename, data):
    df = pd.DataFrame(data)
    df.to_csv(filename)

def add_extra_data(sl, data):
    rsl = []
    for d in sl:
        d.update(data)
        rsl.append(d)
    return rsl

def clean_data(data, fields=None):
    """
    FIELDS = ['list of keys I care about']
    """
    table = pd.DataFrame()
    pprint(data)
    pprint(len(data))
    for i in range(len(data) - 1):
        df = pd.json_normalize(data[i + 1])
        if fields:
            df = df[fields]
        table = pd.concat([table, df])
    return table


if __name__ == "__main__":

    # source = "https://aiq.netapp.com"
    accesstoken = input("Enter Access Token: ")
    refreshtoken = input("Enter Refresh Token: ")

    aiq = netapp_activeiq_api.ActiveIQClient(
        refresh_token=refreshtoken, access_token=accesstoken
    )

    # aiq.get_refresh_token()

    cl = aiq.SystemApi.get_list_by_level("customer")
    customers = cl["customers"]["list"]
    pprint(customers)
    write2file("/home/wouter/netapp/customers.json", customers)
    write2csv("/home/wouter/netapp/customers.csv", clean_data(customers))

    with open("/home/wouter/netapp/customers.csv", "r") as read_obj:
        tablesl = pd.DataFrame()
        # pass the file object to DictReader() to get the DictReader object
        csv_dict_reader = DictReader(read_obj)
        # iterate over each line as a ordered dictionary
        for row in csv_dict_reader:
            # row variable is a dictionary that represents a row in csv
            cust_id = row["customer_id"]
            sl = aiq.SystemApi.get_system_details_by_level(level="customer", id=cust_id)
            systems = sl["results"]
            extra_data = {"customer_id": cust_id}
            # systems.update(extra_data)  # add the customer id to the system
            systems = add_extra_data(systems, extra_data)  # add the customer id to the system
            tablesl = pd.concat([tablesl,clean_data(systems)])
        # pprint(tablesl)
        write2csv("/home/wouter/netapp/systems.csv", tablesl)

    with open("/home/wouter/netapp/systems.csv", "r") as read_obj:
        i = 0
        tablesl = pd.DataFrame()
        # pass the file object to DictReader() to get the DictReader object
        csv_dict_reader = DictReader(read_obj)
        # iterate over each line as a ordered dictionary
        for row in csv_dict_reader:
            # row variable is a dictionary that represents a row in csv
            sys_id = row["serial_number"]
            sl = aiq.StorageEfficiencyApi.get_efficiency_details_by_level(
                level="serial_numbers", id=sys_id, source="laptop"
            )
            results = sl["results"]
            extra_data = {"serial_number": sys_id}
            # print(results)
            # print(type(results))
            results = add_extra_data(results, extra_data)  # add the serial number to the efficiency data
            tablesl = pd.concat([tablesl,results], ignore_index=True)
        pprint(tablesl)
        write2csv("/home/wouter/netapp/storage_efficiencies_systems.csv", tablesl)

    with open("/home/wouter/netapp/systems.csv", "r") as read_obj:
        i = 0
        tablesl = pd.DataFrame()
        # pass the file object to DictReader() to get the DictReader object
        csv_dict_reader = DictReader(read_obj)
        # iterate over each line as a ordered dictionary
        for row in csv_dict_reader:
            # row variable is a dictionary that represents a row in csv
            sys_id = row["serial_number"]
            try:
                sl = aiq.ClusterAnalyticsApi.get_resolver(serial_no=sys_id)
            except requests.exceptions.HTTPError:
                if sl.status_code == 504:
                    # Cloud volumes ontap returns a 504 error when requesting the cluster-id
                    pass
                else:
                    raise requests.exceptions.HTTPError
            systems = sl["clusters"]
            # extra_data= {'customer_id': cust_id}
            # systems.update(extra_data) #add the customer id to the system
            tablesl = pd.concat([tablesl, clean_data(systems)])
        # pprint(tablesl)
        write2csv("/home/wouter/netapp/clusters.csv", tablesl)

    with open("/home/wouter/netapp/clusters.csv", "r") as read_obj:
        i = 0
        tablesl = pd.DataFrame()
        # pass the file object to DictReader() to get the DictReader object
        csv_dict_reader = DictReader(read_obj)
        # iterate over each line as a ordered dictionary
        for row in csv_dict_reader:
            # row variable is a dictionary that represents a row in csv
            sys_id = row["clusterUUID"]
            sl = aiq.StorageEfficiencyApi.get_efficiency_details_by_level(
                level="cluster", id=sys_id, source = 'laptop'
            )

            pprint(sl)
            results = sl["results"]
            extra_data = {"cluster_id": sys_id}
            results = add_extra_data(results, extra_data)  # add the serial number to the efficiency data
            tablesl = pd.concat([tablesl, results], ignore_index=True)
        pprint(tablesl)
        write2csv("/home/wouter/netapp/storage_efficiencies_clusters.csv", tablesl)
