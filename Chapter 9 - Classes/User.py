class User:
    """A class to model a user"""

    def __init__(self, first_name, last_name, age, height, weight):
        self.first_name = first_name
        self.last_name = last_name
        self.age = age
        self.height = height
        self.weight = weight
        self.login_attempts = 0

    def describe_user(self):
        self.full_name = self.first_name + ' ' + self.last_name
        print(
            f'{self.full_name.title()} is {self.age} years old, {self.height} meters tall, and {self.weight} kilograms.'
        )

    def greet_user(self):
        print(f'Hello {self.full_name.title()}!')

    def increment_login_attempts(self):
        """Increment the value of login attempts by 1"""

        self.login_attempts += 1

    def reset_login_attempts(self):
        """Reset the login counter"""

        self.login_attempts = 0


