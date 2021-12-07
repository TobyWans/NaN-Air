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
        self.login_checker = LogInCheck(self.dlapi)
        self.destinationLL = DestinationLL(self.dlapi)
        self.employeell = EmployeeLL(self.dlapi)
        self.workrequestLL = WorkRequestLL(self.dlapi)
        self.housLL = HousingLL(self.dlapi)
        self.contractormenuLL = ContractorMenuLL(self.dlapi)
        
        # Misc Logic
    def ID_login(self, user_id):
        self.curent_user = user_id
        return self.login_checker.ID_login(self.curent_user)
    
    def login_saver(self, id_num):
        return self.login_checker.login_saver(id_num)
    
    def supervisor_check(self):
        return self.login_checker.supervisor_check()
    
    def clear_console(self):
        clear_cmd = os.system('cls' if os.name in ('nt', 'dos') else 'clear')
        return clear_cmd
    
    def employee_rng_id(self):
        return self.login_checker.employee_rng_id()
    
    def supervisor_rng_id(self):
        return self.login_checker.supervisor_rng_id()
        
        # Destination Logic
    def destination_info(self):
        return self.destinationLL.destination_info()
    
    def get_only_city(self):
        return self.destinationLL.get_only_city()
        
        # Employee Logic
    def create_new_employee(self, new_employee):
        return self.employeell.create_new_employee(new_employee)

    def change_employee(self):
        return self.employeell.change_employee()

    def search_employee_by_id(self, id):
        return self.employeell.search_employee_by_id(id)

    def search_employee_by_location(self):
        return self.employeell.serch_employee_by_location()

    def get_all_employees(self):
        return self.employeell.get_all_employees()
    
    def confirm_emp_login(self, emp_id):
        return self.employeell.confirm_emp_login(emp_id)

    def location_check(self): # returnar location í string Td. 'Svalbard'
        id = self.login_checker.user_id
        return self.employeell.location_check(id)
            
        # Work Request Logic
    def all_open_work_requests(self):
        return self.workrequestLL.all_open_work_requests()
    
    def all_closed_work_requests(self):
        return self.workrequestLL.all_closed_work_requests()
    
    def search_id(self, wr_id):
        return self.workrequestLL.search_id(wr_id)

    def search_des_file_by_city(self, city):
        return self.destinationLL.search_des_file_by_city(city)
    
    def search_date(self, date):
        return self.workrequestLL.search_date(date)
    
    def user_open_requests(self, user_id):
        return self.workrequestLL.user_open_requests(user_id)
    
    def create_new_request(self, req):
        return self.workrequestLL.create_new_request(req)
    
    def finnished_work_req(self):
        return self.workrequestLL.finnished_work_req()
    
    def append_finnished_work_req(self, req):
        return self.workrequestLL.append_finnished_work_req(req)
    
    def open_request(self, wr_id):
        return self.workrequestLL.open_request(wr_id)
    
    def close_request(self, wr_id):
        return self.workrequestLL.close_request(wr_id)
    
    def work_req_count(self):
        return self.workrequestLL.work_req_count()
        
        # Housing Logic
    def add_housing(self, hous):
        return self.housLL.add_housing(hous)

    def change_housing(self, hous):
        return self.housLL.change_housing(hous)
    
    def housing_list(self):
        return self.housLL.housing_list()

    def location_list(self):
        return self.housLL.get_location_list()
    
    def search_by_housing_id(self, entered_id):
        return self.housLL.search_by_housing_id(entered_id)
    
    def get_rental_status(self):
        return self.housLL.get_rental_status()
    
    def get_housing_id_by_location(self, location):
        return self.housLL.get_housing_id_by_location(location)
        
        # Constructor Logic
    def get_contractor_list(self):
        return self.contractormenuLL.get_contractor_list()

    def add_new_contractor(self, Contractor_mdl):
        return self.contractormenuLL.add_new_contractor(Contractor_mdl)

    def sort_contractors_by_location(self, location):
        return self.contractormenuLL.sort_contractors_by_location(location)
