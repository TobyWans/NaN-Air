import csv

from src.models.housing import Housing

class HousingDL:
    def __init__(self):
        self.filepath = "src/data/Housing.csv"

    def add_housing(self, hous):
        with open(self.filepath, 'a', newline='', encoding='utf-8') as csvfile:
            fieldnames = ["property_number" ,"street_name" ,"street_number", "location" ,"size", "nr_of_rooms" ,"type", "requires_maintenance"]
            writer = csv.DictWriter(csvfile, fieldnames=fieldnames)
            writer.writerow({"property_number": hous.property_number, "street_name": hous.street_name, "street_number": hous.street_number, "location": hous.location, "size": hous.size, "nr_of_rooms": hous.nr_of_rooms, "type": hous.type, "requires_maintenance": hous.requires_maintenance})
    
    def get_housing_list(self):
        ret_list = []
        with open(self.filepath, newline='', encoding='utf-8') as csvfile:
            reader = csv.DictReader(csvfile)
            for row in reader:
                emp = Housing(row["property_number"], row["street_name"], row["street_number"], row["location"], row["size"], row["nr_of_rooms"], row["type"], row ["requires_maintenance"])
                ret_list.append(emp)
        return ret_list
    
    def change_housing():
        pass

    def renting_status():
        pass
