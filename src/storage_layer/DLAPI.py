from src.storage_layer.destinationDL import DestinationDL
from src.storage_layer.work_requestDL import WorkRequestDL

class DLAPI:
    def __init__(self):
        self.destDL = DestinationDL()
        self.ReqDL = WorkRequestDL()
        
    def get_all_work_requests(self):
        return self.ReqDL.get_all_work_requests()
    
    def create_new_request(self, req):
        return self.ReqDL.create_new_request(req)

    def destination_info(self):
        return self.destDL.destination_info()

    def create_new_employee(self):
        pass

    def change_employee(self):
        pass

    def get_all_employees(self):
        pass

    def search_employee_by_id(self):
        pass

    def search_employee_by_location(self):
        pass
