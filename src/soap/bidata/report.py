import re

from src.soap.soap_connection import SoapService
from core.config import *

__all__ = ['UKGReports']

module_service = 'BiDataService'


class BIConn(SoapService):

    service = module_service
    method = 'loginservice'

    @property
    def tokens(self):
        try:
            post = self.post()
            print(post)
            return {
                'token': re.search('<Token>(.*?)</Token>', post).group(1),
                'instance': re.search('<InstanceKey>(.*?)</InstanceKey>', post).group(1),
                'service': re.search('<ServiceId>(.*?)</ServiceId>', post).group(1),
            }
        except AttributeError:
            raise ConnectionError


class UKGReports(BIConn):

    auth_resp = BIConn().tokens
    token = auth_resp['token']
    del auth_resp['token']

    def __init__(self):
        super().__init__()
        self.auth_headers = self.auth_headers | self.auth_resp


class GetReportList(UKGReports):
    service = module_service
    method = 'GetReportList'

    def __init__(self):
        print(self.auth_headers)
        super().__init__()


class GetReportParamaters(UKGReports):
    pass


class ExecuteReport(UKGReports):

    service = module_service
    method = 'executereport'

    def __init__(self, *args, **kwargs):
        self.headers = {'report_path':
                        "/content/folder[@name='zzzCompany Folders']/folder[@name='Arizona Pipeline Company']/folder[@name='UltiPro']/folder[@name='Customs']/folder[@name='GoLive Reports']/report[@name='MASTER']"}
        super().__init__(*args, **kwargs)


class RetrieveReport(UKGReports):
    pass


class RetrieveStream(UKGReports):
    pass


class LogOff(UKGReports):
    pass
