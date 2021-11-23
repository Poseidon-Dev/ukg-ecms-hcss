import apps.employee
from apps.employee.services import Person, Compensation, Address

p = Person()
c = Compensation()
a = Address()

print(p.ping())
print(c.ping())
print(a.ping())