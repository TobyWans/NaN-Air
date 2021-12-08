from src.storage_layer.destinationDL import DestinationDL
from src.storage_layer.work_requestDL import WorkRequestDL
from src.storage_layer.housingDL import HousingDL
from src.storage_layer.employeeDL import EmployeeDL
from src.storage_layer.contractorsDL import ContractorMenuDL
from src.storage_layer.login_checkerDL import LoginCheckerDL

class DLAPI:
    def __init__(self):
        self.destDL = DestinationDL()
        self.ReqDL = WorkRequestDL()
        self.housDL = HousingDL()
        self.employee = EmployeeDL()
        self.contractorDL = ContractorMenuDL()
        self.logincheckerDL = LoginCheckerDL()
        
        # Login Checker Logic
    def get_logins(self):
        return self.logincheckerDL.get_logins()
    
    def login_writer(self, id_check):
        return self.logincheckerDL.login_writer(id_check)
                
        # Work Request Logic
    def get_all_open_work_requests(self):
        return self.ReqDL.get_all_open_work_requests()
    
    def get_all_closed_work_requests(self):
        return self.ReqDL.get_all_closed_work_requests()
    
    def search_id(self, user_id):
        return self.ReqDL.search_id(user_id)
    
    def search_date(self, date):
        return self.ReqDL.search_date(date)
    
    def create_new_request(self, req):
        return self.ReqDL.create_new_request(req)
    
    def close_request(self, wr_id):
        return self.ReqDL.close_request(wr_id)
    
    def change_req(self, req_id):
        return self.ReqDL.change_request_prep(req_id)
    
    def open_request(self, wr_id):
        return self.ReqDL.open_request(wr_id)
    
    def work_req_count(self):
        return self.ReqDL.work_req_count()
        
        # Destination Logic
    def destination_info(self):
        return self.destDL.destination_info()
    
    def get_only_city(self):
        return self.destDL.get_only_city()

    def search_des_file_by_city(self, city):
        return self.destDL.search_des_file_by_city(city)
        
        # Employee Logic
    def create_new_employee(self, new_employee):
        return self.employee.create_new_employee(new_employee)

    def change_employee(self):
        return self.employee.change_employee(self)

    def get_all_employees(self):
        return self.employee.get_all_employees()

    def search_employee_by_id(self, id):
        return self.employee.search_employee_by_ID(id)

    def search_employee_by_location(self, location):
        return self.employee.search_employee_by_location(location)
    
    def confirm_emp_login(self, emp_id):
        return self.employee.confirm_emp_login(emp_id)

    def location_check(self, id):
        return self.employee.location_check(id)

    def get_employee_name(self, user_id):
        return self.employee.get_employee_name(user_id)
        
        # Housing Logic
    def add_housing(self, hous):
        return self.housDL.add_housing(hous)
    
    def change_housing(self,hous):
        return self.housDL.change_housing(hous)

    def get_housing_list(self):
        return self.housDL.get_housing_list()

    def get_location_list(self):
        return self.housDL.get_location_list()
    
    def search_by_housing_id(self, entered_id):
        return self.housDL.search_by_housing_id(entered_id)
    
    def get_rental_status(self, user_location):
        return self.housDL.get_rental_status(user_location)
    
    def get_housing_id_by_location(self, location):
        return self.housDL.get_housing_id_by_location(location)
            
        # Constructor Logic
    def get_contractor_list(self):
        return self.contractorDL.get_contractor_list()

    def add_new_contractor(self, contractor_mdl):
        return self.contractorDL.add_new_contractor(contractor_mdl)

    def sort_contractors_by_location(self, location):
        return self.contractorDL.sort_contractors_by_location(location)