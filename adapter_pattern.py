'''The adapter pattern is a design pattern that lets 2 systems or components that werent designed to work together communicate with
each other by creating a bridge between them.'''

from abc import ABC, abstractmethod

class NotificationsService(ABC):
    @abstractmethod
    def send(self):
        pass


class EmailNotificationService(NotificationsService):
    def send(self,to:str, title:str, body:str):
        print(f"sending email through EmailNotificationService....")
        print(f"sending to {to}")
        print(f"Title:{title}")
        print(f"Body:{body}")


class SendGridService:
    def send_email(self,recipient:str,subject:str,content:str):
        print(f"sending email through EmailNotificationService....")
        print(f"sending to {recipient}")
        print(f"Title{subject}")
        print(f"Body:{content}")

class SendGridAdapter(NotificationsService):
    def __init__(self,email_grid_service:SendGridService):
        self.__email_notify_service = email_grid_service

    def send(self,to: str, title:str, body:str):
        self.__email_notify_service.send_email(to,title, body)
         
class OrderService:
    def __init__(self, email_service:NotificationsService):
        self.__email_service = email_service

    def create_order(self):
        self.__email_service.send("priyanshujadhav117@gmail.com","application","request to join")


email_notification = SendGridService()
send_grid_adapter = SendGridAdapter(email_notification)
order_serv = OrderService(send_grid_adapter)
order_serv.create_order()

