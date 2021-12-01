import csv
from src.models.work_requests import Work_Request

class WorkRequestDL:
    def __init__(self):
        self.filepath = 'src\data\Work_Requests.csv'
    
    def get_all_work_requests(self):
        req_list = []
        with open(self.filepath, newline='', encoding='utf-8') as WRfile:
            reader = csv.DictReader(WRfile)
            for row in reader:
                req = Work_Request(row["title"], row["where"], row["housing_id"], row["description"], row["priority"])
                req_list.append(req)
        return req_list
    
    def create_new_request(self, req):
        with open(self.filepath, 'a', newline='', encoding='utf-8') as wrfile:
            fieldnames = ['title', 'where', 'housing_id', 'description', 'priority']
            writer = csv.DictWriter(wrfile, fieldnames=fieldnames)
            writer.writerow({'title': req.title, 'where': req.where, 'housing_id': req.housing_id, 'description': req.description, 'priority': req.priority})