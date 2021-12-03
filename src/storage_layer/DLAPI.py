from src.storage_layer.destinationDL import DestinationDL
from src.storage_layer.work_requestDL import WorkRequestDL
from src.storage_layer.housingDL import HousingDL
from src.storage_layer.employeeDL import EmployeeDL

class DLAPI:
    def __init__(self):
        self.destDL = DestinationDL()
        self.ReqDL = WorkRequestDL()
        self.housDL = HousingDL()
        self.employee = EmployeeDL()
                
        # Work Request Logic
    def get_all_open_work_requests(self):
        return self.ReqDL.get_all_open_work_requests()
    
    def get_all_closed_work_requests(self):
        return self.ReqDL.get_all_closed_work_requests()
    
    def search_id(self, user_id):
        return self.ReqDL.search_id(user_id)
    
    def create_new_request(self, req):
        return self.ReqDL.create_new_request(req)
    
    def close_request(self, wr_id):
        return self.ReqDL.close_request(wr_id)
    
    def open_request(self, wr_id):
        return self.ReqDL.open_request(wr_id)
    
    def finnished_work_req(self):
        return self.ReqDL.finnished_work_req()
    
    def append_finnished_work_req(self, req):
        return self.ReqDL.append_finnished_work_req(req)
    
    def work_req_count(self):
        return self.ReqDL.work_req_count()
        
        # Destination Logic
    def destination_info(self):
        return self.destDL.destination_info()
    
    def get_only_city(self):
        return self.destDL.get_only_city()
        
        # Employee Logic
    def create_new_employee(self, new_employee):
        return self.employee.create_new_employee(self, new_employee)

    def change_employee(self):
        return self.employee.change_employee(self)

    def get_all_employees(self):
        return self.employee.get_all_employees()

    def search_employee_by_id(self):
        return self.employee.search_employee_by_ID(self)

    def search_employee_by_location(self):
        return self.employee.search_employee_by_location(self)
        
        # Housing Logic
    def add_housing(self, hous):
        return self.housDL.add_housing(hous)

    def get_housing_list(self):
        return self.housDL.get_housing_list()
    
    def search_by_housing_id(self, entered_id):
        return self.housDL.search_by_housing_id(entered_id)
            
        # Constructor Logic