from abc import ABC, abstractmethod

from typing import List

class AirTrafficControl(ABC):
    @abstractmethod
    def register_airplane(self):
        pass

    @abstractmethod
    def send_message(self):
        pass

class ControlTower(AirTrafficControl):
    def __init__(self):
        self.__airplanes:List[Airplane] = []

    def register_airplane(self, new_airplane:'Airplane'):
        self.__airplanes.append(new_airplane)

    def send_message(self, msg:str, sender:'Airplane'):
        for airplane in self.__airplanes:
            if airplane != sender:
                airplane.recieve_message(msg, sender)



class Airplane:
    def __init__(self,flight_num:str, control_tower:str):
        self.__flight_number = flight_num
        self.__control_tower = control_tower

        self.__control_tower.register_airplane(self)

    def send_message(self, msg:str):
        self.__control_tower.send_message(msg, self)

    def get_flight_num(self):
        return self.__flight_number

    def recieve_message(self, msg:str, sender:'Airplane'):
        print(f"{self.__flight_number} got {msg} from {sender.get_flight_num()}")


control_tower = ControlTower()
air_india = Airplane("AIR-546", control_tower)
spicejet = Airplane("SPICE-87171", control_tower)
indigo = Airplane("IND-9911", control_tower)

air_india.send_message("I am getting on runway")

express = Airplane("EXP-1122", control_tower)
express.send_message("I am getting on runway")