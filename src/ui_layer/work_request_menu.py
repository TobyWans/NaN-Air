from src.logic_layer.LLAPI import LLAPI
import random
import time
from 

PRIORITY = ('low', 'medium', 'high')

class WorkRequestMenu:
    def __init__(self, llapi):
        self.llapi = llapi
        self.supervisor_options = ["Create new request", "Open/Change request", "Close request"]
        self.employee_options = ["All work requests", "Search by ID", "Search by date", "Your open requests", "Finished request"]
    
    def draw_options(self):
        self.llapi.clear_console()
        all_options = []
        all_options.extend(self.employee_options)
        if self.llapi.supervisor_check():
            all_options.extend(self.supervisor_options)
        print("Work Request Menu:")
        for index in all_options:
            print(f"\t{all_options.index(index) + 1}. {index}")
        print("\tR. Return\n")
        return self.prompt_input()
    
    def prompt_input(self):
        while True:
            command = input("\tEnter an option: ")
            if command == '1':
                all_work_requests = self.llapi.all_work_requests() # bæta við llapi
                for request in all_work_requests:
                    print(request)
            elif command == '2':
                search_id = self.llapi.search_id() # bæta við llapi
            elif command == '3':
                search_date = self.llapi.search_date() # bæta við llapi
            elif command == '4':
                user_open_requests = self.llapi.user_open_requests() # bæta við llapi
            elif command == '5':
                finished_requests = self.llapi.finished_requests() # bæta við llapi
            elif command == '6':
                create_new_request = self.llapi.create_new_request() # bæta við llapi
            elif command == '7':
                open_change_request = self.llapi.open_change_request() # bæta við llapi
            elif command == '8':
                close_request = self.llapi.close_request() # bæta við llapi
            elif command.lower() == 'r':
                return 'r'
            else:
                print("Invalid option, please try again ")
        time.sleep(2)
        self.draw_options()
            
        
    def create_new_request(self):
        work_request_ID = print(f"Work request ID: {random.randint(100, 999)}")
        housing = input("Housing: ")
        description = input("Description: ")
        priority = input("Priority: ")
        if priority.lower not in PRIORITY:
            pass
    
    def close_request(self):
        pass