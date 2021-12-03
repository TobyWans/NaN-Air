import csv

from src.models.employee import Employee

class EmployeeDL:
    def __init__(self):
        self.filepath = 'src/data/Employee.csv'
    
    def get_all_employees(self):
        ret_list = []
        with open(self.filepath, newline='', encoding='utf-8') as csvfile:
            reader = csv.DictReader(csvfile)
            for row in reader:
                emp = Employee(row["name"], row["email"], row["address"], row["phone"], row["mobile"], row["location"])
                ret_list.append(emp)
        return ret_list

    def create_new_employee(self, new_employee):
        with open(self.filepath, 'a', newline='', encoding='utf-8') as csvfile:
            fieldnames = ["name", "email", "address", "phone", "mobile", "location"]
            writer = csv.DictWriter(csvfile, fieldnames=fieldnames)
            writer.writerow({'name': new_employee.name, "email": new_employee.email, "address": new_employee.address, "phone": new_employee.phone, "mobile": new_employee.mobile, "location": new_employee.location})
       
    def change_employee(self, emp):
        pass

    def search_employee_by_location(self, emp):
        pass

    def search_employee_by_ID(self, emp):
        pass

