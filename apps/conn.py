import requests
from requests.api import request
from requests.auth import HTTPBasicAuth
import zeep

# from core.defaults import *

WSDL_URL = 'https://service5.ultipro.com/services/EmployeeUserDefinedFields?wsdl=wsdl0'
METHOD_URL = 'https://service5.ultipro.com/services/EmployeeUserDefinedFields'
SERVICE_URL = ''




# header = zeep.xsd.Element(
#     "Header",
#     zeep.xsd.ComplexType(

#     )
# )


url = 'https://service5.ultipro.com/services/EmployeeUserDefinedFields'

class UKGConn:

    def __init__(self):
        self.auth = HTTPBasicAuth(UID, PWD)


# wsdl = BaseURL + 'loginservice'

# auth_headers = {
#         'ClientAccessKey': ClientAccessKey, 
#         'Password': Password, 
#         'UserAccessKey': UserAccessKey,
#         'UserName': UserName,
#         }

# settings = zeep.Settings(extra_http_headers=auth_headers)
# client = zeep.Client(wsdl=wsdl, settings=settings)
# response = client.service.Authenticate()
# print(response)

# wsdl = BaseURL + 'EmployeePerson'
# client = zeep.Client(wsdl=wsdl, settings=settings)

# ping = client.service.Ping()
# print(ping)

# response = client.service.GetPersonByEmployeeIdentifier(token['Token'])
# print(response)

from core.defaults import *
from apps.models import APIConfig

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

class EmployeePersonService:

    def __init__(self):
        self.service = UKGBaseService('EmployeePerson').operation

    def ping(self):
        return self.service.Ping()

    def fetch_by_id(self):
        return self.service.GetPersonByEmployeeIdentifier()

    def person_search(self):
        return self.service.FindPeople()

    def update_person(self):
        return self.service.UpdatePerson()

    



# ukg = UKGService('EmployeePerson')

# ping = ukg.client.Ping()
# print(ping)

class UKGApi(APIConfig):


    def __init__(self):
        self.base_url = BaseURL

    def headers(self):
        return 
        
    def service(self, service):
        return self.base_url + service

    def method(self, service, method):
        pass


    def authenticate(self):
        """
        Validates authentication with the server
        """
        pass

    def auth_token(self):
        """
        Returns the authentication token upon successful authentication
        """
        pass

    def _get_request(self):
        """
        Default get method
        """
        pass

    def _post_request(self):
        """
        Default post method
        """
        pass

    def _update_request(self):
        """
        Default update method
        """
        pass