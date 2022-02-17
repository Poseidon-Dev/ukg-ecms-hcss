from distutils.log import Log
from src import Person
from src.utils import ReadXML
from requests.auth import HTTPBasicAuth
import requests
import os
import json
from pprint import pprint


from src.soap.bidata.report import GetReportList

report = GetReportList()

print(report.post())

# from src.rest import EmployeeLookup,  EmployeeChanges, Employees

# resp = Employees.employee_test()



# import time

# start = time.perf_counter()

# hold_changes = []
# for record in resp[0]:
#     for new_record in resp[1]:
#         if record == new_record:
#             changes = record.diffs(new_record)
#             if changes:
#                 hold_changes.append(changes)

# elapsed_time = time.perf_counter() - start
# print(elapsed_time)

# for change in hold_changes:
#     for k,v in change.items():
#         if k == 'employee':
#             print(k, ': ', v)
#         if k == 'changes':
#             print('\t', k, ': ', v)







# UKGUID = os.getenv('UID')
# UKGPWD = os.getenv('PWD')
# ClientAccessKey = os.getenv('CUSTOMERAPIKEY')
# url = 'https://service5.ultipro.com/configuration/v1/company-details'
# auth = HTTPBasicAuth(username=UKGUID, password=UKGPWD)
# headers = {'US-Customer-Api-Key': ClientAccessKey}

# resp = requests.get(url=url, auth=auth, headers=headers)

# print(resp.text)
