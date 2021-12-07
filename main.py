from src import Person, services, Login, Job
from src import UKG

from src.services.soap_connection import SoapService

service = Person.GetPersonByEmployeeIdentifier('99998')
print(service.post())
