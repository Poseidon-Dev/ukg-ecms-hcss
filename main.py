from apps import UKGBaseService
from apps.employee import JobModel, JobService

j = JobService()
response = j.ping()
print(response)