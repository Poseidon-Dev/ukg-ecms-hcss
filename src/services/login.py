import re

from src.services.soap_connection import SoapService

__all__ = ['UKGSoap']


class LoginService(SoapService):

    service = 'LoginService'
    
    def token(self):
        """
        Converts the base response into a single token string
        """
        return '2345'
        token_response = re.search(r'<TokenResponse(.*?)</TokenResponse>', self.post()).group(1)
        return re.search(r'<Token xmlns="http://www.ultipro.com/services/loginservice">(.*?)<', token_response).group(1)



class UKGSoap(SoapService):

    token = LoginService().token()
