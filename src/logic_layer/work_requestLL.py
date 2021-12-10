from src.storage_layer.DLAPI import DLAPI


class WorkRequestLL:
    def __init__(self, dlapi: DLAPI):
        self.dlapi = dlapi
        
    def all_open_work_requests(self):
        return self.dlapi.get_all_open_work_requests()
    
    def all_closed_work_requests(self):
        return self.dlapi.get_all_closed_work_requests()
    
    def get_all_work_reports(self, wr_id):
        return self.dlapi.get_all_work_reports(wr_id)
    
    def get_all_reports(self, wr_id):
        return self.dlapi.get_all_reports(wr_id)
    
    def report_id_check(self, wr_id):
        return self.dlapi.report_id_check(wr_id)
    
    def search_id(self, user_id):
        return self.dlapi.search_id(user_id)
    
    def search_user_id(self, user_id):
        return self.dlapi.search_user_id(user_id)
    
    def search_date(self, date):
        return self.dlapi.search_date(date)
    
    def search_housing_id(self, housing):
        return self.dlapi.search_housing_id(housing)
    
        # gets all requests linked to the users account
    def user_open_requests(self, user_id):
        user_req_list = []
        wr_list = self.dlapi.get_all_open_work_requests()
        for req in wr_list:
            if user_id == req.employee:
                user_req_list.append(req)
        return user_req_list
    
    def create_new_request(self, req):
        return self.dlapi.create_new_request(req)
    
    def create_report(self, rep):
        return self.dlapi.create_report(rep)
    
    def open_request(self, wr_id):
        return self.dlapi.open_request(wr_id)
    
    def close_request(self, wr_id):
        return self.dlapi.close_request(wr_id)
    
    def change_req(self,change_req,  req_id):
        return self.dlapi.change_req(change_req, req_id)
    
    def work_req_count(self):
        return self.dlapi.work_req_count()
    
    def work_rep_count(self):
        return self.dlapi.work_rep_count()
    
    
if __name__=='__main__':
    requestsLL = WorkRequestLL(DLAPI())