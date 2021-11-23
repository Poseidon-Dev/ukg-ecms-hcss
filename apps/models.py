from core.defaults import *

class APIConfig:

    Token = {
        'ClientAccessKey': ClientAccessKey, 
        'Password': Password, 
        'UserAccessKey': UserAccessKey,
        'UserName': UserName,
    }


class Employee:
    AlternativeEmailAddress = ''
    EmailAddress = ''
    FirstName = ''
    FormerLastName = ''
    LastName = ''
    MiddleName = ''
    PreferredFirstName = ''
    Prefix = ''
    SSN = ''
    Suffix = ''
    SuppressSSN = True
    EmployeeIdentifier = 0