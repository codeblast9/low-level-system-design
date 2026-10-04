from abc import ABC,abstractmethod

class TransportMode(ABC):

    @abstractmethod
    def eta(self):
        pass

    @abstractmethod
    def directions(self):
        pass


class BikeMode(TransportMode):
    def eta(self):
        print("15 minutes to reach destination")

    def directions(self):
        print("2 left and then 1 right from the current destination")

class WalkMode(TransportMode):
    def eta(self):
        print("21 minutes to reach the destination")

    def directions(self):
        print("take the bridge and then a left")

class TrainMode(TransportMode):
    def eta(self):
        print("10 minutes to reach the destination")
    def directions(self):
        print("take churgate train at prabhadevi and get off at mahalaxmi")

class TransportService:
    def __init__(self, mode:TransportMode):
        self.__mode:TransportMode = mode

    def set_mode(self, new_mode:TransportMode):
        self.__mode:TransportMode = self.new_mode


    def eta(self):
        self.__mode.eta()

    def directions(self):
        self.__mode.directions()


        
