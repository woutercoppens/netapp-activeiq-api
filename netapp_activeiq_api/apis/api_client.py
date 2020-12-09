class ApiClient(object):
    def __init__(self, client, basepath=None):
        self._client = client

    def call_api(self, path=None, *args, **kwargs):
        path = path or []
        return self._client.call_api(path, *args, **kwargs)
