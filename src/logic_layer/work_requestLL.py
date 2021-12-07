from src.storage_layer.DLAPI import DLAPI


class WorkRequestLL:
    def __init__(self, dlapi: DLAPI):
        self.dlapi = dlapi
        
    def all_open_work_requests(self):
        return self.dlapi.get_all_open_work_requests()
    
    def all_closed_work_requests(self):
        return self.dlapi.get_all_closed_work_requests()
    
    def search_id(self, user_id):
        return self.dlapi.search_id(user_id)
    
    def search_date(self, date):
        return self.dlapi.search_date(date)
    
    def user_open_requests(self, user_id):
        user_req_list = []
        wr_list = self.dlapi.get_all_open_work_requests()
        for req in wr_list:
            if user_id == req.user_id:
                user_req_list.append
        return user_req_list
    
    def finnished_work_req(self):
        return self.dlapi.finnished_work_req()
    
    def append_finnished_work_req(self, req):
        return self.dlapi.append_finnished_work_req(req)
    
    def create_new_request(self, req):
        return self.dlapi.create_new_request(req)
    
    def open_request(self, wr_id):
        return self.dlapi.open_request(wr_id)
    
    def close_request(self, wr_id):
        return self.dlapi.close_request(wr_id)
    
    def work_req_count(self):
        return self.dlapi.work_req_count()
    
    
if __name__=='__main__':
    requestsLL = WorkRequestLL(DLAPI())