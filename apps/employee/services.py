from apps.services import UKGBaseService

__all__ = ['Person', 'Address', 'Compensation', 'EmploymentInformation', 'Job']

class Person:

    def __init__(self):
        self.service = UKGBaseService('EmployeePerson').operation

    def ping(self):
        return self.service.Ping()

    def fetch_by_id(self):
        return self.service.GetPersonByEmployeeIdentifier()

    def query(self):
        return self.service.FindPeople()

    def update(self):
        return self.service.UpdatePerson()


class Address:

    def __init__(self):
        self.service = UKGBaseService('EmployeeAddress').operation

    def ping(self):
        return self.service.Ping()

    def fetch_by_id(self):
        return self.service.GetAddressByEmployeeIdentifier()

    def query(self):
        return self.service.FindAddresses()

    def update(self):
        return self.service.UpdateAddress()

class Compensation:

    def __init__(self):
        self.service = UKGBaseService('EmployeeCompensation').operation

    def ping(self):
        return self.service.Ping()

    def fetch_by_id(self):
        return self.service.GetCompensationByEmployeeIdentifier()

    def query(self):
        return self.service.FindCompensations()

    def update(self):
        return self.service.UpdateCompensation()


class EmploymentInformation:

    def __init__(self):
        self.service = UKGBaseService('EmploymentInformation').operation

    def ping(self):
        return self.service.Ping()

    def fetch_by_id(self):
        return self.service.GetEmploymentInformationByEmployeeIdentifier()

    def query(self):
        return self.service.FindEmploymentInformations()

    def update(self):
        return self.service.UpdateEmploymentInformation()

    
class Job:

    def __init__(self):
        self.service = UKGBaseService('EmployeeJob').operation

    def ping(self):
        return self.service.Ping()

    def fetch_by_id(self):
        return self.service.GetJobByEmployeeIdentifier()

    def query(self):
        return self.service.FindJobs()

    def update(self):
        return self.service.UpdateJob()