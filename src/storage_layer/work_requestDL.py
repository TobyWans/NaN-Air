from src.models.work_report import Work_Report
from src.models.work_requests import Work_Request
import csv, os

class WorkRequestDL:
    def __init__(self):
        self.work_req_file = 'src\data\Work_Requests.csv'
        self.work_report_file = 'src\data\work_report.csv'
    
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
    
    def get_all_work_reports(self, wr_id):
        rep_list = []
        with open(self.work_report_file, newline='', encoding='utf-8') as WRfile:
            reader = csv.DictReader(WRfile)
            for row in reader:
                if row['rep_id'] == wr_id:
                    req = Work_Report(row['rep_id'], row['housing'], row['regular_irr'], row['work_desc'], row['time'], row['contractor_cost'], row['other_cost'], row['employee'])
                    rep_list.append(req)
        return rep_list
    
    def get_all_reports(self, wr_id):
        rep_list = []
        with open(self.work_report_file, newline='', encoding='utf-8') as WRfile:
            reader = csv.DictReader(WRfile)
            for row in reader:
                if row['employee'] == wr_id:
                    req = Work_Report(row['rep_id'], row['housing'], row['regular_irr'], row['work_desc'], row['time'], row['contractor_cost'], row['other_cost'], row['employee'])
                    rep_list.append(req)
        return rep_list
    
    def report_id_check(self, wr_id):
        with open(self.work_report_file, newline='', encoding='utf-8') as WRfile:
            reader = csv.DictReader(WRfile)
            for row in reader:
                if row['rep_id'] == wr_id:
                    return True
        return False
    
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
    
    def search_user_id(self, user_id):
        reqs_list = []
        with open(self.work_req_file, newline='', encoding='utf-8') as WRfile:
            reader = csv.DictReader(WRfile)
            for row in reader:
                if row['employee'] == user_id:
                    req = Work_Request(**row)
                    reqs_list.append(req)
        if len(reqs_list):
            return reqs_list
        else:
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
        
    def search_housing_id(self, housing):
        req_list = []
        with open(self.work_req_file, newline='', encoding='utf-8') as wrfile:
            reader = csv.DictReader(wrfile)
            for row in reader:
                if row['housing_id'] == housing:
                    req = Work_Request(**row)
                    req_list.append(req)
            if len(req_list):
                return req_list
            else:
                return None
        
        # Creates a new work request and writes it to the csv file
    def create_new_request(self, req):
        with open(self.work_req_file, 'a', newline='', encoding='utf-8') as wrfile:
            fieldnames = ['req_id', 'title', 'where', 'housing_id', 'description', 'priority', 'status', 'date', 'employee']
            writer = csv.DictWriter(wrfile, fieldnames=fieldnames)
            writer.writerow({'req_id': req.req_id, 'title': req.title, 'where': req.where, 'housing_id': req.housing_id, 'description': req.description, 'priority': req.priority, 'status': req.status, 'date': req.date, 'employee': req.employee})
            
    def create_report(self, rep):
        with open(self.work_report_file, 'a', newline='', encoding='utf-8') as workreport:
            fieldnames = ['rep_id','housing','regular_irregular','work_desc','time','contractor_cost','other_cost','employee']
            writer = csv.DictWriter(workreport, fieldnames=fieldnames)
            writer.writerow({'rep_id': rep.rep_id, 'housing': rep.housing, 'regular_irregular': rep.regular_irr, 'work_desc': rep.desc, 'time': rep.time, 'contractor_cost': rep.contractor, 'other_cost': rep.other, 'employee': rep.employee})
        
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
    
    def change_request_prep(self,change_req, re_id):
        change_list = list()
        with open(self.work_req_file, 'r', newline='', encoding='utf-8') as csvfile:
            reader = csv.DictReader(csvfile)
            for row in reader:
                print(row)
                if str(re_id) == row['req_id']:
                    change_list.append({'req_id': change_req.req_id, 'title': change_req.title, 'where': change_req.where, 'housing_id': change_req.housing_id, 'description': change_req.description, 'priority': change_req.priority, 'status': change_req.status, 'date': change_req.date, 'employee': change_req.employee})
                else:
                    change_list.append(row)
                    
        with open(self.work_req_file, 'w', newline='', encoding='utf-8') as csvfile:
            fieldnames = ['req_id', 'title', 'where', 'housing_id', 'description', 'priority', 'status', 'date', 'employee']
            writer = csv.DictWriter(csvfile, fieldnames=fieldnames)
            writerV2 = csv.writer(csvfile)
            writerV2.writerow(fieldnames)
            writer.writerows(change_list)
            
       # counter for requests to id them
    def work_req_count(self):
        with open(self.work_req_file, newline='', encoding='utf-8') as wrfile:
            reader = csv.reader(wrfile)
            lines = len(list(reader))
        return lines
    
    def work_rep_count(self):
        with open(self.work_report_file, newline='', encoding='utf-8') as wrfile:
            reader = csv.reader(wrfile)
            lines = len(list(reader))
        return lines
            