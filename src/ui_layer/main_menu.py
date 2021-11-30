from src.logic_layer.LLAPI import LLAPI
from src.ui_layer.work_request_menu import WorkRequestMenu


class MainMenu:
    def __init__(self):
        self.supervisor_options = ["Employees", "Destination"]
        self.employee_options = ["Work request", "Contractors", "Housing"]
        self.LLAPI = LLAPI()
        
    def draw_options(self):
        all_options = []
        all_options.extend(self.employee_options)
        if self.LLAPI.supervisor_check():
            all_options.extend(self.supervisor_options)
        for index in all_options:
            print(f"\t{all_options.index(index) + 1}. {index}")
        print("\tQ. Log out\n")
        

        
        
    def prompt_input(self):
        return_option = ''
        while True:
            command = input("\t\tEnter an option: ")
            
            if command == '1':
                work_request_menu = WorkRequestMenu()
                return_option = work_request_menu.draw_options()
            elif command == '2':
                contractor_menu = print("here goes the contractor menu")
                # contractor_menu.draw_options()
            elif command == '3':
                housing_menu = print("here goes the housing menu")
                # housing_menu.draw_options()
            elif command == '4':
                employees_menu = print("here goes the employees menu")
                # employees_menu.draw_options()
            elif command == '5':
                destination_menu = print("here goes the destination menu")
                # destination_menu.draw_options()
            elif command.lower() == 'q':
                return
            else: print("Invalid option, please try again ")
            
            
    def login(self):
        login = input("Enter your ID: ")
        while not self.LLAPI.ID_login(login):
            print("Invalid ID")
            login = input("Enter your ID: ")
            