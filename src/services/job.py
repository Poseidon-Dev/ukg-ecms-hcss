from src.services.soap_connection import SoapService
from src.services.login import LoginToken

__all__ = ['FindJobs', 'GetJobByEmployeeIdentifier', 'UpdateJob']

class JobService(SoapService):
    """
    A class for handlding the job service 
    """
    def __init__(self, *args, **kwargs):
        self.headers = self.headers | {
            'Token': '12345',
            # 'Token': Login.LoginToken(),
        }
        super(JobService, self).__init__()


class FindJobs(JobService):

    def __init__(self):
        self.headers = {}
        super(FindJobs, self).__init__()


class GetJobByEmployeeIdentifier(JobService):

    def __init__(self):
        self.headers = {}
        super(GetJobByEmployeeIdentifier, self).__init__()


class UpdateJob(JobService):

    def __init__(self):
        self.headers = {}
        super(UpdateJob, self).__init__()
