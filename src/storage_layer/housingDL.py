import csv

from src.models.housing import Housing
from src.models.housing import Particular_real_estate

class HousingDL:
    def __init__(self):
        self.filepath = "src/data/Housing.csv"

    def add_housing(self, hous):
        with open(self.filepath, 'a', newline='', encoding='utf-8') as csvfile:
            fieldnames = ["supervisor", "property_number" ,"street_name" ,"street_number", "location" ,"size", "nr_of_rooms" ,"type", "requires_maintenance", "rental_status"]
            writer = csv.DictWriter(csvfile, fieldnames=fieldnames)
            writer.writerow({"supervisor": hous.supervisor,"property_number": hous.property_number, "street_name": hous.street_name, "street_number": hous.street_number, "location": hous.location, "size": hous.size, "nr_of_rooms": hous.nr_of_rooms, "type": hous.type, "requires_maintenance": hous.requires_maintenance, "rental_status": hous.rental_status})

    def change_housing(self, hous):
        pass

    def get_housing_list(self):
            hous_list = []
            with open(self.filepath, newline='', encoding='utf-8') as csvfile:
                reader = csv.DictReader(csvfile)
                for row in reader:
                    hous_list.append(row)
            return hous_list
        
    def get_housing_id_by_location(self, location):
        housing_id_list = []
        with open(self.filepath, newline='', encoding='utf-8') as csvfile:
            reader = csv.DictReader(csvfile)
            for row in reader:
                if row['location'] == location:
                    housing_id = Housing(**row)
                    housing_id_list.append(housing_id)
        return housing_id_list
    
    def get_location_list(self):
        location_list = []
        with open(self.filepath, newline='', encoding='utf-8') as csvfile:
            reader = csv.DictReader(csvfile)
            for row in reader:
                if row['location'] in location_list:
                    continue
                else:
                    location_list.append(row['location'])
        return location_list
    
    def search_by_housing_id(self, entered_property_number):
        
        with open(self.filepath, newline='', encoding='utf-8') as csvfile:
            reader = csv.DictReader(csvfile)
            for row in reader:
                if row["property_number"] == entered_property_number:
                    property = Particular_real_estate(**row)
                    return property
            return "Invalid input!"

    def change_housing():
        pass

    def get_rental_status(self): #List of free to book and booked requests
        free_to_book = []
        booked = []
        with open(self.filepath, newline='', encoding='utf-8') as csvfile:
            reader = csv.DictReader(csvfile)
            for row in reader:
                hous = Housing(**row)
                if row['rental_status'] == 'free to rent':
                    free_to_book.append(hous)
                else: 
                    booked.append(hous)
                    
        return free_to_book, booked


'''    

'''