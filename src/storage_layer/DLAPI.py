from src.storage_layer.destinationDL import DestinationDL

class DLAPI:
    def __init__(self):
        self.destDL = DestinationDL()

    def destination_info(self, index):
        return self.destDL.destination_info(index)
