from src.logic_layer.LLAPI import LLAPI
from src.ui_layer.work_request_menu import WorkRequestMenu
from src.ui_layer.employee_menu import EmployeeMenu
from src.ui_layer.destination_menu import DestinationMenu
from src.ui_layer.housing_menu import HousingMenu
import time

class MainMenu:
    def __init__(self):
        self.supervisor_options = ["Employees", "Destination"]
        self.employee_options = ["Work request", "Contractors", "Housing"]
        self.llapi = LLAPI()
        
    def draw_options(self):
        self.llapi.clear_console()
        all_options = []
        all_options.extend(self.employee_options)
        if self.llapi.supervisor_check():
            all_options.extend(self.supervisor_options)
        print(f"\tMenu:")
        for index in all_options:
            print(f"\t{all_options.index(index) + 1}. {index}")
        print("\tQ. Log out\n")
        

        
        
    def prompt_input(self):
        return_option = ''
        while True:
            self.draw_options()
            command = input("\tEnter an option: ")
            
            if command == '1':
                work_request_menu = WorkRequestMenu(self.llapi)
                return_option = work_request_menu.prompt_input()
            elif command == '2':
                contractor_menu = print("here goes the contractor menu")
                # contractor_menu.draw_options()
            elif command == '3':
                housing_menu = HousingMenu(self.llapi)
                return_option = housing_menu.prompt_input()
            elif command == '4' and self.llapi.supervisor_check():
                employee_menu = EmployeeMenu(self.llapi)
                return_option = employee_menu.draw_options()
                # employees_menu.draw_options()
            elif command == '5' and self.llapi.supervisor_check():
                destination_menu = DestinationMenu(self.llapi)
                return_option = destination_menu.draw_options()
            elif command.lower() == 'q':
                return
            else:
                print("Invalid option, please try again ")
            
    def login(self):
        login = input("Enter your ID: ")
        while not self.llapi.ID_login(login):
            print("Invalid ID")
            login = input("Enter your ID: ")