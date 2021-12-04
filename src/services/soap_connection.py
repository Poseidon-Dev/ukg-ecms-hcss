import requests
import inspect

from core.config import *

__all__ = ['SoapService',]

class SoapService:
    """ 
    A class for handling templateing XML SOAP Requests with jijna2 
    """

    service = ''
    method = ''
    headers = {}
    base_headers = {'Content-Type': 'application/soap+xml; charset=utf-8'}


    def __init__(self, *args, **kwargs):
        self.auth_headers = auth_headers
        self.headers = self.headers | self.auth_headers | self.base_headers
        if not self.method:
            self.method = self.__class__.__name__
        if not self.service:
            self.service = inspect.getmro(self.__class__)[1].__name__
                

    @property
    def template_path(self):
        return self.service.lower().replace('service', '') + '/' + self.method.lower() + '.xml'

    
    @property
    def service_url(self):
        return BaseURL + self.service
    

    def template(self):
        """
        Returns a jinja template based on Base values or entered value
        """
        return jin_env.get_template(self.template_path)


    def render(self):
        """
        Base jijna renderer
        """
        return self.template().render(self.headers)
        

    def post(self):
        """
        Base post request
        """
        post = requests.request(
            'POST', 
            self.service_url,
            headers=self.headers, 
            data=self.render()
            ).text
        return post