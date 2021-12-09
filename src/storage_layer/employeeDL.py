import csv
import os
from src.models.employee import Employee

class EmployeeDL:
    def __init__(self):
        self.filepath = 'src/data/Employee.csv'
    
    def get_all_employees(self):
        ret_list = []
        with open(self.filepath, newline='', encoding='utf-8') as csvfile:
            reader = csv.DictReader(csvfile)
            for row in reader:
                emp = Employee(**row)
                ret_list.append(emp)
        return ret_list

    def create_new_employee(self, new_employee):
        with open(self.filepath, 'a', newline='', encoding='utf-8') as csvfile:
            fieldnames = ["name", "email", "address", "phone", "mobile", "location", "empid"]
            writer = csv.DictWriter(csvfile, fieldnames=fieldnames)
            writer.writerow({'name': new_employee.name, "email": new_employee.email, "address": new_employee.address, "phone": new_employee.phone, "mobile": new_employee.mobile, "location": new_employee.location, "empid": new_employee.empid})
       
    def change_employee(self,change_employee, emp_id):
        with open('src/data/Employee.csv','r', newline='', encoding='utf-8') as inf, open('src/data/Employee_temp.csv', 'w' ,newline='', encoding='utf-8') as outf:
            reader = csv.reader(inf)
            writer = csv.writer(outf)
            fieldnames = ["name", "email", "address", "phone", "mobile", "location", "empid"]
            for row in reader:
                if row[6] == emp_id:
                    writer = csv.DictWriter(outf, fieldnames=fieldnames)
                    writer.writerow({'name': change_employee.name, "email": change_employee.email, "address": change_employee.address, "phone": change_employee.phone, "mobile": change_employee.mobile, "location": change_employee.location, "empid": emp_id})
                    break
                else:
                    writer.writerow(row)
                writer.writerows(reader)
        os.remove('src/data/Employee.csv')
        os.rename('src/data/Employee_temp.csv', 'src/data/Employee.csv')

    def search_employee_by_location(self, location):
        emp_location = []
        with open(self.filepath, newline='', encoding='utf-8') as csvfile:
            reader = csv.DictReader(csvfile)
            for row in reader:
                if row['location'] == location:
                    emp = Employee(**row)
                    emp_location.append(emp)
        if len(emp_location):
            return emp_location
        else:
            return None
        
    def search_employee_by_ID(self, empid):
        employee_id = []
        with open(self.filepath, newline='', encoding='utf-8') as csvfile:
            reader = csv.DictReader(csvfile)
            for row in reader:
                if row['empid'] == str(empid):
                    emp = Employee(**row)
                    employee_id.append(emp) 
                    return employee_id
        return None
    
    def confirm_emp_login(self, emp_id):
        with open(self.filepath, newline='', encoding='utf-8') as csvfile:
            reader = csv.DictReader(csvfile)
            for row in reader:
                if row['empid'] == emp_id:
                    return True
        return None

    def location_check(self, empid):
        with open(self.filepath, newline='', encoding='utf-8') as csvfile:
            reader = csv.DictReader(csvfile)
            for row in reader:
                if row['empid'] == str(empid):
                    return row['location']

    def get_employee_name(self, user_id):
        with open(self.filepath, newline='', encoding='utf-8') as csvfile:
            reader = csv.DictReader(csvfile)
            for row in reader:
                if row['empid'] == user_id:
                    user_name = row['name']
                    quit
        return user_name