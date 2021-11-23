import apps.employee
from apps.employee.models import JobModel, PersonModel
from apps.employee.services import PersonService, CompensationService, AddressService
from apps.services import Login

l = Login()

response = l.Authenticate()

print(response)
