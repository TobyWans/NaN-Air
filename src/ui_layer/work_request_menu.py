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
        self.current_user = self.llapi.curent_user
        self.splash_screen = """_____   __                   ____________        
___  | / /_____ _______      ___    |__(_)_______
__   |/ /_  __ `/_  __ \     __  /| |_  /__  ___/
_  /|  / / /_/ /_  / / /     _  ___ |  / _  /    
/_/ |_/  \__,_/ /_/ /_/      /_/  |_/_/  /_/     
                                                 """
    
    def draw_options(self):
        self.llapi.clear_console()
        print(self.splash_screen)
        all_options = []
        all_options.extend(self.employee_options)
        if self.llapi.supervisor_check():
            all_options.extend(self.supervisor_options)
        print("Work Request Menu".center(48, '-'))
        for index in all_options:
            print(f"\t\t{all_options.index(index) + 1}. {index}")
        print("\t\tR. Return\n")
    
    def prompt_input(self):
        while True:
            self.draw_options()
            command = input("\tEnter an option: ")
            print()
            
            if command == '1': # List all Work Requests
                all_work_requests = self.llapi.all_open_work_requests()
                self.llapi.clear_console()
                print("List of all open work requests".center(48, '-'))
                for request in all_work_requests:
                    print(request)
                back = input("Press enter to continue")
                self.llapi.clear_console()
                
            elif command == '2': # Search Work Requests by ID
                running = True
                id_input = input("Please enter the ID of your work request or type r to return: ")
                if id_input == 'r':
                    running = False
                print()
                while running:
                    search_id = self.llapi.search_id(id_input)
                    if search_id == None:
                        print("Sorry, there are no requests with that ID\n")
                        id_input = input("Please try another ID: ")
                        print()
                    else:
                        print(search_id)
                        id_input = input("Enter another ID to search or type r to return: ")
                        self.llapi.clear_console()
                        if id_input == 'r':
                            running = False
                
            elif command == '3': # Search Work Requests by date
                running = True
                date_input = input("Please enter a date in the format dd/mm/yy or type r to return\n\t      ")
                if date_input == 'r':
                    running = False
                while running:
                    search_date = self.llapi.search_date(date_input)
                    if search_date == None:
                        print("Sorry, there is no requests with that date")
                        date_input = input("Please try another date | dd/mm/yy | or type r to return\n\t      ")
                        self.llapi.clear_console()
                        if date_input == 'r':
                            running = False
                    else:
                        for req in search_date:
                            print(req)
                        date_input = input("Enter another date | dd/mm/yy | or type r to return\n\t      ")
                        self.llapi.clear_console()
                        if date_input == 'r':
                            running = False
                
            elif command == '4': # User open Work Requests
                user_req_list = self.llapi.user_open_requests(self.llapi.curent_user)
                if user_req_list != []:
                    for row in user_req_list:
                        print(row)
                input("Press enter to continue")
                    
            elif command == '5': # List Finished Requests
                finished_requests = self.llapi.all_closed_work_requests()
                self.llapi.clear_console()
                print("List of closed work Requests".center(48, '-'))
                for request in finished_requests:
                    print(request)
                back = input("Press enter to continue")
                self.llapi.clear_console()
                
            elif command == '6': # Create new Request
                self.create_new_request()
                print("Work request created successfully".center(48, '-'))
                time.sleep(1.8)
                
            elif command == '7': # Open Request
                running = True
                all_closed_work_requests = self.llapi.all_closed_work_requests()
                self.llapi.clear_console()
                for request in all_closed_work_requests:
                    print(request)
                open_id = input("Please enter work request ID you want to open or R to return: ")
                if open_id.lower() == 'r':
                    running = False
                    open_id = 0
                open_id = int(open_id)
                self.llapi.clear_console()
                while running:
                    open_change_request = self.llapi.open_request(open_id)
                    if open_change_request == None:
                        print("Sorry, there are no requests with that ID\n")
                        time.sleep(1.8)
                        self.llapi.clear_console()
                        all_closed_work_requests = self.llapi.all_closed_work_requests()
                        for request in all_closed_work_requests:
                            print(request)
                        try:
                            open_id = int(input("Please try another ID: "))
                        except ValueError:
                            open_id = None
                        print()
                    elif open_change_request == 69:
                        print("That work request is already open")
                        time.sleep(1.8)
                        self.llapi.clear_console()
                        all_closed_work_requests = self.llapi.all_closed_work_requests()
                        for request in all_closed_work_requests:
                            print(request)
                        open_id = int(input("Please try another ID: "))
                    else:
                        print("Work request successfully changed!".center(48, '-'))
                        time.sleep(1.8)
                        running = False
                
            elif command == '8': # Close Request
                running = True
                all_open_work_requests = self.llapi.all_open_work_requests()
                self.llapi.clear_console()
                for request in all_open_work_requests:
                    print(request)
                close_id = input("Please enter a work request ID you want to close or R to return: ")
                if close_id.lower() == 'r':
                    running = False
                    close_id = 0
                close_id = int(close_id)
                self.llapi.clear_console()
                while running:
                    close_request = self.llapi.close_request(close_id)
                    if close_request == None:
                        print("Sorry, there are no requests with that ID\n")
                        time.sleep(1.8)
                        self.llapi.clear_console()
                        all_open_work_requests = self.llapi.all_open_work_requests()
                        for request in all_open_work_requests:
                            print(request)
                        try:
                            close_id = int(input("Please try another ID: "))
                        except ValueError:
                            close_id = None
                        print()
                    elif close_request == 69:
                        print("That work request is already closed")
                        time.sleep(1.8)
                        self.llapi.clear_console()
                        all_open_work_requests = self.llapi.all_open_work_requests()
                        for request in all_open_work_requests:
                            print(request)
                        close_id = int(input("Please try another ID: "))
                    else:
                        print("Work request changed successfully!".center(48, '-'))
                        time.sleep(1.8)
                        running = False
                
            elif command.lower() == 'r': # Return to Main Menu
                self.llapi.clear_console()
                return 'r'
            else:
                print("Invalid option, please try again ")
                time.sleep(1.4)
            
    def create_new_request(self):
        today = datetime.today()
        day = today.strftime("%d/%m/%y")
        running = True
        employee = self.llapi.curent_user
        work_request_ID = self.llapi.work_req_count()
        print(f"Work request ID: {self.llapi.work_req_count()}")
        title = input("Title: ")
        print("Available Locations:", ' - '.join(self.llapi.location_list()))
        where = input("Location: ")
        print("Available housing:")
        locations = self.llapi.get_housing_id_by_location(where)
        print(' - '.join(locations))
        housing = input("Housing: ")
        description = input("Description: ")
        while running:
            priority = input("Priority: ")
            if priority not in PRIORITY:
                print("Please use high, medium or low")
            else:
                running = False
        status = 'Open'
        req = Work_Request(work_request_ID, title, where,  housing, description, priority, status, day, employee)
        self.llapi.create_new_request(req)