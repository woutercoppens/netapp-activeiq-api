# coding: utf-8

from .api_client import ApiClient


class WellnessApi:
    def __init__(self, api_client=None):
        if api_client is None:
            api_client = ApiClient()
        self.api_client = api_client

    def acknowledge_risk(self, source, **kwargs):  # noqa: E501
        """Acknowledge or Unacknowledge a risk for a number of systems.  # noqa: E501

        Submit a risk acknowledgement or unacknowledgement for set of systems.  # noqa: E501
        :param str source: The source from where this service is being invoked. (required)
        """

        all_params = ["source"]  # noqa: E501

        params = locals()
        for key, val in params["kwargs"].items():
            if key not in all_params:
                raise TypeError(
                    "Got an unexpected keyword argument '%s'"
                    " to method acknowledge_risk" % key
                )
            params[key] = val
        del params["kwargs"]
        # verify the required parameter 'source' is set
        if "source" not in params or params["source"] is None:
            raise ValueError(
                "Missing the required parameter `source` when calling `acknowledge_risk`"
            )  # noqa: E501

        path_params = {}

        query_params = []

        header_params = {}
        if "source" in params:
            header_params["source"] = params["source"]  # noqa: E501

        body_params = None

        return self.api_client.call_api(
            "/v1/wellness/acknowledgeRisk",
            "POST",
            path_params,
            query_params,
            header_params,
            body=body_params,
        )
