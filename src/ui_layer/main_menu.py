from src.logic_layer.LLAPI import LLAPI
from src.ui_layer.work_request_menu import WorkRequestMenu
from src.ui_layer.employee_menu import EmployeeMenu
from src.ui_layer.destination_menu import DestinationMenu
from src.ui_layer.housing_menu import HousingMenu
from src.ui_layer.contractor_menu import ContractorMenu
import time

class MainMenu:
    def __init__(self):
        self.supervisor_options = ["Employees", "Destination"]
        self.employee_options = ["Work request", "Contractors", "Housing"]
        self.llapi = LLAPI()
        self.splash_screen = """_____   __                   ____________        
___  | / /_____ _______      ___    |__(_)_______
__   |/ /_  __ `/_  __ \     __  /| |_  /__  ___/
_  /|  / / /_/ /_  / / /     _  ___ |  / _  /    
/_/ |_/  \__,_/ /_/ /_/      /_/  |_/_/  /_/     
                                                 """
        
        # Prints out the menu and checks if user is supervisor
    def draw_options(self):
        self.llapi.clear_console()
        print(self.splash_screen)
        all_options = []
        all_options.extend(self.employee_options)
        if self.llapi.supervisor_check():
            all_options.extend(self.supervisor_options)
        print("=".center(48, '='))
        print("Main menu".center(48, ' '))
        print("=".center(48, '='))
        print()
        for index in all_options:
            print(f"\t\t{all_options.index(index) + 1}. {index}")
        print("\t\tQ. Log out\n")
        

        
        # Prompt for options
        # to choose what menu you want
    def prompt_input(self):
        return_option = ''
        while True:
            self.draw_options()
            command = input("\tEnter an option: ")
            
            if command == '1':
                work_request_menu = WorkRequestMenu(self.llapi)
                return_option = work_request_menu.prompt_input()
            elif command == '2':
                contractor_menu = ContractorMenu(self.llapi)
                return_option = contractor_menu.prompt_input()
            elif command == '3':
                housing_menu = HousingMenu(self.llapi)
                return_option = housing_menu.prompt_input()
            elif command == '4' and self.llapi.supervisor_check():
                employee_menu = EmployeeMenu(self.llapi)
                return_option = employee_menu.prompt_input()
            elif command == '5' and self.llapi.supervisor_check():
                destination_menu = DestinationMenu(self.llapi)
                return_option = destination_menu.prompt_input()
            elif command.lower() == 'q':
                return
            else:
                print("Invalid option, please try again ")
                time.sleep(1.8)
                
            # Login prompt for user
    def login(self):
        self.llapi.clear_console()
        print(self.splash_screen)
        print("=".center(48, '='))
        print("Please login with your employee ID number".center(48, ' '))
        print("=".center(48, '='))
        print()
        login = input("\tEnter your ID: ")
        while not self.llapi.ID_login(login):
            print("\tInvalid ID")
            time.sleep(1)
            self.llapi.clear_console()
            print(self.splash_screen)
            print("Please login with your employee ID number".center(48, '-'))
            print()
            login = input("\tEnter your ID: ")
        print()
        print("\tLogin successful!")
        time.sleep(1.2)
        return login