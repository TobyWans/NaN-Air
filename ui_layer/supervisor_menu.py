class SupervisorMenu:
    def __init__(self):
        self.options = """
        1. Work request
        2. Contractors
        3. Housing
        4. Employees
        5. Destination
        Q. Log out
        """
    
    def draw_options(self):
        print(self.options)
        self.prompt_input()
        
        
    def prompt_input(self):
        return_option = ''
        while True:
            command = input("Enter an option: ")
            
            if command == '1':
                work_request_menu = print("here goes the work request menu")
                # return_option = work_request_menu.draw_options()
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
            