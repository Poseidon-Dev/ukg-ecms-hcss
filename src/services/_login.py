import re

from src.services import SoapService

__all__ = ['LoginToken']

class LoginService(SoapService):
    """
    A class for collecting the Authentication Service Token
    """

    def __init__(self, *args, **kwargs):
        super(LoginService, self).__init__()


class LoginToken(LoginService):

    def __init__(self):
        super(LoginToken, self).__init__()

    
    def token(self):
        """
        Converts the base response into a single token string
        """
        token_response = re.search(r'<TokenResponse(.*?)</TokenResponse>', self.post()).group(1)
        return re.search(r'<Token xmlns="http://www.ultipro.com/services/loginservice">(.*?)<', token_response).group(1)


