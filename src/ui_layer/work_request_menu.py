from src.models.work_requests import Work_Request
from src.logic_layer.LLAPI import LLAPI
from src.models.work_report import Work_Report
from datetime import datetime
import time

PRIORITY = ('Low', 'Medium', 'High')

class WorkRequestMenu:
    def __init__(self, llapi: LLAPI):
        self.llapi = llapi
        self.supervisor_options = ["Create new request", "Open/Change request", "Close request", "List of work reports"]
        self.employee_options = ["All work requests", "Search by ID", "Search by user ID", "Search by date", "Search by housing ID", "Your open requests", "Finished request"]
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
        print("=".center(48, '='))
        print("Work Request Menu".center(48, ' '))
        print("=".center(48, '='))
        print()
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
                    self.llapi.clear_console()
                    print(self.splash_screen)
                    print("Search for work requests by ID".center(48, '-'))
                    search_id = self.llapi.search_id(id_input)
                    if search_id == None:
                        print("\nSorry, there are no requests with that ID\n".center(48))
                        id_input = input("Please try another ID: ")
                        if id_input == 'r':
                            running = False
                        print()
                    else:
                        print(search_id)
                        id_input = input("Enter another ID to search or type r to return: ")
                        self.llapi.clear_console()
                        if id_input == 'r':
                            running = False
                            
            # B??ta vi?? search by user id
            elif command == '3':
                running = True
                id_input = input("Please enter a user ID or type r to return: ")
                if id_input == 'r':
                    running = False
                print()
                while running:
                    self.llapi.clear_console()
                    print(self.splash_screen)
                    print("Search for work requests by user ID".center(48, '-'))
                    search_id = self.llapi.search_user_id(id_input)
                    if search_id == None:
                        print("\nSorry, there are no requests with that user ID\n".center(48))
                        id_input = input("Please try another user ID: ")
                        if id_input == 'r':
                            running = False
                        print()
                    else:
                        for req in search_id:
                            print(req)
                        id_input = input("Enter another user ID to search or type r to return: ")
                        self.llapi.clear_console()
                        if id_input == 'r':
                            running = False
                
            elif command == '4': # Search Work Requests by date
                running = True
                print("Enter a date in the format dd-mm-yy or type r to return")
                date_input = input("".center(27))
                if date_input == 'r':
                    running = False
                else:
                    date_str = datetime.strptime(date_input, "%d-%m-%y")
                    date_obj = date_str.strftime("%d/%m/%y")
                while running:
                    self.llapi.clear_console()
                    print(self.splash_screen)
                    print("Search for work requests by date".center(48, '-'))
                    search_date = self.llapi.search_date(date_obj)
                    if search_date == None:
                        print("\nSorry, there is no requests with that date\n".center(48))
                        print("Try another date | dd-mm-yy | or type r to return")
                        date_input = input("".center(19))
                        if date_input == 'r':
                            running = False
                        else:
                            date_str = datetime.strptime(date_input, "%d-%m-%y")
                            date_obj = date_str.strftime("%d/%m/%y")
                            self.llapi.clear_console()
                    else:
                        for req in search_date:
                            print(req)
                        print("Enter another date | dd-mm-yy | or type r to return")
                        date_input = input("".center(21))
                        if date_input == 'r':
                            running = False
                        else:
                            date_str = datetime.strptime(date_input, "%d-%m-%y")
                            date_obj = date_str.strftime("%d/%m/%y")
                            self.llapi.clear_console()
                            
            elif command == '5': # Search by housing ID.
                running = True
                id_input = input("Please enter a housing ID of your work request or type r to return: ")
                if id_input == 'r':
                    running = False
                print()
                while running:
                    self.llapi.clear_console()
                    print(self.splash_screen)
                    print("Search for work requests by housing ID".center(48, '-'))
                    search_id = self.llapi.search_housing_id(id_input)
                    if search_id == None:   
                        print("\nSorry, there are no requests with that housing ID\n".center(48))
                        id_input = input("Please try another ID: ")
                        if id_input == 'r':
                            running = False
                        print()
                    else:
                        for house in search_id:
                            print(house)
                        id_input = input("Enter another housing ID to search or type r to return: ")
                        self.llapi.clear_console()
                        if id_input == 'r':
                            running = False
                
            elif command == '6': # User open Work Requests
                user_rep = self.llapi.user_open_requests(self.llapi.curent_user)
                self.llapi.clear_console()
                print(self.splash_screen)
                print("Your open requests".center(48, '-'))
                if user_rep != []:
                    for row in user_rep:
                        print(row)
                    work_report_input = input("Enter ID of work request to write a report on or type R to return: ")
                    if work_report_input.lower() == 'r':
                        pass
                    elif self.llapi.report_id_check(work_report_input):
                        print("Report already created!")
                        time.sleep(1.4)
                    else:
                        self.create_work_report(work_report_input)
                        print("Work Report created successfully!")
                        time.sleep(1.8)
                else:
                    print("\n\tThere are no open work requests for you")
                    time.sleep(1.8)
                
                    
            elif command == '7': # List Finished Requests
                finished_requests = self.llapi.all_closed_work_requests()
                self.llapi.clear_console()
                print("List of closed work Requests".center(48, '-'))
                for request in finished_requests:
                    print(request)
                back = input("Press enter to continue")
                self.llapi.clear_console()
                
            elif command == '8' and self.llapi.supervisor_check(): # Create new Request
                self.create_new_request()
                print("Work request created successfully".center(48, '-'))
                time.sleep(1.8)
                
            elif command == '9' and self.llapi.supervisor_check(): # Open Request
                running = True
                all_closed_work_requests = self.llapi.all_closed_work_requests()
                self.llapi.clear_console()
                print("All closed work requests".center(48, '-'))
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
                        open_id = input("Please try another ID or type R to return: ")
                        if open_id.lower() == 'r':
                            running = False
                            open_id = 0
                        open_id = int(open_id)
                    else:
                        print("Work request successfully opened!".center(48, '-'))
                        while running:
                            change = input("Would you like to change the request? (Y/N): ")
                            if change.lower() == 'y':
                                self.change_request(open_id)
                                print("Work request changed successfully!")
                                time.sleep(1)
                                running = False
                            elif change.lower() == 'n': 
                                time.sleep(1)
                                running = False
                            else:
                                continue
                            
                
            elif command == '10' and self.llapi.supervisor_check(): # Close Request
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
                        report = input("Would you like to look at the work report for this request? (Y/N)")
                        if report.lower() == 'y':
                            work_reports = self.llapi.get_all_work_reports(str(close_id))
                            for report in work_reports:
                                print(report)
                        elif report.lower() == 'n':
                            time.sleep(1)
                            running = False
                        again = input("\nWould you like to close another work request? (Y/N): ")
                        if again.lower() == 'y':
                            self.llapi.clear_console()
                            all_open_work_requests = self.llapi.all_open_work_requests()
                            for request in all_open_work_requests:
                                print(request)
                            close_id = input("Please enter a work request ID you want to close or R to return: ")
                            if close_id.lower() == 'r':
                                running = False
                                close_id = 0
                            elif close_id.isdigit():
                                close_id = int(close_id)
                            else:
                                close_id = None
                        elif again.lower() == 'n': 
                            time.sleep(1)
                            running = False
                        else:
                            continue
                        
            elif command == '11':
                all_work_reports = self.llapi.get_all_reports(self.llapi.curent_user)
                self.llapi.clear_console()
                print("List of all open work reports".center(48, '-'))
                for request in all_work_reports:
                    print(request)
                back = input("Press enter to continue")
                self.llapi.clear_console()
                
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
        while running:
            print("Available Locations:", ' - '.join(self.llapi.location_list()) + ' - Everywhere')
            where = input("Location: ").capitalize()
            if where.capitalize() in self.llapi.location_list() or where.lower() == 'everywhere':
                running = False
        running = True
        locations = self.llapi.get_housing_id_by_location(where.capitalize())
        while running:
            if where.lower() == 'everywhere':
                housing = 'All'
                running = False
                break
            print("Available housing:")
            print(' - '.join(locations))
            housing = input("Housing: ")
            if housing in self.llapi.get_housing_id_by_location(where.capitalize()):
                running = False
        running = True
        description = input("Description: ")
        print("high, medium or low")
        while running:
            priority = input("Priority: ")
            if priority.capitalize() not in PRIORITY:
                print("Please use high, medium or low")
            else:
                running = False
        status = 'Open'
        req = Work_Request(work_request_ID, title, where,  housing, description, priority, status, day, employee)
        self.llapi.create_new_request(req)
        
    def change_request(self, req_id):
        today = datetime.today()
        day = today.strftime("%d/%m/%y")
        running = True
        employee = self.llapi.curent_user
        work_request_ID = req_id
        print(f"Work request ID: {req_id}")
        title = input("Title: ")
        while running:
            print("Available Locations:", ' - '.join(self.llapi.location_list()) + ' - Everywhere')
            where = input("Location: ")
            if where.capitalize() in self.llapi.location_list() or where.lower() == 'everywhere':
                running = False
            running = True
        print("Available housing:")
        locations = self.llapi.get_housing_id_by_location(where)
        while running:
            print(' - '.join(locations) + ' - All')
            housing = input("Housing: ")
            if housing in self.llapi.get_housing_id_by_location(where.capitalize() or housing.lower() == 'all'):
                running = False
        running = True
        description = input("Description: ")
        while running:
            priority = input("Priority: ").capitalize()
            if priority not in PRIORITY:
                print("Please use high, medium or low")
            else:
                running = False
        status = 'Open'
        change_req = Work_Request(work_request_ID, title, where.capitalize(),  housing, description, priority, status, day, employee)
        self.llapi.change_req(change_req, req_id)
        
    def create_work_report(self, wr_id):
        MAINTENANCE = ('I', 'R')
        running = True
        employee = self.llapi.curent_user
        work_report_id = str(wr_id)
        print(f"Work report ID: {wr_id}")
        while running:
            regular_irr = input("Regular/Irregular Maintenance(R/I): ")
            if regular_irr.capitalize() in MAINTENANCE:
                running = False
        housing = input("Housing: ")
        description = input("Description: ")
        timeofjob = input("Time in hours: ")
        contractor = (input("Contractor Cost: "))
        if contractor == '':
            contractor = None
        other = (input("Other costs: "))
        if other == '':
            other = None
        rep = Work_Report(work_report_id, housing, regular_irr.capitalize(), description, timeofjob, contractor, other, employee)
        self.llapi.create_report(rep)