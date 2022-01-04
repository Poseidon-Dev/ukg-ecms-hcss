# from src.services.soap_connection import SoapService
# from src.services.login import LoginService, LoginToken
from src.soap.person import person as Person
from src.soap import login as Login
from src.soap import job as Job

__all__ = ['Person', 'Login', 'Job']
