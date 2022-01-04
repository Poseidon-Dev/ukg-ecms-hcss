__all__ = ['Person']

class Person:

    def __init__(self, person_dict, *args, **kwargs):
        self.alt_email_address = person_dict['AlternateEmailAddress']
        self.email_address = person_dict['EmailAddress']
        self.company_cde = person_dict['CompanyCode']
        self.employee_number = person_dict['EmployeeNumber']
        self.employee_id = person_dict['EmployeeIdentifier']
        self.first_name = person_dict['FirstName']
        self.former_last_name = person_dict['FormerLastName']
        self.last_name = person_dict['LastName']
        self.middle_name = person_dict['MiddleName']
        self.preferred_first_name = person_dict['PreferredFirstName']
        self.prefix = person_dict['Prefix']
        self.ssn = person_dict['SSN']
        self.self_service_properties = person_dict['SelfServiceProperties']
        self.suffix = person_dict['Suffix']
        self.suppress_ssn = person_dict['SuppressSSN']

    
    def __str__(self):
        return f'{self.employee_number}: {self.first_name} {self.last_name}'