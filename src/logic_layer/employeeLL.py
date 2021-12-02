from src.storage_layer.DLAPI import DLAPI
from src.models.employee import Employee


class EmployeeLL:
    def __init__(self, dlapi):
        self.dlapi = dlapi
    
    def all_employees(self):
        return self.dlapi.get_all_employees()

    def create_new_employee(self, emp):
        self.dlapi.create_new_employee(emp)
    
    def get_employees_that_started_working_before(self, date):
        pass

    def change_employee(self, emp):
        return self.dlapi.change_employee(emp)

    def search_employee_by_id(self, emp):
        return self.dlapi.search_employee_by_id(emp)

    def serch_employee_by_location(self, emp):
        return self.dlapi.search_employee_by_location(emp)

