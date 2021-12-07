from src.services.soap_connection import SoapService
from src.services.login import UKGSoap

__all__ = ['GetPersonByEmployeeIdentifier', 'FindPeople', 'UpdatePerson']

module_service = 'PersonService'

auth_token = '1234'


class GetPersonByEmployeeIdentifier(UKGSoap):

    service = module_service

    def __init__(self, employee_id, company_code='APC', *args, **kwargs):
        self.headers = {
            'EmployeeIdentifier': employee_id,
            'CompanyCode': company_code, 
        }
        super().__init__()



class FindPeople(UKGSoap):

    service = module_service

    def __init__(self, page_number=1, page_size=1, *args, **kwargs):
        self.headers = {
            'page_number': page_number,
            'page_size': page_size,
        }
        self.headers = self.headers | {k:v for k,v in kwargs.items()}
        super().__init__(args, kwargs)


class UpdatePerson(UKGSoap):

    service = module_service

    def __init__(self, first_name, last_name, employee_id, *args, **kwargs):
        self.headers = self.headers | { 
            'EmployeeIdentifier': employee_id,
            'FirstName': first_name,
            'LastName': last_name }
        self.headers = self.headers | {k:v for k,v in kwargs.items()}
        super().__init__(args, kwargs)

    