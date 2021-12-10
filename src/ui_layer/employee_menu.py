from src.models.employee import Employee
from src.logic_layer.LLAPI import LLAPI
import time

from src.ui_layer.housing_menu import INVALID



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
        print("=".center(48, '='))
        print("Employees Menu".center(48, ' '))
        print("=".center(48, '='))
        print()
        for index in all_options:
            print(f"\t\t{all_options.index(index) + 1}. {index}")
        print("\t\tR. Return\n")


    def prompt_input(self):
        while True:
            self.draw_options()
            command = input("\tEnter an option: ")
            if command == '1':
                self.create_employee()
                
                time.sleep(1.8)
            elif command == '2':
                running = True
                emp_id = input("Enter a employee ID: ")
                while running:
                    if self.llapi.confirm_emp_login(emp_id):
                        self.change_employee(emp_id)
                        running = False
                    else:
                        print("No employee with that ID")
                        time.sleep(1.4)
                        self.llapi.clear_console()
                        print(self.splash_screen)
                        print("=".center(48, '='))
                        print("Employees Menu".center(48, ' '))
                        print("=".center(48, '='))
                        print()
                        emp_id = input("Please choose a diffrent ID: ")
                        
                        
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
                running = True
                print("Available locations: ", ' - '.join(self.llapi.location_list()))
                while running:
                    location = input("Enter location: ")
                    search_employee_by_location = self.llapi.search_employee_by_location(location.capitalize())
                    if search_employee_by_location == None:
                        print("Sorry, No employee with that location")
                        location = None
                    else:
                        for row in search_employee_by_location:
                            print(row)
                        running = False
                        input("Press enter to continue")

            elif command == '5':
                all_employees = self.llapi.get_all_employees()
                for employee in all_employees:
                    print(employee)
                input("Press enter to continue")
            elif command.lower() == 'r':
                return
            else:
                print("Invalid option, please try again ")
                time.sleep(1.8)
                
    def create_employee(self):
        self.llapi.clear_console()
        emp_id = self.llapi.employee_rng_id()
        print("Employee ID:", emp_id)
        city = self.llapi.location_check()
        location = city
        name = input("Enter name: ")
        e_mail = None
        while e_mail == None:
            e_mail = input("Enter e-mail: ")
            if '@' not in e_mail:
                print("Incorrect e_mail - '@' is missing! Try again")
                e_mail = None
        address = input("Enter address: ")
        phone_input = None
        while phone_input == None:
            try:
                phone_input = int(input("Enter phone number (without dialling code): "))
                if len(str(phone_input)) < 6:
                    print("Your phone number is to short! Try again")
                    phone_input = None
                elif len(str(phone_input)) > 14:
                    print("Your phone number is to long! Try again")
                    phone_input = None
            except ValueError:
                print(INVALID)
                phone_input =None
        if location == 'Svalbard':
            phone = f'+47 {phone_input}'
        elif location == 'Nuuk':
            phone = f'+299 {phone_input}'
        elif location == 'Faroe Islands':
            phone = f'+298 {phone_input}'
        mobile_input = None
        while mobile_input == None:
            try:
                mobile_input = int(input("Enter mobile number (without dialling code): "))
                if len(str(mobile_input)) < 6:
                    print("Your phone number is to short! Try again")
                    phone_input = None
                elif len(str(mobile_input)) > 14:
                    print("Your phone number is to long! Try again")
                    phone_input = None   
            except ValueError:
                print(INVALID)
                phone_input = None
        mobile = f'+354 {phone_input}'
        confirm = ""
        while confirm != "y" and confirm != "n":
            confirm = input("Confirm? (y/n): ")
            if confirm.lower() == "y":
                new_employee = Employee(name, e_mail, address, phone, mobile, location, emp_id)
                self.llapi.create_new_employee(new_employee)
                print("Employee successfully created")
                time.sleep(1.8)
            elif confirm.lower() == "n":
                return
            else:
                print(INVALID)

    def change_employee(self,emp_id):
        self.llapi.clear_console
        city = self.llapi.location_check()
        location = city
        name = input("Enter name: ")
        e_mail = None
        while e_mail == None:
            e_mail = input("Enter e-mail: ")
            if '@' not in e_mail:
                print("Incorrect e_mail - '@' is missing! Try again")
                e_mail = None
        address = input("Enter address: ")
        phone_input = None
        while phone_input == None:
            try:
                phone_input = int(input("Enter phone number (without dialling code): "))
                if len(str(phone_input)) < 6:
                    print("Your phone number is to short! Try again")
                    phone_input = None
                elif len(str(phone_input)) > 14:
                    print("Your phone number is to long! Try again")
                    phone_input = None
            except ValueError:
                print(INVALID)
                phone_input =None
        if location == 'Svalbard':
            phone = f'+47 {phone_input}'
        elif location == 'Nuuk':
            phone = f'+299 {phone_input}'
        elif location == 'Faroe Islands':
            phone = f'+298 {phone_input}'
        mobile_input = None
        while mobile_input == None:
            try:
                mobile_input = int(input("Enter mobile number (without dialling code): "))
                if len(str(mobile_input)) < 6:
                    print("Your phone number is to short! Try again")
                    phone_input = None
                elif len(str(mobile_input)) > 14:
                    print("Your phone number is to long! Try again")
                    phone_input = None   
            except ValueError:
                print(INVALID)
                phone_input = None
        mobile = f'+354 {phone_input}'
        confirm = ""
        while confirm != "y" and confirm != "n":
            confirm = input("Confirm? (y/n): ")
            if confirm.lower() == "y":
                change_employee = Employee(name, e_mail, address, phone, mobile, location, emp_id)
                self.llapi.change_employee(change_employee, emp_id)
                print(f"Information about employee {emp_id} successfully updated")
                time.sleep(1.8)
            elif confirm.lower() == "n":
                return
            else:
                print(INVALID)