# C9-05 p.171 Login Attempts

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

# Creating a user
user_1 = User('Richard', 'Sharpe', 26, 175, 95)

# attempting a log in
user_1.increment_login_attempts()
print(f'There have been {user_1.login_attempts} attempts to log in')

# Simulating the user attempting to log in 5 times
for i in range (1,6):
    user_1.increment_login_attempts()

print(f'There have been {user_1.login_attempts} attempts to log in')

user_1.reset_login_attempts()
print(f'There have been {user_1.login_attempts} attempts to log in')