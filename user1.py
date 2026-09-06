
class User:
    def __init__(self, name, age, email):
        self.name = name
        self.age = age
        self.email = email

    def display_info(self):
        print(f"{self.name} is of {self.age} age.")

    def is_adult(self):
        return self.age > 18
    