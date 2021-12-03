from src.models.work_requests import Work_Request
from src.logic_layer.LLAPI import LLAPI
from datetime import datetime
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
            command = input("\tEnter an option:\n")
            
            if command == '1': # List all Work Requests
                all_work_requests = self.llapi.all_open_work_requests()
                self.llapi.clear_console()
                print("List of all open work requests:\n")
                for request in all_work_requests:
                    print(request)
                back = input("Press enter to continue")
                self.llapi.clear_console()
                
            elif command == '2': # Search Work Requests by ID
                running = True
                id_input = input("Please enter the ID of your work request: ")
                print()
                while running:
                    search_id = self.llapi.search_id(id_input)
                    if search_id == None:
                        print("Sorry, there are no requests with that ID\n")
                        id_input = input("Please try another ID: ")
                        print()
                    else:
                        print(search_id)
                        running = False
                input("Press enter to contine")
                
            elif command == '3': # Search Work Requests by date
                running = True
                date_input = input("Please enter a date in the format dd/mm/yy\n\t      ")
                while running:
                    search_date = self.llapi.search_date(date_input)
                    if search_date == None:
                        print("Sorry, there is no requests with that date")
                        date_input = input("Please try another date | dd/mm/yy\n\t      ")
                    else:
                        for req in search_date:
                            print(req)
                        running = False
                input("Press enter to contine")
                
            elif command == '4':
                user_open_requests = self.llapi.user_open_requests() # bæta við llapi
                
            elif command == '5': # List Finnished Requests
                finished_requests = self.llapi.all_closed_work_requests()
                self.llapi.clear_console()
                print("List of closed work Requests:\n")
                for request in finished_requests:
                    print(request)
                back = input("Press enter to continue")
                self.llapi.clear_console()
                
            elif command == '6': # Create new Request
                self.create_new_request()
                
            elif command == '7': # Open Request
                all_closed_work_requests = self.llapi.all_closed_work_requests()
                self.llapi.clear_console()
                for request in all_closed_work_requests:
                    print(request)
                open_id = int(input("Please enter work request ID you want to open and change: "))
                self.llapi.clear_console()
                open_change_request = self.llapi.open_request(open_id)
                # while running:
                #     search_id = self.llapi.search_id(id_input)
                #     if search_id == None:
                #         print("Sorry, there are no requests with that ID\n")
                #         id_input = input("Please try another ID: ")
                #         print()
                #     else:
                #         print(search_id)
                #         running = False
                
            elif command == '8': # Close Request
                all_open_work_requests = self.llapi.all_open_work_requests()
                self.llapi.clear_console()
                for request in all_open_work_requests:
                    print(request)
                close_id = int(input("Please enter work request ID you want to close: "))
                self.llapi.clear_console()
                close_request = self.llapi.close_request(close_id)
                
            elif command.lower() == 'r':
                self.llapi.clear_console()
                return 'r'
            else:
                print("Invalid option, please try again ")
                time.sleep(1)
            
        
    def create_new_request(self):
        today = datetime.today()
        day = today.strftime("%d/%m/%y")
        running = True
        work_request_ID = self.llapi.work_req_count()
        print(f"Work request ID: {self.llapi.work_req_count()}")
        title = input("Title: ")
        print("Available Locations:", ' - '.join(self.llapi.get_only_city()))
        where = input("Location: ")
        print("Housing in that area")
        housing = input("Housing: ")
        description = input("Description: ")
        while running:
            priority = input("Priority: ")
            if priority not in PRIORITY:
                print("Please use high, medium or low")
            else:
                running = False
        status = 'Open'
        req = Work_Request(work_request_ID, title, where,  housing, description, priority, status, day)
        self.llapi.create_new_request(req)
    
    def close_request(self):
        pass