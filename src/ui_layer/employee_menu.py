from src.models.employee import Employee
from src.logic_layer.LLAPI import LLAPI



class EmployeeMenu:
    def __init__(self, llapi: LLAPI):
        self.llapi = llapi
        self.supervisor_options = ["Add employee", "Change employee","Search by ID", "Search by location", "All employees"]
        

    
    def draw_options(self):
        self.llapi.clear_console()
        all_options = []
        all_options.extend(self.supervisor_options)
        for index in all_options:
            print(f"\t{all_options.index(index) + 1}. {index}")
        print("\tR. Return\n")
        return self.prompt_input()


    def prompt_input(self):
        while True:
            command = input("Enter an option: ")
            if command == '1':
                self.create_employee()
            elif command == '2':
                change_employee = self.llapi.change_employee() 
            elif command == '3':
                id = input("Enter employee id: ")
                search_employee_by_id = self.llapi.search_employee_by_id(id) 
                print(search_employee_by_id)
            elif command == '4':
                location = input("Enter location: ")
                search_employee_by_location = self.llapi.search_employee_by_location(location)
                for row in search_employee_by_location:
                    print(row) 
            elif command == '5':
                all_employees = self.llapi.get_all_employees()
                for employee in all_employees:
                    print(employee)
            elif command.lower() == 'r':
                return
            else:
                print("Invalid option, please try again ")
                
    def create_employee(self):
        self.llapi.clear_console()
        emp_id = self.llapi.employee_rng_id()
        print(emp_id)
        name = input("Enter name: ")
        e_mail = input("Enter e-mail: ")
        address = input("Enter address: ")
        phone = input("Enter phone number: ")
        mobile = input("Enter mobile number ")
        location = input("Enter location: ")
        new_employee = Employee(name, e_mail, address, phone, mobile, location, emp_id)
        self.llapi.create_new_employee(new_employee)

    