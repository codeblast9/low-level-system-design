from location import Location
from vehicle import Vehicle

class Drivers:
    def __init__(self,name:str, location:Location,vehicle:Vehicle):
        self.name = name
        self.location:Location = location
        self.vehicle:Vehicle = vehicle

    def get_location(self)->Location:
        return self.location

    def set_location(self,location:Location)-> None:
        self.location = location

