from src.services.soap_connection import SoapService
from src.services.login import LoginToken

__all__ = ['GetPersonByEmployeeIdentifier', 'FindPeople', 'UpdatePerson']

class PersonService(SoapService):
    """
    A class for handling the employee person service
    """
    def __init__(self, *args, **kwargs):
        self.headers = self.headers | {
            # 'Token': LoginToken().token(),
            'Token': '123455',
        }
        super().__init__()


class GetPersonByEmployeeIdentifier(PersonService):

    def __init__(self, employee_id, company_code='APC', *args, **kwargs):
        self.headers = {
            'EmployeeIdentifier': employee_id,
            'CompanyCode': company_code, 
        }
        super().__init__(args, kwargs)


class FindPeople(PersonService):

    def __init__(self, page_number=1, page_size=1, *args, **kwargs):
        self.headers = {
            'page_number': page_number,
            'page_size': page_size,
        }
        self.headers = self.headers | {k:v for k,v in kwargs.items()}
        super().__init__(args, kwargs)


class UpdatePerson(PersonService):

    def __init__(self, first_name, last_name, employee_id, *args, **kwargs):
        self.headers = self.headers | { 
            'EmployeeIdentifier': employee_id,
            'FirstName': first_name,
            'LastName': last_name }
        self.headers = self.headers | {k:v for k,v in kwargs.items()}
        super().__init__(args, kwargs)

    