import csv
from src.models.work_requests import Work_Request

class WorkRequestDL:
    def __init__(self):
        self.work_req_file = 'src\data\Work_Requests.csv'
        self.finnished_work_req_file = 'src\data\Finnished_WR.csv'
        self.tmp_file = 'src\data\work_request_temp.csv'
    
    def get_all_work_requests(self):
        req_list = []
        with open(self.work_req_file, newline='', encoding='utf-8') as WRfile:
            reader = csv.DictReader(WRfile)
            for row in reader:
                if row['status'] == 'Open':
                    req = Work_Request(**row)
                    req_list.append(req)
        return req_list
    
    def search_id(self, user_id):
        search_list = []
        with open(self.work_req_file, newline='', encoding='utf-8') as WRfile:
            reader = csv.DictReader(WRfile)
            for row in reader:
                    if row['id'] == user_id:
                        req = Work_Request(**row)
                        return req
        return None
                        
    def create_new_request(self, req):
        with open(self.work_req_file, 'a', newline='', encoding='utf-8') as wrfile:
            fieldnames = ['id', 'title', 'where', 'housing_id', 'description', 'priority']
            writer = csv.DictWriter(wrfile, fieldnames=fieldnames)
            writer.writerow({'id': req.id, 'title': req.title, 'where': req.where, 'housing_id': req.housing_id, 'description': req.description, 'priority': req.priority})
    
    def finnished_work_req(self):
        req_list = []
        with open(self.work_req_file, newline='', encoding='utf-8') as wrfile:
            reader = csv.DictReader(wrfile)
            for row in reader:
                if row['status'] == 'Closed':
                    req = Work_Request(**row)
                    req_list.append(req)
        return req_list
            
    def append_finnished_work_req(self, req):
        with open(self.finnished_work_req_file, 'a', newline='', encoding='utf-8') as wrfile:
            fieldnames = ['id', 'title', 'where', 'housing_id', 'description', 'priority']
            writer = csv.DictWriter(wrfile, fieldnames=fieldnames)
            writer.writerow(req)
            
    def close_request(self, wr_id):
        lines = []
        with open(self.work_req_file, newline='', encoding='utf-8') as wrfile:
            reader = csv.reader(wrfile)
            next(reader) # skip header
            for row in reader:
                lines.append(row)
                for field in row:
                    if field == wr_id:
                        lines.remove(row)
        with open(self.work_req_file, 'w', newline='', encoding='utf-8') as wrfile:
            fieldnames = ['id', 'title', 'where', 'housing_id', 'description', 'priority']
            writer = csv.DictWriter(wrfile, fieldnames=fieldnames)
            req = Work_Request(**row)
            writer.writerow({'id': req.id, 'title': req.title, 'where': req.where, 'housing_id': req.housing_id, 'description': req.description, 'priority': req.priority})
            
       
    def work_req_count(self):
        with open(self.work_req_file, newline='', encoding='utf-8') as wrfile:
            reader = csv.reader(wrfile)
            lines = len(list(reader))
        return lines
            