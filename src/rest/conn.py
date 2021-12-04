import requests
from requests.auth import HTTPBasicAuth

from core.defaults import *

class UKGApi:

    def __init__(self):
        self.auth = HTTPBasicAuth(UKGUID, UKGPWD)
        self.headers = {'US-Customer-Api-Key': ClientAccessKey}


    def test_creds(self):
        response = self._get_request("Authorization")
        return response.status_code == 200

    
    def _get_request(self, service, method):
        url = f'{RestURL}/{service}/v1/{method}'
        print(url)
        return requests.get(url, auth=self.auth, headers=self.headers)


    def _post_request(self, service, method):
        url = f'{RestURL}/{service}/v1/{method}'
        print(url)
        return requests.post(url, auth=self.auth, headers=self.headers)

    