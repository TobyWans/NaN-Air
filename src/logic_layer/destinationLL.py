from src.storage_layer.DLAPI import DLAPI

class DestinationLL:
    def __init__(self, dlapi):
        self.dlapi = dlapi

    def print_nuuk(self, index):
        return self.dlapi.destination_info(index)