from src import Person

service = Person.GetPersonByEmployeeIdentifier('99998')
print(service.render())
print('\n')
print(service.post())
print('\n')
print('\n')
update = Person.UpdatePerson('99998', last_name='SomeNewTestLast')
print(update.render())
print('\n')
print(update.post())


# service = Person.GetPersonByEmployeeIdentifier('99998')
# print(service.post())
