from src.logic_layer.LLAPI import LLAPI


class ContractorMenu:
    def __init__(self):
        self.supervisor_options = ["list imported from LLAPI", "Add new contractor"]
        self.employee_options = ["list imported from LLAPI"]
        self.LLAPI = LLAPI()
        self.LLAPI.ID_login("1234") # Place holder for testing. Veit ekki hvernig user id flakkast á milli klasa...


    def add_new_contractor(self):
        self.LLAPI.add_new_contractor()   #

    def list_all_contractors(self):
        self.LLAPI.list_all_contractors() # gera þessi föll í LLAPI?

    def draw_options(self):
        all_options = []
        all_options.extend(self.employee_options)
        if self.LLAPI.supervisor_check():
            all_options.extend(self.supervisor_options)
        for index in all_options:
            print(f"\t{all_options.index(index) + 1}. {index}")
        print("\tQ. Back\n")

    def prompt_input(self):
        return_option = ''
        while True:
            command = input("Enter number: ")

            if command == '1':
                pass
            elif command == '2':
                pass
            elif command.lower() == 'q':
                return
        
        