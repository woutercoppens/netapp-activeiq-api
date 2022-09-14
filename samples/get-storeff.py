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

def add_extra_data(data, extra_data):
    if isinstance(data, pd.DataFrame):
        for k, v in extra_data.items():
            data[k] = v
        table = data
    
    elif isinstance(data, dict):
        data.update(extra_data)
        table = pd.DataFrame([data])

    elif isinstance(data, list):
        new_data = []
        for i in data:
            i.update(extra_data)
            new_data.append(i)
        table = pd.DataFrame.from_records(new_data)

    pprint(table)
    return table

def clean_data(data, fields=None):
    """
    FIELDS = ['list of keys I care about']
    """
    table = pd.DataFrame()
    # pprint(data)
    # pprint(len(data))
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
            try:
                sl = aiq.SystemApi.get_system_details_by_level(level="customer", id=cust_id)
                # print(sl)
            except requests.exceptions.HTTPError as exc:
                pass
                # if exc.response.status_code == 504:
                #     # returns a 504 error: time out
                #     pass
                # else:
                #     raise requests.exceptions.HTTPError
            systems = sl["results"]
            extra_data = {"customer_id": cust_id}
            # systems.update(extra_data)  # add the customer id to the system
            # print(systems)
            # print(type(systems))
            systems = clean_data(systems)
            systems = add_extra_data(systems, extra_data)  # add the customer id to the system
            pprint(systems)
            tablesl = pd.concat([tablesl,systems])
            pprint(tablesl)
        write2csv("/home/wouter/netapp/systems.csv", tablesl)

    with open("/home/wouter/netapp/systems.csv", "r") as read_obj:
        i = 0
        tables2 = pd.DataFrame()
        # pass the file object to DictReader() to get the DictReader object
        csv_dict_reader = DictReader(read_obj)
        # iterate over each line as a ordered dictionary
        for row in csv_dict_reader:
            # row variable is a dictionary that represents a row in csv
            sys_id = row["serial_number"]
            try: 
                sl = aiq.StorageEfficiencyApi.get_efficiency_details_by_level(
                    level="serial_numbers", id=sys_id, source="laptop"
                )
                print(sl)
            except requests.exceptions.HTTPError:
                pass
                # if sl.status_code == 504:
                #     # returns a 504 error: time out
                #     pass
                # else:
                #     raise requests.exceptions.HTTPError
            results = sl["results"]
            extra_data = {"serial_number": sys_id}
            # pprint(results)
            results = add_extra_data(results, extra_data)  # add the serial number to the efficiency data
            print(results)
            tables2 = pd.concat([tables2,results], ignore_index=True)
            print(tables2)
        write2csv("/home/wouter/netapp/storage_efficiencies_systems.csv", tables2)
    
    with open("/home/wouter/netapp/systems.csv", "r") as read_obj:
        i = 0
        tables3 = pd.DataFrame()
        # pass the file object to DictReader() to get the DictReader object
        csv_dict_reader = DictReader(read_obj)
        # iterate over each line as a ordered dictionary
        for row in csv_dict_reader:
            # row variable is a dictionary that represents a row in csv
            sys_id = row["serial_number"]
            try:
                sl = aiq.ClusterAnalyticsApi.get_resolver(serial_no=sys_id)
                print(sl)
            except requests.exceptions.HTTPError:
                pass
                # if sl.status_code == 504:
                #     # Cloud volumes ontap returns a 504 error when requesting the cluster-id
                #     pass
                # else:
                #     raise requests.exceptions.HTTPError
            try:
                systems = sl["clusters"]
            except KeyError:
                pass
            # extra_data= {'customer_id': cust_id}
            # systems.update(extra_data) #add the customer id to the system
            systems = clean_data(systems)
            tables3 = pd.concat([tables3, systems])
        # pprint(tables3)
        write2csv("/home/wouter/netapp/clusters.csv", tables3)

    with open("/home/wouter/netapp/clusters.csv", "r") as read_obj:
        i = 0
        tables4 = pd.DataFrame()
        # pass the file object to DictReader() to get the DictReader object
        csv_dict_reader = DictReader(read_obj)
        # iterate over each line as a ordered dictionary
        for row in csv_dict_reader:
            # row variable is a dictionary that represents a row in csv
            sys_id = row["clusterUUID"]
            try:
                sl = aiq.StorageEfficiencyApi.get_efficiency_details_by_level(
                    level="cluster", id=sys_id, source = 'laptop'
                )
                pprint(sl)
            except requests.exceptions.HTTPError:
                pass
            results = sl["results"]
            extra_data = {"cluster_id": sys_id}
            results = add_extra_data(results, extra_data)  # add the serial number to the efficiency data
            tables4 = pd.concat([tables4, results], ignore_index=True)
        pprint(tables4)
        write2csv("/home/wouter/netapp/storage_efficiencies_clusters.csv", tables4)
    