from abc import ABC, abstractmethod


class DiscountStrategy(ABC):
    @abstractmethod
    def calculate_discount(self):
        pass

class DiwaliDiscount(DiscountStrategy):
    def calculate_discount(self):
        print("applying the diwali discount of 20%")

class HoliDiscount(DiscountStrategy):
    def calculate_discount(self):
        print("applying the Holi discount of 10%")

class GanpatiDiscount(DiscountStrategy):
    def calculate_discount(self):
        print("applying the ganesh chaturthi discount of 30%")



class DiscountService:
    def __init__(self,discount_strategy:DiscountStrategy):
        self.__strategy = discount_strategy

    def set_strategy(self,new_discount_strategy:DiscountStrategy):
        self.__strategy = new_discount_strategy

    def process(self):
        self.__strategy.calculate_discount()


        