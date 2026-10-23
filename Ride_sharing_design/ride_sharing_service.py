from typing import List
from drivers import Drivers
from passengers import Passengers
from location import Location
from math import sqrt
from vehicle import Vehicle

class RideSharingservice:
    def __init__(self):
        self.drivers:List[Drivers]= []
        self.passengers:List[Passengers] = []

    def add_driver(self,driver:Drivers):
        self.drivers.append(driver)

    def add_passenger(self,passenger:Passengers):
        self.passengers.append(passenger)

    def __CalculateDistance(self,location1:Location,location2:Location):
        dx:float = location1.get_latitude() - location2.get_latitude()    
        dy:float = location2.get_latitude() - location2.get_latitude()
        return sqrt(dx*dx + dy* dy)

    def __CalculateFare(self,vehicle:Vehicle,distance:float):
        if vehicle.type =="car":
            return distance * 15
        elif vehicle.type == "bike":
            return distance * 8
        else:
            return distance * 3

    def book_ride(self,passenger:Passengers,distance:float):
        if self.drivers == 0:
            print("there are no available drivers in your area, if possible shift a little and try again")
            return

        assignedDriver = None
        minDistance = float("inf")
        for driver in self.drivers:
            CurrentDriverDistance = self.__CalculateDistance(driver.get_location(),passenger.location)
        if CurrentDriverDistance < minDistance:
            minDistance = CurrentDriverDistance
            assignedDriver = driver

        expectedFare: float = self.__CalculateFare(assignedDriver.vehicle, distance)
        print(f"Ride booked for {passenger.name}, driver:{driver.name} is on the way...")
        print(f"thanks for waiting {driver.name} is only {minDistance}kms away.")
        print(f"you fare will be {expectedFare}")

