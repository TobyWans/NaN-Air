from src.models.housing import Housing
from src.storage_layer.DLAPI import DLAPI

class HousingLL:
    def __init__(self, dlapi:DLAPI):
        self.dlapi = dlapi

    def add_housing(self, hous):
        self.dlapi.add_housing(hous)

    def change_housing(self, id_number, fieldname, parametr):
        return self.dlapi.change_housing(id_number, fieldname, parametr)

    def housing_list(self):
        return self.dlapi.get_housing_list()

    def get_location_list(self):
        return self.dlapi.get_location_list()

    def search_by_housing_id(self, entered_id):
        return self.dlapi.search_by_housing_id(entered_id)
    
    def get_rental_status(self):
        return self.dlapi.get_rental_status()

    def get_rental_status_by_location(self, user_location):
        return self.dlapi.get_rental_status_by_location(user_location)
    
    def get_housing_id_by_location(self, location):
        get_housing = self.dlapi.get_housing_id_by_location(location)
        housing_id_list = []
        for row in get_housing:
            id_only = row.only_housing_id()
            housing_id_list.append(id_only)
        return housing_id_list
    