from src.storage_layer.DLAPI import DLAPI

class DestinationLL:
    def __init__(self, dlapi):
        self.dlapi = dlapi

    def destination_info(self):
        return self.dlapi.destination_info()