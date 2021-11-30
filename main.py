from src.services import *
from src.persons import *


service = PersonService()
person = service.get_person_by_id('99998')

print(person)


