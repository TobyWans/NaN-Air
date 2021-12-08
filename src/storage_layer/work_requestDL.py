from src.models.work_requests import Work_Request
import csv

class WorkRequestDL:
    def __init__(self):
        self.work_req_file = 'src\data\Work_Requests.csv'
    
        # gets all open work requests by searching a csv file
    def get_all_open_work_requests(self):
        req_list = []
        with open(self.work_req_file, newline='', encoding='utf-8') as WRfile:
            reader = csv.DictReader(WRfile)
            for row in reader:
                if row['status'] == 'Open':
                    req = Work_Request(**row)
                    req_list.append(req)
        return req_list
    
        # gets all closed work requests by searching a csv file
    def get_all_closed_work_requests(self):
        req_list = []
        with open(self.work_req_file, newline='', encoding='utf-8') as WRfile:
            reader = csv.DictReader(WRfile)
            for row in reader:
                if row['status'] == 'Closed':
                    req = Work_Request(**row)
                    req_list.append(req)
        return req_list
    
        # Searches for work request by ID the user inputs
    def search_id(self, req_id):
        with open(self.work_req_file, newline='', encoding='utf-8') as WRfile:
            reader = csv.DictReader(WRfile)
            for row in reader:
                if row['req_id'] == req_id:
                    req = Work_Request(**row)
                    return req
        return None
    
        # Searches for work request by a date the user inputs
    def search_date(self, date):
        reqs_list = []
        with open(self.work_req_file, newline='', encoding='utf-8') as wrfile:
            reader = csv.DictReader(wrfile)
            for row in reader:
                if row['date'] == date:
                    req = Work_Request(**row)
                    reqs_list.append(req)
        if len(reqs_list):
            return reqs_list
        else:
            return None
        
        # Creates a new work request and writes it to the csv file
    def create_new_request(self, req):
        with open(self.work_req_file, 'a', newline='', encoding='utf-8') as wrfile:
            fieldnames = ['req_id', 'title', 'where', 'housing_id', 'description', 'priority', 'status', 'date', 'employee']
            writer = csv.DictWriter(wrfile, fieldnames=fieldnames)
            writer.writerow({'req_id': req.req_id, 'title': req.title, 'where': req.where, 'housing_id': req.housing_id, 'description': req.description, 'priority': req.priority, 'status': req.status, 'date': req.date, 'employee': req.employee})
            
        # Closes open work request
    def close_request(self, wr_id):
        if wr_id == None:
            return None
        try:
            with open(self.work_req_file, newline='', encoding='utf-8') as wrfile:
                reader = csv.reader(wrfile)
                lines = list(reader)
                if lines[wr_id][6] == 'Closed':
                    return 69
                lines[wr_id][6] = 'Closed'
        except (IndexError, ValueError):
            return None
        with open(self.work_req_file, 'w', newline='', encoding='utf-8') as wrfile:
            writer = csv.writer(wrfile)
            writer.writerows(lines)
            return True
            
        # Opens closed work request
    def open_request(self, wr_id):
        if wr_id == None:
            return None
        try:
            with open(self.work_req_file, newline='', encoding='utf-8') as wrfile:
                reader = csv.reader(wrfile)
                lines = list(reader)
                if lines[wr_id][6] == 'Open':
                    return 69
                lines[wr_id][6] = 'Open'
        except (IndexError, ValueError):
            return None
        with open(self.work_req_file, 'w', newline='', encoding='utf-8') as wrfile:
            writer = csv.writer(wrfile)
            writer.writerows(lines)
        return True
    
    def change_request_prep(self, re_id):
        with open(self.work_req_file, newline='', encoding='utf-8') as readfile:
            reader = csv.reader(readfile)
            lines = list(reader)
            for line in lines:
                if line[re_id][0] == re_id:
                    return line
       
       # counter for requests to id them
    def work_req_count(self):
        with open(self.work_req_file, newline='', encoding='utf-8') as wrfile:
            reader = csv.reader(wrfile)
            lines = len(list(reader))
        return lines
            