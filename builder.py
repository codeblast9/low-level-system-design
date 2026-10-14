'''class Laptop:
    def __init__(self,processor:str,ram:str,storage:str, color:str=None,graphics:str = None):
        self.processor = processor
        self.ram = ram
        self.storage = storage
        self.color = color
        self.graphics = graphics

    def display_config(self):
        print(f"Processor: {self.processor}")
        print(f"RAM:{self.ram}GB")
        print(f"storage:{self.storage}GB")
        if self.color:
            print(f"colorcase:{self.color}")
        if self.graphics:
            print(f"graphic card:{self.graphics}")

laptop = Laptop("i7","8GB","512SSD","black","iris")
laptop.display_config()'''
# the above is the bad example

class Laptop:
    processor: str
    ram:str
    storage:str
    graphics:str = None
    screen_size:str = None
    color:str = None

    def display_specs(self):
        if self.processor:
            print(f"Processor:{self.processor}")
        if self.ram:
            print(f"RAM:{self.ram}GB")
        if self.storage:
            print(f"Storage:{self.storage}GB")
        if self.graphics:
            print(f"graphic card:{self.graphics}")
        if self.screen_size:
            print(f"Screensize:{self.screen_size}")
        if self.color:
            print(f"Body color:{self.color}")

class LaptopBuilder:
    def __init__(self):
        self.__laptop = Laptop()

    def set_processor(self,processor:None):
        self.__laptop.processor = processor
        return self

    def set_ram(self,ram:None):
        self.__laptop.ram = ram
        return self

    def set_storage(self,storage:None):
        self.__laptop.storage = storage
        return self

    def set_graphics(self,graphics:None):
        self.__laptop.graphics = graphics
        return self
    def set_screensize(self,screen_size:None):
        self.__laptop.screen_size = screen_size
        return self
    def set_color(self,color:None):
        self.__laptop.color = color
        return self

    def build(self):
        return self.__laptop

l1=LaptopBuilder().set_processor("i7").set_ram("8GB").set_storage("512SSD").build()
print(l1.display_specs())