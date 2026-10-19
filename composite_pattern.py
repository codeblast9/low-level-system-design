from typing import List
from abc import ABC, abstractmethod

class Systemcomponent(ABC):
    @abstractmethod
    def show_details(self):
        pass

class File(Systemcomponent):
    def __init__(self,name:str):
        self.__name = name

    def show_details(self):
        return f"File Name: {self.__name}"


class Folder(Systemcomponent):
    def __init__(self,name:str):
        self.__name = name
        self.__components:List[Systemcomponent] = []

    def add_components(self,component:Systemcomponent):
        self.__components.append(component)

    def show_details(self):
        print(f"Folder Name: {self.__name}")
        for component in self.__components:
            print(component.show_details())


file1 = File("image1.png")
file2 = File("image2.png")
file3 = File("image3.png")

sub_folder = Folder("subFolder")
doc1 = File("doc1")
doc2 = File("doc2")
doc3 = File("doc3")

sub_folder.add_components(doc1)
sub_folder.add_components(doc2)
sub_folder.add_components(doc3)

main_fol=Folder("Main")
main_fol.add_components(file1)
main_fol.add_components(file2)
main_fol.add_components(file3)
main_fol.add_components(sub_folder)

main_fol.show_details()