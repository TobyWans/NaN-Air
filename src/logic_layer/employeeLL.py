from storage_layer.DLAPI import DLAPI
from models.employee import Employee


class EmployeeLL:
    def __init__(self, dlapi):
        self.dlapi = dlapi
    
    def all_employees(self):
        return self.dlapi.get_all_employees()

    def create_employee(self, emp):
        self.dlapi.create_employee(emp)
    
    def get_employees_that_started_working_before(self, date):
        pass

    def change_employee(self, emp):
        return self.dlapi.change_employee(emp)

