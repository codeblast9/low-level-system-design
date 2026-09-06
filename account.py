from abc import ABC, abstractmethod

class Account(ABC):
    def __init__(self,balance):
        self.balance = balance

    @abstractmethod
    def deposit(self,amount):
        pass


class withdrawable(Account):
    def __init__(self, balance):
        super().__init__(balance)

    def withdraw(self,amount):
        if self.balance < amount:
            print("insufficient balance")
        else:
            self.balance -= amount
            print("amount withdrwan")

class SavingsAcc(withdrawable):
    def __init__(self, balance):
        super().__init__(balance)

    def display(self):
        print(f"balance is {self.balance}")

    def deposit(self, amount):
        self.balance += amount
        print(f"{amount}amount is being deposited to account, balance is {self.balance}")


class FixedDeposit(Account):
    def __init__(self, balance):
        super().__init__(balance)

    def deposit(self, amount):
        self.balance += amount
        print(f"{amount}amount is being deposited to account, balance is {self.balance}")

    def display(self):
        return self.balance
    





fd = FixedDeposit(1000)
fd.deposit(1000)