from src import Person

service = Person.GetPersonByEmployeeIdentifier('99998')
render = service.render()

print(render)

