from src import Person
from src import LoginToken
from src.rest.conn import UKGApi

# service = Person.UpdatePerson('SomeFirstName', 'SomeLastName', '99998')
# render = service.render()
# print(render)

conn = UKGApi()
render = conn._post_request('personnel', 'employee-ids')
print(render)

