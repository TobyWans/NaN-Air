import csv

from models.employee import Employee

class EmployeeDL:
    def __init__(self):
        self.filepath = "csv_files/Employee.csv"
    
    def get_all_employees(self):
        ret_list = []
        with open(self.filepath, newline='', encoding='utf-8') as csvfile:
            reader = csv.DictReader(csvfile)
            for row in reader:
                emp = Employee(row["name"], row["email"],row["address"], row["phone"], row["mobile"])
                ret_list.append(emp)
        return ret_list

    def create_employee(self, emp):
        with open(self.filepath, 'a', newline='', encoding='utf-8') as csvfile:
            fieldnames = ["name","email","address","phone","mobile"]
            writer = csv.DictWriter(csvfile, fieldnames=fieldnames)
            writer.writerow({'name': emp.name, "email": emp.email, "address": emp.address, "phone": emp.phone, "mobile": emp.mobile})
       
    def change_employee():
        pass