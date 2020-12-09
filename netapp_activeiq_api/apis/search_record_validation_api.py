# coding: utf-8

from .api_client import ApiClient


class SearchRecordValidationApi:
    def __init__(self, api_client=None):
        if api_client is None:
            api_client = ApiClient()
        self.api_client = api_client

    def search_system_validation_by_level(self, level, **kwargs):  # noqa: E501
        """Validate search record details based on the input provided by the user.  # noqa: E501

         Provides the details of valid and not valid records based on user input.  # noqa: E501
        :param str level: Unique identifier for the level.  (required)
        :param str name: The serial number that is used to validate.
        """

        all_params = ["level", "name"]  # noqa: E501

        params = locals()
        for key, val in params["kwargs"].items():
            if key not in all_params:
                raise TypeError(
                    "Got an unexpected keyword argument '%s'"
                    " to method search_system_validation_by_level" % key
                )
            params[key] = val
        del params["kwargs"]
        # verify the required parameter 'level' is set
        if "level" not in params or params["level"] is None:
            raise ValueError(
                "Missing the required parameter `level` when calling `search_system_validation_by_level`"
            )  # noqa: E501

        path_params = {}
        if "level" in params:
            path_params["level"] = params["level"]  # noqa: E501

        query_params = []
        if "name" in params:
            query_params.append(("name", params["name"]))  # noqa: E501

        header_params = {}

        body_params = None

        return self.api_client.call_api(
            "/v1/search/system/validation/level/{level}",
            "GET",
            path_params,
            query_params,
            header_params,
            body=body_params,
        )
