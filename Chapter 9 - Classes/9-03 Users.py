# C9-03 p.166 Users

class User:
    """A class to model a user"""

    def __init__(self, first_name, last_name, age, height, weight):

        self.first_name = first_name
        self.last_name = last_name
        self.age = age
        self.height = height
        self.weight = weight

    def describe_user(self):
        self.full_name = self.first_name + ' ' + self.last_name
        print(
            f'{self.full_name.title()} is {self.age} years old, {self.height} meters tall, and {self.weight} kilograms.'
        )

    def greet_user(self):
        print(f'Hello {self.full_name.title()}!')


bob = User('Bob', 'Loblaw', 52, 175, 101)

bob.describe_user()

bob.greet_user()

fred = User('Fred', 'Bear', 35, 185, 85)

fred.describe_user()

fred.greet_user()

george = User('george', 'strombolopolis', 42, 167, 80)

george.describe_user()

george.greet_user()
