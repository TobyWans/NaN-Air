from src.logic_layer.LLAPI import LLAPI



class EmployeeMenu:
    def __init__(self, llapi):
        self.llapi = llapi
        self.supervisor_options = ["Add employee", "Change employee","Search by ID", "Search by location"]
        

    
    def draw_options(self):
        self.llapi.clear_console()
        all_options = []
        all_options.extend(self.supervisor_options)
        for index in all_options:
            print(f"\t{all_options.index(index) + 1}. {index}")
        print("\tQ. Return\n")
        return self.prompt_input()


    def prompt_input(self):
        while True:
            command = input("Enter an option: ")
            if command == '1':
                create_new_employee = self.llapi.create_new_employee() # bæta við llapi
            elif command == '2':
                change_employee = self.llapi.change_employee() # bæta við llapi
            elif command == '3':
                search_employee_by_id = self.llapi.search_employee_by_id() # bæta við llapi
            elif command == '4':
                search_employee_by_location = self.llapi.search_employee_by_location() # bæta við llapi
            elif command == '5':
                all_employees = self.llapi.all_employees() # bæta við í llapi
            elif command.lower() == 'r':
                return
            else:
                print("Invalid option, please try again ")