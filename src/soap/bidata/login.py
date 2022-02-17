import re

from src.soap.soap_connection import SoapService
from core.config import *

__all__ = ['UKGReportsConn']

module_service = 'BiDataService'

class BIConn(SoapService):

    service = module_service
    method = 'loginservice'

    @property
    def token(self):

        # return 1234
        try:
            return re.search('<Token>(.*?)</Token>', self.post()).group(1)
        except:
            return None
    
class UKGReportsConn(BIConn):

    token = BIConn().token


    