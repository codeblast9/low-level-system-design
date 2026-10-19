from typing import List
class LoginService:
    def login(self, username:str, password:str)->dict:
        print(f"[login service] logging the user {username}")
        return {"user-id":"u-123", "username":username}

    def get_profile(self,user_id:str)->dict:
        print(f"[login service] getting user if for {user_id}")
        return{"user_id":user_id, "name":"Priyanshu","Address": "Mumbai"}

class OrderService:
    def get_order(self,user_id:str)->List:
        print(f"[Orderservice] getting orders list for:{user_id}")
        return [
            {"order_id":"ord11", "total":20000},
            {"order_id":"ord21", "total":15000},
        ]

class APIGateway:
    def __init__(self):
        self.__user_login = LoginService()
        self.__order_service = OrderService()

    def user_login(self, username:str, password:str):
        self.__user_login.login(username, password)

    def user_profile(self,user_id):
        self.__user_login.get_profile(user_id)

    def get_oders(self,user_id):
        self.__order_service.get_order(user_id)

    def all_details(self, username:str, password:str, userId:str):
        self.__user_login.login(username, password)
        self.__user_login.get_profile(userId)
        self.__order_service.get_order(userId)



api = APIGateway()
api.all_details("priyanshu","pass123","a123")