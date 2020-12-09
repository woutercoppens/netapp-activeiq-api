import os
import time
import logging
from pprint import pprint

import netapp_activeiq_api

# logging.basicConfig(level=os.environ.get("LOGLEVEL", "DEBUG"))

if __name__ == "__main__":

    atoken = input("Enter Access Token: ")
    rtoken = input("Enter Refresh Token: ")

    aiq = netapp_activeiq_api.ActiveIQClient(refresh_token=rtoken, access_token=atoken)

    # aiq.get_refresh_token()

    ca = aiq.SystemApi.get_list_by_level('customer')
    pprint(ca)
