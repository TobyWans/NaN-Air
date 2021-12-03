from src.logic_layer.LLAPI import LLAPI
from src.models.contractors import contractors
import time

class ContractorMenu:
    def __init__(self, llapi):
        self.llapi = llapi
        self.list_of_contractors = self.llapi.get_contractor_list()
        self.supervisor_options = ["Add new contractor"]
        self.employee_options = self.list_of_contractors

    def add_new_contractor(self):
        self.llapi.clear_console()
        contractor = input("Enter contractor: ")
        name = input("Enter name: ")
        profession = input("Enter profession: ")
        phone = input("Enter phone: ")
        opening_hours = input("Enter opening hours: ")
        location = input("Enter location: ")
        rating = input("Enter rating: ")
        contractor_mdl = contractors(contractor, name, profession, phone, opening_hours, location, rating)
        self.llapi.add_new_contractor(contractor_mdl)

    def draw_options(self):
        self.llapi.clear_console()
        self.all_options = []
        self.all_options.extend(self.employee_options)
        if self.llapi.supervisor_check():
            self.all_options.extend(self.supervisor_options)
        print("Contractors Menu")
        for index in self.all_options:
            print(f"\t{self.all_options.index(index) + 1}. {index}")
        print("\tR. Return\n")
        

    def prompt_input(self):
        while True:
            self.draw_options()
            command = input("Enter number: ")
            if self.llapi.supervisor_check() and command == str(self.all_options.index("Add new contractor")+1):
                return self.add_new_contractor()
            elif command.lower() == 'r':
                return
            else:
                try:
                    index = int(command) - 1
                    self.list_of_contractors[index].show_all_info()
                except:
                    print("Invalid option, please try again.")
                    time.sleep(1)
        
        