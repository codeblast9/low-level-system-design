'''
## this one is bad example
from abc import ABC, abstractmethod

class Food(ABC):
    @abstractmethod
    def prepare(self):
        pass


class Pizza(Food):
    def prepare(self):
        print("preparing pizza")

class Burger(Food):
    def prepare(self):
        print("preparing burger")


class restrauntOrder:
    def order_food(self, food_type:str):
        if food_type=="pizza":
            f = Pizza()
        elif food_type=="burger":
            f = Burger()
        else:
            print("Not available currently order something else")
            return None
        f.prepare()
        return f


res = restrauntOrder()
res.order_food("pizza")
'''

from abc import ABC, abstractmethod


class Food(ABC):
    @abstractmethod
    def prepare(self):
        pass


class Pizza(Food):
    def prepare(self):
        print("preparing pizza")

class Burger(Food):
    def prepare(self):
        print("preparing burger")


class FoodFactory:
    @staticmethod
    def create_food(food_type:str)-> Food:
        if food_type=="pizza":
            return Pizza()
        elif food_type=="burger":
            return Burger()
        else:
            return None

class RestrauntService:
    def create_order(self,food_type:str):
        f= FoodFactory.create_food(food_type)
        if f is None:
            print("order something else")
            return None
        f.prepare()
        return f

res = RestrauntService()
res.create_order("pasta")

