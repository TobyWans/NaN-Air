from src.storage_layer.destinationDL import DestinationDL
from src.storage_layer.work_requestDL import WorkRequestDL
from src.storage_layer.housingDL import HousingDL
from src.storage_layer.employeeDL import EmployeeDL

class DLAPI:
    def __init__(self):
        self.destDL = DestinationDL()
        self.ReqDL = WorkRequestDL()
        self.housDL = HousingDL()
        self.employee = EmployeeDL
        
    def get_all_work_requests(self):
        return self.ReqDL.get_all_work_requests()
    
    def create_new_request(self, req):
        return self.ReqDL.create_new_request(req)

    def destination_info(self):
        return self.destDL.destination_info()

    def create_new_employee(self):
        return self.employee.create_new_employee()

    def change_employee(self):
        return self.employee.change_employee()

    def get_all_employees(self):
        return self.employee.get_all_employees()

    def search_employee_by_id(self):
        return self.employee.search_employee_by_ID()

    def search_employee_by_location(self):
        return self.employee.search_employee_by_location()

    def add_housing(self, hous):
        return self.housDL.add_housing(hous)

    def get_housing_list(self):
        return self.housDL.get_housing_list()