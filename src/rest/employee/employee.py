import json
import requests
from src.rest.conn import UKGApi
from src.rest.employee import models

from jsondiff import diff
from deepdiff import DeepDiff
from pprint import pprint


__all__ = ['EmployeeLookup', 'EmployeeChanges', 'Employees']


class EmployeeChanges(UKGApi):

    module = 'personnel'
    method = 'employee-changes'


    def _post_request(self, version='v1', data=None, *args, **kwargs):
        url = f'{self.base_url}{self.module}/{version}/{self.method}'
        if data:
            data = json.dumps(data)
        base = {'url': url, 'data': data}
        page = 1
        record_check = 1
        all_results = []
        while record_check >= 1:
            discover = requests.get(url=base['url'], auth=self.auth, headers=self.headers, params={'page': page, 'per_page': 200}).json()
            all_results.extend(discover)
            record_check = len(discover)
            page += 1
            
        with open('results.json', 'w') as out:
            json.dump(all_results, out)

        return all_results


    def diffs(self):
        f1 = json.load(open('src/rest/employee/response.json', 'r'))
        f2 = json.load(open('src/rest/employee/response2.json', 'r'))

        
        # diffs = DeepDiff(f1, f2, ignore_order=True, indent=2).to_json()
        return f1




class Employees:


    @staticmethod
    def employee_test():
        f1 = open('src/rest/employee/results.json')
        f2 = open('src/rest/employee/results2.json')
        data1 = json.load(f1)
        data2 = json.load(f2)

        records1 = [models.Employee(e) for e in data1]
        records2 = [models.Employee(e) for e in data2]


        return (records1, records2)

class EmployeeLookup(UKGApi):

    module = 'personnel'
    method = 'employee-ids'

    def __init__(self, id_val, id_type='Employee Number', company_id_type='Company Name', company_id_val='APC'):
        self._identifiers = [{
        'employeeIdentifierType': id_type,
        'employeeIdentifierValue': id_val,
        'companyIdentifierType': company_id_type,
        'companyIdentifierValue': company_id_val,
        }]
        super().__init__()


    # @property
    # def identifiers(self):
    #     return json.dumps(self._identifiers)


    def post(self, *args, **kwargs):
        self.resp = requests.post(
            url='https://service5.ultipro.com/personnel/v1/employee-ids?employeeIdentifierType=Employee%20Number&employeeIdentifierValue=12799&companyIdentifierType=Company%20Name&companyIdentifierValue=APC',
            auth=self.auth,
            headers=self.headers)
        # self.resp = self._post_request(self.module, self.method, self.version, params=self._identifiers)
        print(self.resp.request.url)
        print(self.resp.request.headers)
        return self.resp
