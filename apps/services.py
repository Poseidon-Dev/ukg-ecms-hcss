import zeep
from core.defaults import *
from apps.models import APIConfig

__all__ = ['UKGBaseService']

class UKGBaseService:

    def __init__(self, service):
        self.service = service

    @property
    def wsdl(self):
        return BaseURL + self.service 

    @property
    def settings(self):
        return zeep.Settings(extra_http_headers=APIConfig.Token)

    @property
    def client(self):
        return zeep.Client(wsdl=self.wsdl, settings=self.settings)

    @property
    def operation(self):
        return self.client.service

class Login:

    def __init__(self):
        self.service = UKGBaseService('LoginService').operation

    def Authenticate(self):
        return self.service.Authenticate()

    def fetch_by_id(self):
        return self.service.GetJobByEmployeeIdentifier()

    def query(self):
        return self.service.FindJobs()

    def update(self):
        return self.service.UpdateJob()
