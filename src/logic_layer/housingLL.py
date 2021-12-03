from src.models.housing import Housing
from src.storage_layer.DLAPI import DLAPI

class HousingLL:
    def __init__(self, dlapi:DLAPI):
        self.dlapi = dlapi

    def add_housing(self, hous):
        self.dlapi.add_housing(hous)

    def housing_list(self):
        return self.dlapi.get_housing_list()

    def get_location_list(self):
        return self.dlapi.get_location_list()

    def search_by_housing_id(self, entered_id):
        return self.dlapi.search_by_housing_id(entered_id)
    
    def get_rental_status(self):
        return self.dlapi.get_rental_status()
    