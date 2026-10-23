class Location:
    def __init__(self,lat:float, long:float):
        self.__latitude:float = lat
        self.__longitude:float = long

    def get_latitude(self)->float:
        return self.__latitude

    def get_longitude(self)->float:
        return self.__longitude
    

        