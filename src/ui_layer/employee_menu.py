from src.models.employee import Employee
from src.logic_layer.LLAPI import LLAPI
import time



class EmployeeMenu:
    def __init__(self, llapi: LLAPI):
        self.llapi = llapi
        self.supervisor_options = ["Add employee", "Change employee","Search by ID", "Search by location", "All employees"]
        self.splash_screen = """_____   __                   ____________        
___  | / /_____ _______      ___    |__(_)_______
__   |/ /_  __ `/_  __ \     __  /| |_  /__  ___/
_  /|  / / /_/ /_  / / /     _  ___ |  / _  /    
/_/ |_/  \__,_/ /_/ /_/      /_/  |_/_/  /_/     
                                                 """
        

    
    def draw_options(self):
        self.llapi.clear_console()
        print(self.splash_screen)
        all_options = []
        all_options.extend(self.supervisor_options)
        print("Menu".center(48, '-'))
        for index in all_options:
            print(f"\t\t{all_options.index(index) + 1}. {index}")
        print("\t\tR. Return\n")


    def prompt_input(self):
        while True:
            self.draw_options()
            command = input("\tEnter an option: ")
            if command == '1':
                self.create_employee()
                print("Employee successfully created")
                time.sleep(1.8)
            elif command == '2':
                change_employee = self.llapi.change_employee() 
            elif command == '3':
                emp_id = input("Enter employee id: ")
                running = True
                if emp_id.lower() == 'r':
                    running = False
                while running:
                    search_employee_by_id = self.llapi.search_employee_by_id(emp_id) 
                    if search_employee_by_id == None:
                        print("There is no employee with that ID")
                    else:
                        for row in search_employee_by_id:
                            print(row)
                    emp_id = input("Search for another ID or type R to return: ")
                    if emp_id.lower() == 'r':
                        running = False

            elif command == '4':
                print("Available locations: ", ' - '.join(self.llapi.location_list()))
                location = input("Enter location: ")
                search_employee_by_location = self.llapi.search_employee_by_location(location.lower)
                for row in search_employee_by_location:
                    print(row)
                print("Press enter to continue")
                time.sleep(1.8)

            elif command == '5':
                all_employees = self.llapi.get_all_employees()
                for employee in all_employees:
                    print(employee)
                input("Press enter to continue")
            elif command.lower() == 'r':
                return
            else:
                print("Invalid option, please try again ")
                
    def create_employee(self):
        self.llapi.clear_console()
        emp_id = self.llapi.employee_rng_id()
        print("Employee ID:", emp_id)
        name = input("Enter name: ")
        e_mail = input("Enter e-mail: ")
        address = input("Enter address: ")
        phone = input("Enter phone number: ")
        mobile = input("Enter mobile number ")
        print("Available locations: ", ' - '.join(self.llapi.location_list()))
        location = input("Enter location: ")
        new_employee = Employee(name, e_mail, address, phone, mobile, location, emp_id)
        self.llapi.create_new_employee(new_employee)

    