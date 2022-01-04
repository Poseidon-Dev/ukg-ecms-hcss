from src import Person
from requests.auth import HTTPBasicAuth

## Serivice POST TEST
service = Person.GetPersonByEmployeeIdentifier('12799')
person = service.results()
print(person)


## REST GET TEST

# code = UKGApi()
# resp = code._get_request()
# print(resp)

# UKGUID = os.getenv('APLBOT')
# UKGPWD = os.getenv('PWD')
# ClientAccessKey = os.getenv('CUSTOMERAPIKEY')
# url = 'https://service5.ultipro.com/configuration/v1/company-details'
# auth = HTTPBasicAuth(UKGUID, UKGPWD)
# headers = {'US-Customer-Api-Key': ClientAccessKey}

# resp = requests.get(url=url, auth=auth, headers=headers)

# print(resp.text)


# resp = ReadXML().results()

# for k,val in resp.items():
#     print(k,': ', val)

# print(resp)