### below is the bad example
'''class PhoneDisplay:
    def update(self,new_temp):
        print(f"Phone displayed temperature : {new_temp}")

class TVDisplay:
    def update(self, new_temp):
        print(f"TV display temperature: {new_temp}")


class WeatherStation:
    def __init__(self):
        self.__temperature = 0
        self.__phone_display = PhoneDisplay()
        self.__tv_display = TVDisplay()

    def update_temperature(self,new_temp):
        self.__temperature = new_temp
        self.notify_display()

    def notify_display(self):
        self.__phone_display.update(self.__temperature)
        self.__tv_display.update(self.__temperature)


ws = WeatherStation()
ws.update_temperature(30)'''
#####################################################################################################
## better method

from abc import ABC, abstractmethod
from typing import List

class Observer(ABC):
    @abstractmethod
    def update(self,temp):
        pass


class TVDisplay(Observer):
    def update(self, temp):
        print(f"TV temperature updated is {temp}")


class WeatherStation:
    def __init__(self):
        self.__temperature = 0
        self.__observers:List[Observer]=[]

    def add_observer(self,new_observer:Observer):
        self.__observers.append(new_observer)

    def remove_observer(self,ob:Observer):
        self.__observers.remove(ob)

    def update_temperature(self,new_temp):
        self.__temperature= new_temp
        self.notify_observers()

    ## notify
    def notify_observers(self):
        for observer in self.__observers:
            observer.update(self.__temperature)



class MobileDisplay(Observer):
    def update(self,temp):
        print(f"Mobile temperature display is {temp}")


class DesktopDisplay(Observer):
    def update(self,temp):
        print(f"Desktop temperature display :{temp}")

