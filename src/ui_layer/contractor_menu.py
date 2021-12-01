from src.logic_layer.LLAPI import LLAPI
from src.models.contractors import contractors

class ContractorMenu:
    def __init__(self, llapi):
        self.supervisor_options = ["Add new contractor"]
        self.employee_options = [self.llapi.get_contractor_list()]
        self.llapi = llapi
        self.llapi.ID_login("1111") # Place holder for testing. Veit ekki hvernig user id flakkast á milli klasa...
        self.max_size_list = len(self.employee_options[0])


    def add_new_contractor(self):
        self.llapi.add_new_contractor()   #

    def list_all_contractors(self):
        self.llapi.list_all_contractors() # gera þessi föll í LLAPI?

    def draw_options(self):
        self.llapi.clear_console()
        all_options = []
        all_options.extend(self.employee_options)
        if self.llapi.supervisor_check():
            all_options.extend(self.supervisor_options)
        for index in all_options:
            print(f"\t{all_options.index(index) + 1}. {index}")
        print("\tR. Return\n")

    def prompt_input(self): # listinn herna þarf að vera dynamic. Einhverjar betri aðferðir?
        while True:
            command = input("Enter number: ")
            if command == '1':
                pass
            elif command == '2':
                pass
            elif command.lower() == 'r':
                return
        
        