import requests
import xmltodict

from src.services import SoapService, LoginToken

__all__ = ['GetPersonByEmployeeIdentifier', 'FindPeople', 'UpdatePerson']

class PersonService(SoapService):
    """
    A class for handling the employee person service
    """

    # service = 'employeeperson'

    def __init__(self, *args, **kwargs):
        self.headers = self.headers | {
            # 'Token': LoginToken().token(),
            'Token': '123455',
        }
        super(PersonService, self).__init__()


class GetPersonByEmployeeIdentifier(PersonService):

    def __init__(self, employee_id, company_code='APC', *args, **kwargs):
        self.headers = {
            'EmployeeIdentifier': employee_id,
            'CompanyCode': company_code, 
        }
        super(GetPersonByEmployeeIdentifier, self).__init__(args, kwargs)


class FindPeople(PersonService):

    def __init__(self, page_number=1, page_size=1, *args, **kwargs):
        self.headers = {
            'page_number': page_number,
            'page_size': page_size,
        }
        self.headers = self.headers | {k:v for k,v in kwargs.items()}
        super(FindPeople, self).__init__(args, kwargs)


class UpdatePerson(PersonService):

    def __init__(self, employee_id, *args, **kwargs):
        self.headers = self.headers | { 'EmployeeIdentifier': employee_id }
        super(UpdatePerson, self).__init__(args, kwargs)

    