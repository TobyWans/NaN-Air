from src.models.work_requests import Work_Request
from src.logic_layer.LLAPI import LLAPI
import random
import time

PRIORITY = ('low', 'medium', 'high')

class WorkRequestMenu:
    def __init__(self, llapi: LLAPI):
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
    
    def prompt_input(self):
        while True:
            self.draw_options()
            command = input("\tEnter an option: ")
            if command == '1':
                all_work_requests = self.llapi.all_work_requests()
                for request in all_work_requests:
                    print(request)
                back = input("Press enter to continue")
                self.llapi.clear_console()
            elif command == '2':
                id_input = input("Please enter the ID of your work request: ")
                search_id = self.llapi.search_id(id_input) # bæta við llapi
                print(search_id)
                wait = input("Press enter to contine")
            elif command == '3':
                search_date = self.llapi.search_date() # bæta við llapi
            elif command == '4':
                user_open_requests = self.llapi.user_open_requests() # bæta við llapi
            elif command == '5':
                finished_requests = self.llapi.finnished_work_req() # bæta við llapi
                for request in finished_requests:
                    print(request)
                back = input("Press enter to continue")
                self.llapi.clear_console()
            elif command == '6':
                self.create_new_request()
            elif command == '7':
                open_change_request = self.llapi.open_change_request() # bæta við llapi
            elif command == '8':
                all_work_requests = self.llapi.all_work_requests()
                for request in all_work_requests:
                    print(request)
                close_id = input("Please enter work request ID you want to close: ")
                self.llapi.clear_console()
                close_request = self.llapi.close_request(close_id) # bæta við llapi
            elif command.lower() == 'r':
                self.llapi.clear_console()
                return 'r'
            else:
                print("Invalid option, please try again ")
            
        
    def create_new_request(self):
        work_request_ID = self.llapi.work_req_count()
        print(f"Work request ID: {self.llapi.work_req_count()}")
        title = input("Title: ")
        where = input("Location: ")
        housing = input("Housing: ")
        description = input("Description: ")
        priority = input("Priority: ")
        if priority.lower not in PRIORITY:
            pass
        req = Work_Request(work_request_ID, title, where,  housing, description, priority)
        self.llapi.create_new_request(req)
    
    def close_request(self):
        pass