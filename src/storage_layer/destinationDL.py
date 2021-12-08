import csv 
from src.models.destination import Destination

class DestinationDL:
    def __init__(self):
        self.filepath = "src/data/Destinations.csv"

    def destination_info(self):          # Reads the destination CSV file and returns a list of all the info.
        ret_list = []
        with open(self.filepath, newline='', encoding='utf-8') as csvfile:
            reader = csv.DictReader(csvfile)
            for row in reader:
                dest = Destination(**row)
                ret_list.append(dest)
        return ret_list
    
    def get_only_city(self):          # Reads the destination CSV file and returns a list of only the cities.
        dest_list = []
        with open(self.filepath, newline='', encoding='utf-8') as destfile:
            reader = csv.reader(destfile)
            next(reader)
            for row in reader:
                dest_list.append(row[0])
        return dest_list
    
    def search_des_file_by_city(self, city):          # Checks if the city excists in the file.
        with open(self.filepath, newline='', encoding='utf-8') as csvfile:
            reader = csv.DictReader(csvfile)
            for row in reader:
                if row['city'] == city:
                    des = Destination(**row)
                    return des          # if it does excist, it just returns the Destination class.
        return None          # else it returns none.

