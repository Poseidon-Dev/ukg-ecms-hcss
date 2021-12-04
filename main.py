from src import Person
from src import LoginToken

service = Person.UpdatePerson('SomeFirstName', 'SomeLastName', '99998')
render = service.render()

print(render)

