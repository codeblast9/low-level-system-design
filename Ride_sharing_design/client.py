from vehicle import Vehicle
from drivers import Drivers
from location import Location
from ride_sharing_service import RideSharingservice
from passengers import Passengers


loc1 = Location(15.8936,16.2587)
loc2 = Location(11.9999,11.5478)
loc3 = Location(13.2547,14.0011)

car = Vehicle("cretta","car")
bike = Vehicle("pulsar","bike")

driver1 = Drivers("john",loc1,car)
driver2 = Drivers("sam",loc2,bike)

passenger = Passengers("chris",loc3)

ride_service = RideSharingservice()
ride_service.add_driver(driver1)
ride_service.add_driver(driver2)

ride_service.add_passenger(passenger)

ride_service.book_ride(passenger,25)
