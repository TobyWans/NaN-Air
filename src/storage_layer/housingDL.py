import csv

from src.models.housing import Housing

class HousingDL:
    def __init__(self):
        self.filepath = "data/Housing.csv"

    def add_housing(self, hous):
        with open(self.filepath, 'a', newline='', encoding='utf-8') as csvfile:
            fieldnames = ["property_number" ,"street_name" ,"street_number", "location" ,"size", "nr_of_rooms" ,"type", "requires_maintenance"]
            writer = csv.DictWriter(csvfile, fieldnames=fieldnames)
            writer.writerow({"property_number": hous.property_number, "street_name": hous.street_name, "street_number": hous.street_number, "location": hous.location, "size": hous.size, "nr_of_rooms": hous.nr_of_rooms, "type": hous.type, "requires_maintenance": hous.requires_maintenance})
            