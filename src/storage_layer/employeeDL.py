import csv

from src.models.employee import Employee

class EmployeeDL:
    def __init__(self):
        self.filepath = "csv_files/Employee.csv"
    
    def get_all_employees(self):
        ret_list = []
        with open(self.filepath, newline='', encoding='utf-8') as csvfile:
            reader = csv.DictReader(csvfile)
            for row in reader:
                emp = Employee(row["name"], row["email"],row["address"], row["phone"], row["mobile"], row["location"])
                ret_list.append(emp)
        return ret_list

    def create_new_employee(self, emp):
        with open(self.filepath, 'a', newline='', encoding='utf-8') as csvfile:
            fieldnames = ["name","email","address","phone","mobile", "location"]
            writer = csv.DictWriter(csvfile, fieldnames=fieldnames)
            writer.writerow({'name': emp.name, "email": emp.email, "address": emp.address, "phone": emp.phone, "mobile": emp.mobile, "location": emp.location})
       
    def change_employee(self, emp):
        pass

    def search_employee_by_location(self, emp):
        pass

    def search_employee_by_ID(self, emp):
        pass

