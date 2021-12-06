from src.storage_layer.DLAPI import DLAPI
from src.models.employee import Employee


class EmployeeLL:
    def __init__(self, dlapi: DLAPI):
        self.dlapi = dlapi
    
    def get_all_employees(self):
        return self.dlapi.get_all_employees()

    def create_new_employee(self, new_employee):
        return self.dlapi.create_new_employee(new_employee)
    
    def get_employees_that_started_working_before(self, date):
        pass

    def change_employee(self):
        return self.dlapi.change_employee(self)

    def search_employee_by_id(self):
        return self.dlapi.search_employee_by_id(self)

    def serch_employee_by_location(self):
        return self.dlapi.search_employee_by_location(self)
    
    def confirm_emp_login(self, emp_id):
        return self.dlapi.confirm_emp_login(emp_id)

    def location_check(self, id):
        return self.dlapi.location_check(id)