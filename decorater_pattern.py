''''''

from abc import ABC, abstractmethod

class Beverages(ABC):
    @abstractmethod
    def get_description(self)->str:
        pass

    @abstractmethod
    def get_price(self)->int:
        pass

class Coffee(Beverages):
    def get_description(self):
        return "Order Plain Coffee"

    def get_price(self):
        return 100
class AddOnDecorator(Beverages):
    def __init__(self,coffee:Coffee):
        self._coffee = coffee

    def get_description(self):
        pass

    def get_price(self):
        pass

class MilkDecorator(AddOnDecorator):
    def get_description(self):
        return self._coffee.get_description() + 'Milked'

    def get_price(self):
        return self._coffee.get_price() + 50


coffee = Coffee()
coffee=MilkDecorator(coffee)
print(coffee.get_price())
print(coffee.get_description())
        