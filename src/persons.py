import requests
import xmltodict

from src.services import SoapService, LoginService

__all__ = ['PersonById', 'PersonService']

class PersonService(SoapService):
    """
    A class for handling the employee person service
    """

    service = 'employeeperson'

    def __init__(self, *args, **kwargs):
        super(PersonService, self).__init__()
        self.token = LoginService().token()
        self.headers = {
            'Token': self.token,
            'ClientAccessKey': self.auth_headers['ClientAccessKey'],
        }
        self.headers.update(self.base_headers)


    def person(self, person_dict):
        person_dict = xmltodict.parse(person_dict)
        person_dict = person_dict['s:Envelope']['s:Body']['GetPersonByEmployeeIdentifierResponse']['GetPersonByEmployeeIdentifierResult']['Results']
        return person_dict


    def get_person_by_id(self, employee_id, company_code='APC', *args, **kwargs):
        """
        Get person by id UKG service
        """
        template_name = 'persons/getpersonbyid.xml'
        headers = {
            'service_name': 'GetPersonByEmployeeIdentifier',
            'EmployeeIdentifier': employee_id,
            'CompanyCode': company_code,
            }
        headers = headers | self.headers
        data = self.template(template_name).render(headers)
        resp = self.resp(headers, data).replace('b:','')
        return resp
        return self.person(resp)


    
    def find_people(self, page_number='1', page_size='100', **kwargs):
        template_name = 'persons/findpeople.xml'
        headers = {
            'service_name': 'FindPeople',
            'page_number': page_number,
            'page_size': page_size,
        }
        headers = headers | {k:v for k,v in kwargs.items()}
        headers = headers | self.headers
        data = self.template(template_name).render(headers)
        return self.resp(headers, data)

           
    def resp(self, headers, data, req_type="POST"):
        """
        Default response
        """
        return requests.request(req_type, self.service_url, headers=headers, data=data).text


        

    

class PersonById(SoapService):
    """
    A class for handling the employee person service
    """

    template_name = 'persons/getpersonbyid.xml'
    service = 'employeeperson'

    def __init__(self, employee_id, company_code='APC'):
        super(PersonById, self).__init__()
        self.token = LoginService().token()
        self.headers = {
            'EmployeeIdentifier': employee_id,
            'CompanyCode': company_code,
            'Token': self.token,
            'ClientAccessKey': self.auth_headers['ClientAccessKey']
        }
        self.headers.update(self.base_headers)

   
    def render_to_text(self):
        return self.template.render(self.headers)


    def response(self, req_type="POST"):
        return requests.request(req_type, self.service_url, headers=self.headers, data=self.render_to_text()).text


