from src.soap.login import UKGSoap
from src.soap.person import models
from src.utils import ReadXML

__all__ = ['GetPersonByEmployeeIdentifier', 'FindPeople', 'UpdatePerson']

module_service = 'employeeperson'

class GetPersonByEmployeeIdentifier(UKGSoap):

    service = module_service

    def __init__(self, employee_id, company_code='APC', *args, **kwargs):
        self.headers = {
            'EmployeeIdentifier': employee_id,
            'CompanyCode': company_code, 
        }
        super().__init__()


    def results(self):
        val = self.post()
        return models.Person(ReadXML(val).results())

class FindPeople(UKGSoap):

    service = module_service

    def __init__(self, page_number='1', page_size='100', *args, **kwargs):
        self.headers = {
            'page_number': page_number,
            'page_size': page_size,
        }
        self.headers = self.headers | {k:v for k,v in kwargs.items()}
        super().__init__(args, kwargs)


class UpdatePerson(UKGSoap):

    service = module_service

    def __init__(self, employee_id, company_code='APC', suppress_ssn='false', *args, **kwargs):
        self.headers = self.headers | { 
            'CompanyCode': company_code, 
            'EmployeeIdentifier': employee_id,
            'suppress_ssn': suppress_ssn
        }
        self.headers = self.headers | {k:v for k,v in kwargs.items()}
        super().__init__(args, kwargs)

    