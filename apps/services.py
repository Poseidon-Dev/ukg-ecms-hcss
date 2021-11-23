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
