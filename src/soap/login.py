import re

from src.soap.soap_connection import SoapService

__all__ = ['UKGSoap']


class LoginService(SoapService):

    service = 'LoginService'
    
    @property
    def token(self):
        """
        Converts the base response into a single token string
        """
        # return '2345'
        # return self.post()
        try:
            token_response = re.search(r'<TokenResponse(.*?)</TokenResponse>', self.post()).group()
            return re.search(r'<Token xmlns="http://www.ultipro.com/services/loginservice">(.*?)<', token_response).group(1)
        except AttributeError:
            token_response = re.search(r'<TokenResponse(.*?)</TokenResponse>', self.post())
            return None

class UKGSoap(SoapService):

    token = LoginService().token
