from typing import OrderedDict

class PersonModel:

    def __init__(self, person_dict):
        for k,v in person_dict['Person'].items():
            if isinstance(v, dict):
                for val in v:
                    v = val
                    setattr(self, k, v)

class JobModel:
    
    def __init__(self, employee_id, employee_type, 
                 full_or_part, hourly_or_salary, job_code, 
                 pay_frequency, pay_group, scheduled_hours, 
                 effective_date, agricultural: bool = False,
                 alternative_title=None, date_in_job=None,
                 direct_labor=None, job_group=None, 
                 local_union=None, national_union=None, 
                 org_level1=None, org_level2=None, org_level3=None,
                 org_level4=None, project=None, promotion=None,
                 reason_code=None, seasonal=None, shift_code=None,
                 shift_group=None, supervisor=None, time_clock=None,
                 transfer=None, youth_training=None, 
                 pay_scale_code=None, step_no=None, *args, **kwargs):

        self.employee_id = self._employee_id(employee_id)
        self.employee_type = self._employee_type(employee_type)
        self.full_or_part = self._full_or_part(full_or_part)
        self.hourly_or_salary = self._hourly_or_salary(hourly_or_salary)
        self.job_code = self._job_code(job_code)
        self.pay_frequency = self._pay_frequency(pay_frequency)
        self.pay_group = self._pay_group(pay_group)
        self.scheduled_hours = self._scheduled_hours(scheduled_hours)
        self.effective_date = self._effective_date(effective_date)

        if alternative_title: self.alternative_title = alternative_title
        if date_in_job: self.date_in_job = date_in_job
        if direct_labor: self.direct_labor = direct_labor
        if job_group: self.job_group = job_group
        if local_union: self.local_union = local_union
        if national_union: self.national_union = national_union
        if org_level1: self.org_level1 = org_level1
        if org_level2: self.org_level2 = org_level2
        if org_level3: self.org_level3 = org_level3
        if org_level4: self.org_level4 = org_level4
        if project: self.project = project
        if promotion: self.promotion = promotion
        if reason_code: self.reason_code = reason_code
        if seasonal: self.seasonal = seasonal
        if shift_code: self.shift_code = shift_code
        if shift_group: self.shift_group = shift_group
        if supervisor: self.supervisor = supervisor
        if time_clock: self.time_clock = time_clock
        if transfer: self.transfer = transfer
        if youth_training: self.youth_training = youth_training
        if pay_scale_code: self.pay_scale_code = pay_scale_code
        if step_no: self.step_no = step_no
        if agricultural: self.agricultural = agricultural
        if args: self.args = args
        if kwargs: self.kwargs = kwargs


    def _employee_id(self, id):
        if len(str(id)) != 5:
            raise ValueError(f'{id} is not in the appropriate amount of digits')
        try:
            return int(id)
        except (ValueError, TypeError):
            raise Exception('Cannot cast to integer')
        

    def _employee_type(self, type):
        return type


    def _full_or_part(self, fop):
        if fop.upper() not in ['F', 'P']:
            raise ValueError(f'{fop} is not an allowable value')
        return fop.upper()


    def _hourly_or_salary(self, hos):
        if hos.upper() not in ['H', 'S']:
            raise ValueError(f'{hos} is not an allowable value')
        return hos.upper()


    def _job_code(self, jc):
        return jc


    def _pay_frequency(self, pf):
        return pf


    def _pay_group(self, pg):
        return pg


    def _scheduled_hours(self, sh):
        return sh


    def _effective_date(self, ed):
        return ed

    
    def as_dict(self):
        return vars(self)


    def __str__(self):
        return str(self.as_dict())




# OrderedDict([
#     ('Person', OrderedDict([
#         ('AlternateEmailAddress', OrderedDict([
#             ('@i:nil', 'true')])), 
#         ('EmailAddress', 'testemployee@arizonapipeline.com'), 
#         ('EmployeeIdentifier', OrderedDict([
#             ('@i:type', 'EmployeeNumberIdentifier'), 
#         ('CompanyCode', 'APC'), 
#         ('EmployeeNumber', '99998')])), 
#         ('FirstName', 'Employee'), 
#         ('FormerLastName', OrderedDict([
#             ('@i:nil', 'true')])), 
#         ('LastName', 'TestAPIP'), 
#         ('MiddleName', OrderedDict([
#             ('@i:nil', 'true')])), 
#         ('PreferredFirstName', 'Employee'), 
#         ('Prefix', OrderedDict([
#             ('@i:nil', 'true')])), 
#         ('SSN', '999999997'), 
#         ('SelfServiceProperties', OrderedDict([
#             ('@i:nil', 'true'), 
#         ('@xmlns:c', 'http://schemas.microsoft.com/2003/10/Serialization/Arrays')])), 
#         ('Suffix', OrderedDict([
#             ('@i:nil', 'true')])), 
#         ('SuppressSSN', 'false')]))])