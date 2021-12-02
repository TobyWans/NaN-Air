from src.logic_layer.login_checker import LogInCheck
from src.logic_layer.destinationLL import DestinationLL
from src.storage_layer.DLAPI import DLAPI
from src.logic_layer.employeeLL import EmployeeLL
from src.logic_layer.work_requestLL import WorkRequestLL
from src.logic_layer.housingLL import HousingLL
from src.logic_layer.contractorsLL import ContractorMenuLL
import os


class LLAPI:
    def __init__(self):
        self.dlapi = DLAPI()
        self.login_checker = LogInCheck()
        self.destinationLL = DestinationLL(self.dlapi)
        self.employeell = EmployeeLL(self.dlapi)
        self.workrequestLL = WorkRequestLL(self.dlapi)
        self.housLL = HousingLL(self.dlapi)
        
    def ID_login(self, id):
        return self.login_checker.ID_login(id)
    
    def supervisor_check(self):
        return self.login_checker.supervisor_check()
    
    def clear_console(self):
        clear_cmd = os.system('cls' if os.name in ('nt', 'dos') else 'clear')
        return clear_cmd

    def destination_info(self):
        return self.destinationLL.destination_info()

    def create_new_employee(self):
        return self.employeell.create_new_employee()

    def change_employee(self):
        pass

    def search_employee_by_id(self):
        pass

    def search_employee_by_location(self):
        pass

    def all_employees(self):
        pass
    
    def all_work_requests(self):
        return self.workrequestLL.all_work_requests()
    
    def create_new_request(self, req):
        return self.workrequestLL.create_new_request(req)

    def add_housing(self, hous):
        return self.housLL.add_housing(hous)
    
    def housing_list(self):
        return self.housLL.housing_list()

    def get_contractor_list(self):
        pass

    def add_new_contractor(self):
        return self.housLL.housing_list()
