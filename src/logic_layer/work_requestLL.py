from src.storage_layer.DLAPI import DLAPI


class WorkRequestLL:
    def __init__(self, dlapi):
        self.dlapi = dlapi
        
    def all_work_requests(self):
        return self.dlapi.get_all_work_requests()
    
    def search_id(self, user_id):
        pass
    
    def search_date(self, date="01.01.2020"):
        pass
    
    def user_open_requests(self):
        pass
    
    def finished_requests(self):
        pass
    
    def create_new_request(self, req):
        return self.dlapi.create_new_request(req)
    
    def open_change_request(self):
        pass
    
    def close_request(self):
        pass
    
    
if __name__=='__main__':
    requestsLL = WorkRequestLL(DLAPI())