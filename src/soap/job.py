from src.services.login import UKGSoap

__all__ = ['FindJobs', 'GetJobByEmployeeIdentifier', 'UpdateJob']

module_service = 'JobService'

class FindJobs(UKGSoap):

    service = module_service


class GetJobByEmployeeIdentifier(UKGSoap):

    service = module_service

    def __init__(self):
        self.headers = {}
        super(GetJobByEmployeeIdentifier, self).__init__()



class UpdateJob(UKGSoap):

    service = module_service

    def __init__(self):
        self.headers = {}
        super(UpdateJob, self).__init__()
