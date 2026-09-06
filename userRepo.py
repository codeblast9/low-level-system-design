from user1 import User

class UserRepo:
    def __init__(self,db, host, password):
        self.__db = db
        self.__host = host
        self.__password = password

    def display_user(self,user:"User"):
        print(f"My name is {user.name} and age is {user.age}")
    
    def display_db_info(self):
        print(f"db name is {self.__db}, hostname:{self.__host}, password:{self.__password}")

    def add(self):
        print("data is getting saved in db")

    def delete(self):
        print("the data is being deleted")