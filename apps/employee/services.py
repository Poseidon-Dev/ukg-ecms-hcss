from apps.services import UKGBaseService

__all__ = ['PersonService', 
           'AddressService', 
           'CompensationService', 
           'EmploymentInformationService', 
           'JobService', 
           'NewHireService', 
           'ContactsService',
           ]

class PersonService:

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


class AddressService:

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
        

class CompensationService:

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


class EmploymentInformationService:

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

    
class JobService:

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


class NewHireService:

    def __init__(self):
        self.service = UKGBaseService('EmployeeNewHire').operation

    def ping(self):
        return self.service.Ping()

    def create(self):
        return self.service.NewHireUsa()



class ContactsService:

    def __init__(self):
        self.service = UKGBaseService('EmployeeContacts').operation

    def ping(self):
        return self.service.Ping()

    def fetch_by_id(self):
        return self.service.GetContactByEmployeeIdentifier()

    def fetch_by_contact_id(self):
        return self.service.GetEmployeeContactByContactId()

    def query(self):
        return self.service.FindContacts()

    def update(self):
        return self.service.UpdateContact()

