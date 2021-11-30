import requests
import re

from core.config import *

__all__ = ['SoapService', 'LoginService']

class SoapService:
    """ 
    A class for handling templateing XML SOAP Requests with jijna2 
    """

    template_name = ''
    base_headers = {'Content-Type': 'application/soap+xml; charset=utf-8'}
    service = ''
    method = ''

    def __init__(self, *args, **kwargs):
        self.auth_headers = auth_headers
        self.service_url = BaseURL + self.service

    
    def template(self, template_name=''):
        """
        Returns a jinja template based on Base values or entered value
        """
        if template_name:
            return jin_env.get_template(template_name)
        else:
            return jin_env.get_template(self.template_name)
        
    def render_to_text(self):
        """
        Base render taking in the authentication headers
        """
        return self.template().render(self.auth_headers)

    def response(self, req_type="POST"):
        """
        Base response passing data into the service url, adding the headers and renderer
        """
        return requests.request(req_type, self.service_url, headers=self.base_headers, data=self.render_to_text())


class LoginService(SoapService):
    """
    A class for collecting the Authentication Service Token
    """

    template_name = 'loginservice.xml'
    service = 'loginservice'


    def __init__(self, *args, **kwargs):
        super(LoginService, self).__init__()


    def token(self):
        """
        Converts the base response into a single token string
        """
        token_response = re.search(r'<TokenResponse(.*?)</TokenResponse>', self.response().text).group(1)
        return re.search(r'<Token xmlns="http://www.ultipro.com/services/loginservice">(.*?)<', token_response).group(1)

