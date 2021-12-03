from src.storage_layer.DLAPI import DLAPI
from src.models.contractors import contractors


class ContractorMenuLL:
    def __init__(self, dlapi: DLAPI):
        self.dlapi = dlapi
    
    def add_new_contractor(self, Contractor_mdl):
        self.dlapi.add_new_contractor(Contractor_mdl)

    def get_contractor_list(self):
        contractor_list = self.dlapi.get_contractor_list()
        self.contractor_list_str = []
        for Contractor in contractor_list:
            contr_str = Contractor.display()
            self.contractor_list_str.append(contr_str)
        return self.contractor_list_str, contractor_list