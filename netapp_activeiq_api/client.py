# -*- coding: utf-8 -*-
# ===============================
#      NetApp ActiveIQ API wrapper
# ===============================
import datetime
import logging

from urllib.parse import urljoin

import requests

# python 2 and python 3 compatibility library
import six
from six import string_types

from cached_property import cached_property

try:
    import simplejson as json
except ImportError:
    import json

from .apis import (
    CapacityApi,
    ClusterAnalyticsApi,
    DataAvailabilityApi,
    DatacenterInsightsApi,
    DiskRemediationApi,
    EfficiencyApi,
    HealthApi,
    InteropSummaryCountApi,
    InteropSummaryDetailsApi,
    PerformanceGraphsApi,
    SearchApi,
    SearchRecordValidationApi,
    StorageEfficiencyApi,
    SupportCasesApi,
    SystemApi,
    SystemListApi,
    UpgradeApi,
    UpgradeDetailsApi,
    UpgradePercgeApi,
    UpgradeRiskCountsApi,
    UpgradeRiskDetailsApi,
    Upgradev2Api,
    ValueReportApi,
    WatchlistApi,
    WellnessApi,
)


# Base API wrapper class
class ActiveIQClient:
    """
    ActiveIQ is wrapper for NetApp ActiveIQ API.
    """

    PRIMITIVE_TYPES = (float, bool, bytes, six.text_type) + six.integer_types
    NATIVE_TYPES_MAPPING = {
        "int": int,
        "long": int,  # Python3 no longer has long
        "float": float,
        "str": str,
        "bool": bool,
        "date": datetime.date,
        "datetime": datetime.datetime,
        "object": object,
    }

    def __init__(self, refresh_token, access_token = None):
        self._base_url = "https://api.activeiq.netapp.com"

        self.cookie = None

        self.default_headers = {
            "Accept": "application/json",
            "Content-Type": "application/json",
        }

        if not refresh_token:
            raise ValueError(
                "Refresh Token must be provided. You can obtain one for free at {}".format(
                    self._base_url
                )
            )

        if refresh_token and not isinstance(refresh_token, string_types):
            raise TypeError("refresh_token parameter must be a string value")

        if access_token and not isinstance(access_token, string_types):
            raise TypeError("access_token parameter must be a string value")

        self.access_token = access_token
        self.refresh_token = refresh_token

    @cached_property
    def CapacityApi(self):
        return CapacityApi(self)

    @cached_property
    def ClusterAnalyticsApi(self):
        return ClusterAnalyticsApi(self)

    @cached_property
    def DataAvailabilityApi(self):
        return DataAvailabilityApi(self)

    @cached_property
    def DatacenterInsightsApi(self):
        return DatacenterInsightsApi(self)

    @cached_property
    def DiskRemediationApi(self):
        return DiskRemediationApi(self)

    @cached_property
    def EfficiencyApi(self):
        return EfficiencyApi(self)

    @cached_property
    def HealthApi(self):
        return HealthApi(self)

    @cached_property
    def InteropSummaryCountApi(self):
        return InteropSummaryCountApi(self)

    @cached_property
    def InteropSummaryDetailsApi(self):
        return InteropSummaryDetailsApi(self)

    @cached_property
    def PerformanceGraphsApi(self):
        return PerformanceGraphsApi(self)

    @cached_property
    def SearchApi(self):
        return SearchApi(self)

    @cached_property
    def StorageEfficiencyApi(self):
        return StorageEfficiencyApi(self)

    @cached_property
    def SystemApi(self):
        return SystemApi(self)

    @cached_property
    def SystemListApi(self):
        return SystemListApi(self)

    @cached_property
    def UpgradeApi(self):
        return UpgradeApi(self)

    @cached_property
    def ValueReportApi(self):
        return ValueReportApi(self)

    @cached_property
    def WatchlistApi(self):
        return WatchlistApi(self)

    @cached_property
    def WellnessApi(self):
        return WellnessApi(self)

    @cached_property
    def SearchRecordValidationApi(self):
        return SearchRecordValidationApi(self)

    @cached_property
    def SupportCasesApi(self):
        return SupportCasesApi(self)

    @cached_property
    def UpgradeDetailsApi(self):
        return UpgradeDetailsApi(self)

    @cached_property
    def UpgradePercgeApi(self):
        return UpgradePercgeApi(self)

    @cached_property
    def UpgradeRiskCountsApi(self):
        return UpgradeRiskCountsApi(self)

    @cached_property
    def UpgradeRiskDetailsApi(self):
        return CapacUpgradeRiskDetailsApiityApi(self)

    @cached_property
    def Upgradev2Api(self):
        return Upgradev2Api(self)
  
    def get_refresh_token(self):
        """Manual refresh."""
        refresh_url = self._url("v1/tokens/accessToken")

        if self.refresh_token is None:
            raise ValueError("ValueError exception: refresh_token is not set.")

        payload = {"refresh_token": self.refresh_token}
        try:
            response = requests.post(
                refresh_url, json=payload, headers=self.default_headers
            )
            response.raise_for_status()

        except requests.exceptions.HTTPError:
            raise requests.exceptions.HTTPError
            exit

        logging.debug(
            "Request to fetch token completed with status %s.", response.status_code
        )
        logging.debug("Request url was %s", response.request.url)
        logging.debug("Request headers were %s", response.request.headers)
        logging.debug("Request body was %s", response.request.body)
        logging.debug(
            "Response headers were %s and content %s.", response.headers, response.text
        )

        if response.status_code == 200:
            logging.debug("Successfully obtained new tokens")
            json_response = response.json()
            logging.debug(json_response)
            if "access_token" in json_response:
                self.access_token= json_response.get("access_token")
                logging.debug("Obtained access_token %s.", self.access_token)

            if "refresh_token" in json_response:
                self.refresh_token = json_response.get("refresh_token")
                logging.debug("Obtained refresh_token %s.", self.refresh_token)
        else:
            logging.error("Error: %s", response.text)
            exit

    def call_api(
        self,
        resource_path,
        method,
        path_params=None,
        query_params=None,
        header_params=None,
        body=None,
        post_params=None,
    ):

        # header parameters
        header_params = header_params or {}
        header_params.update(self.default_headers)

        logging.debug("header_params: %s", header_params)

        if self.cookie:
            header_params["Cookie"] = self.cookie

        if header_params:
            header_params = self.sanitize_for_serialization(header_params)
            header_params = dict(self.parameters_to_tuples(header_params))

        # path parameters
        if path_params:
            path_params = self.sanitize_for_serialization(path_params)
            path_params = self.parameters_to_tuples(path_params)
            for key, value in path_params:
                # specified safe chars, encode everything
                resource_path = resource_path.replace("{%s}" % key, str(value))

        # query parameters
        if query_params:
            query_params = self.sanitize_for_serialization(query_params)
            query_params = self.parameters_to_tuples(query_params)

        # post parameters
        if post_params:
            # post_params = self.prepare_post_parameters(post_params, files)
            post_params = self.sanitize_for_serialization(post_params)
            post_params = self.parameters_to_tuples(post_params)

        # body
        if body:
            body = self.sanitize_for_serialization(body)

        # request url
        url = self._url(resource_path)

        # perform request and return response
        response_data = self.request(
            url,
            method,
            query_params=query_params,
            header_params=header_params,
            body=body,
            post_params=post_params,
        )

        return response_data

    def request(
        self,
        url,
        method,
        query_params=None,
        header_params=None,
        post_params=None,
        body=None,
    ):
        try:
            response = self._raw_request(
                url,
                method,
                query_params=query_params,
                header_params=header_params,
                post_params=post_params,
                body=body,
            )
            response.raise_for_status()

        except requests.exceptions.HTTPError:
            if response.status_code == 401:
                self.get_refresh_token()
                response = self.request(
                    url,
                    method,
                    query_params=query_params,
                    header_params=header_params,
                    post_params=post_params,
                    body=body,
                )
            else:
                raise requests.exceptions.HTTPError
                exit

        return self.__adapt_response_content(response)

    def _url(self, *path):
        url = self._base_url
        for p in path:
            url = urljoin(url, p)
        logging.debug("_url: %s.", url)
        return url

    def _raw_request(
        self,
        url,
        method="GET",
        query_params=None,
        header_params=None,
        post_params=None,
        body=None,
    ):
        header_params = header_params or {}
        header_params["authorizationtoken"] = "%s" % self.access_token

        logging.debug("url: %s", url)
        logging.debug("method: %s", method)
        logging.debug("queryparams: %s", query_params)
        logging.debug("headers: %s", header_params)
        logging.debug("post_params: %s", post_params)
        logging.debug("body: %s", body)

        if method == "GET":
            return requests.get(
                url=url, params=query_params, data=body, headers=header_params
            )

        if method == "POST":
            return requests.post(url=url, data=post_params, headers=header_params)

        # if method == 'PUT':
        #     return requests.put(url=url, json=post_params, headers=header_params)

        # if method == 'PATCH':
        #     return requests.patch(url=url, json=post_params, headers=header_params)

        # if method == 'DELETE':
        #     return requests.delete(url=url, json=post_params, headers=header_params)

        raise ValueError('Unsupported method "%s"' % method)

    def __adapt_response_content(self, response):
        """
        Check if response is a JSON and return it. Otherwise - return raw content
        :param response: Requests response
        :return: {} or raw content
        """
        if response is None:
            return {}

        # in case request() is called recursively, the response is already a dict object
        # so json.loads will fail
        if isinstance(response, dict):
            return response

        try:
            response_body = json.loads(response.text)
        except ValueError:
            return response.text

        return response_body

    def sanitize_for_serialization(self, obj):
        """Builds a JSON POST object.
        If obj is None, return None.
        If obj is str, int, long, float, bool, return directly.
        If obj is datetime.datetime, datetime.date
            convert to string in iso8601 format.
        If obj is list, sanitize each element in the list.
        If obj is dict, return the dict.
        If obj is swagger model, return the properties dict.
        :param obj: The data to serialize.
        :return: The serialized form of data.
        """
        if obj is None:
            return None
        elif isinstance(obj, self.PRIMITIVE_TYPES):
            return obj
        elif isinstance(obj, list):
            return [self.sanitize_for_serialization(sub_obj) for sub_obj in obj]
        elif isinstance(obj, tuple):
            return tuple(self.sanitize_for_serialization(sub_obj) for sub_obj in obj)
        elif isinstance(obj, (datetime.datetime, datetime.date)):
            return obj.isoformat()

        if isinstance(obj, dict):
            obj_dict = obj

        return {
            key: self.sanitize_for_serialization(val)
            for key, val in six.iteritems(obj_dict)
        }

    def parameters_to_tuples(self, params):
        """Get parameters as list of tuples, formatting collections.
        :param params: Parameters as dict or list of two-tuples
        :return: Parameters as list of tuples
        """
        new_params = []
        for k, v in (
            six.iteritems(params) if isinstance(params, dict) else params
        ):  # noqa: E501
            new_params.append((k, v))
        return new_params
