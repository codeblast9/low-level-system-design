## this is a bad example
from abc import ABC, abstractmethod

class Starters(ABC):
    @abstractmethod
    def prepare(self):
        pass

class MainCourse(ABC):
    @abstractmethod
    def prepare(self):
        pass

class Desserts(ABC):
    @abstractmethod
    def prepare(self):
        pass
### accessories daily carry use
class MeduVada(Starters):
    def prepare(self):
        print("preparing Meduvada")

class Dosa(MainCourse):
    def prepare(self):
        print("preparing Dosa")

class Payasum(Desserts):
    def prepare(self):
        print("preparing Payasum")

## home accessories
class PaneerTikka(Starters):
    def prepare(self):
        print("preparing PaneerTikka")

class Seekhkabab(MainCourse):
    def prepare(self):
        print("preparing kebabs")

class GulabJamun(Desserts):
    def prepare(self):
        print("preparing Gulabjamun")

##work/ gaming accessories

class Rolls(Starters):
    def prepare(self):
        print("preparing rolls")

class FriedRice(MainCourse):
    def prepare(self):
        print("preparing FriedRice")

class FortuneCookies(Desserts):
    def prepare(self):
        print("preparing cookies")

class CuisuineFactory(ABC):
    @abstractmethod
    def create_starter(self)-> Starters:
        pass

    @abstractmethod
    def create_Main(self)->MainCourse:
        pass 

    @abstractmethod
    def create_dessert(self)->Desserts:
        pass

class NorthIndianCuisuine(CuisuineFactory):
    def create_starter(self):
        return PaneerTikka()

    def create_Main(self):
        return Seekhkabab()

    def create_dessert(self):
        return GulabJamun()

class SouthIndianCuisuine(CuisuineFactory):
    def create_starter(self):
        return MeduVada()

    def create_Main(self):
        return Dosa()

    def create_dessert(self):
        return Payasum()

class ChineseCuisuine(CuisuineFactory):
    def create_starter(self):
        return Rolls()

    def create_Main(self):
        return FriedRice()

    def create_dessert(self):
        return FortuneCookies()
    

class OrderService:
    def __init__(self,factory:CuisuineFactory):
        self.__factory = factory

    def create_meal(self):
        starter = self.__factory.create_starter()
        main = self.__factory.create_Main()
        dessert = self.__factory.create_dessert()

        starter.prepare()
        main.prepare()
        dessert.prepare()

    def change_cuisuine(self,new_factory:CuisuineFactory):
        self.__factory = new_factory

northindian = NorthIndianCuisuine()
restraunt = OrderService(northindian)
restraunt.create_meal()
chinese = ChineseCuisuine()
restraunt.change_cuisuine(chinese)
restraunt.create_meal()
    

        

     