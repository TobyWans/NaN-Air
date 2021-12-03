from src.storage_layer.DLAPI import DLAPI

class DestinationLL:
    def __init__(self, dlapi: DLAPI):
        self.dlapi = dlapi

    def destination_info(self):
        return self.dlapi.destination_info()
    
    def get_only_city(self):
        return self.dlapi.get_only_city()

    def search_des_file_by_city(self, city):
        return self.dlapi.search_des_file_by_city(city)