from abc import ABC, abstractmethod

class PaymentMethod(ABC):
    @abstractmethod
    def pay(self, amount:int):
        pass


class UPIPayment(PaymentMethod):
    def pay(self, amount:int):
        print(f"making payment through upi of amount:{amount}")


class debitcardpayment(PaymentMethod):
    def pay(self,amount:int):
        print(f"making payment through debit card of amount:{amount}")

class creditcard(PaymentMethod):
    def pay(self, amount:int):
        print(f"making payment through credit card of amount:{amount}")


class PaymentProcessor:
    def process_payment(self, payment_method:PaymentMethod, amount:int):
        payment_method.pay(amount)
