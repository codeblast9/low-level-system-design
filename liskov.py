from abc import ABC, abstractmethod

def Bankaccount(ABC):
    def __init__(self,balance):
        self.balance = balance

    @abstractmethod
    def withdraw(self):
        pass

    @abstractmethod
    def deposit(self):
        pass


class SavingsAccount(Bankaccount):
    def __init__(self,balance):
        super.__init__(balance)

    def withdraw(self,amount:int):
        if self.balance < amount:
            print("no sufficient balance")
        else:
            self.balance -= amount
            print(f"{amount} withdrawn, remaining balance is {self.balance}")
    
    def deposit(self, amount):
        self.balance += amount
        print(f"{amount} is being deposited in bank acc")

