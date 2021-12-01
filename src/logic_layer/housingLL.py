from src.models.housing import Housing

class HousingLL:
    def __init__(self, dlapi):
        self.dlapi = dlapi

    def add_housing(self, hous):
        self.dlapi.add_housing(hous)