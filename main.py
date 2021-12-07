from src import Person, services, Login, Job
from src.services import Person

service = Person.GetPersonByEmployeeIdentifier('99998')
print(service.render())
