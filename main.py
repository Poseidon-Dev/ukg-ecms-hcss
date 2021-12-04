from src import Person
from src import UKG

service = Person.GetPersonByEmployeeIdentifier('99998')
render = service.render()
print(render)

# conn = UKGApi()
# render = conn._post_request('personnel', 'employee-ids')
# print(render)

