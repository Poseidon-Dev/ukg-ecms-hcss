from src import Person, services, Login, Job
from src.services.login import LoginService
from src.services import Person

service = Person.GetPersonByEmployeeIdentifier('12799')
print(service.post())
