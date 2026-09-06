## bad example which violets open closed principle
class Chef:
    def cook_pasta(self):
        print("chef is cooking pasta")

    def cook_pizza(self):
        print("chef is cooking pizza")

    def cook_burger(self):
        print("chef is making burger")

class Waiter:
    def __init__(self, chef:Chef):
        self.__chef = chef


    def take_order(self, item:str):
        if item =="pasta":
            self.__chef.cook_pasta()
        elif item == "pizza":
            self.__chef.cook_pizza()
        else:
            print("cannot take order")



from abc import ABC, abstractmethod

class Order(ABC):
    @abstractmethod
    def execute(self):
        pass

class PizzaOrder(Order):
    def __init__(self,chef:Chef):
        self.__chef = chef

    def execute(self):
        print("chef is making Pizza")
        self.__chef.cook_pizza()

class PastaOrder(Order):
    def __init__(self, chef:Chef):
        self.__chef = chef


    def execute(self):
        print("chef is making pasta")
        self.__chef.cook_pasta()

class BurgerOrder(Order):
    def __init__(self, chef:Chef):
        self.__chef = chef

    def execute(self):
        print("chef is making Burger")
        self.__chef.cook_burger()


