from src.storage_layer.DLAPI import DLAPI
from src.models.contractors import contractors


class ContractorMenuLL:
    def __init__(self, dlapi: DLAPI):
        self.dlapi = dlapi
    
    def add_new_contractor(self, Contractor_mdl):       # Carries the contractor_mdl from the model class to the DLAPI, also checks format correctness
        self.dlapi.add_new_contractor(Contractor_mdl)

    def get_contractor_list(self):                      # Gets list of all contractors
        contractor_list = self.dlapi.get_contractor_list()
        self.contractor_list_str = []
        for Contractor in contractor_list:
            contr_str = Contractor.display()            # Returns a thumbnail or summary of a contractor in string format
            self.contractor_list_str.append(contr_str)
        return self.contractor_list_str, contractor_list

    def sort_contractors_by_location(self, location):   # Gets list of all contractors in user's location
        sorted_contractor_list = self.dlapi.sort_contractors_by_location(location)
        self.contractor_list_str = []
        for Contractor in sorted_contractor_list:
            contr_str = Contractor.display()            # Contractor.display() returns thumbnail/summary of contractor
            self.contractor_list_str.append(contr_str)
        return self.contractor_list_str, sorted_contractor_list