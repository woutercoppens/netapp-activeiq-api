import os
import time
import netapp_activeiq_api

import logging

import var_dump

#from dict_to_csv import extract_header, transform
import csv
import pandas as pd
from pprint import pprint

from flatten_dict import flatten
from flatten_dict.reducer import make_reducer

logging.basicConfig(level=os.environ.get("LOGLEVEL", "DEBUG"))

if __name__ == "__main__":
    # os.environ['OAUTHLIB_INSECURE_TRANSPORT'] = '1'

    accesstoken = input("Enter Access Token: ")
    refreshtoken = input("Enter Refresh Token: ")

    aiq = netapp_activeiq_api.ActiveIQClient(refresh_token=refreshtoken, access_token=accesstoken)

    aiq.get_refresh_token()
    """     customers = aiq.system.list('customer')

    k = customers.keys()
    pprint(k)
 
    # logging.debug(customers)
    v = customers['customers']
    w = v['list']
    pprint(w)
    #data = flatten(w)
    data = w

    # pprint(flatten(customers, reducer=make_reducer(delimiter='_')))
    # k = customers['customers']
    # l = k['list']
    
    # logging.debug(l)
    # # headers = extract_header(l)
    # # output = transform(l)

    df = pd.DataFrame(w)
    # df = pd.concat({k: pd.DataFrame(v).T for k, v in data.items()}, axis=0)
    df.to_csv('/tmp/customers.csv')

    # with open('/tmp/customers.csv', 'w', newline='') as file:
    #     writer = csv.writer(file)
    #     writer.writerows(data) """

    #ca = aiq.CapacityApi.get_capacity_details_by_level_v2(id='651829000005', level='serial_numbers')
    ca = aiq.CapacityApi.get_capacity_trend_details_by_level(id='651829000005', level='serial_numbers', start=1, limit=100)
    pprint(ca)
