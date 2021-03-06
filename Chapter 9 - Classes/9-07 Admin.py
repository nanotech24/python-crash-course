# C9-07 p.178 Admin

# Starting with the User class I wrote in exercise 9-05
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


class Admin(User):
    """A subclass of User, for administrators."""

    def __init__(self, first_name, last_name, age, height, weight):

        super().__init__(first_name,last_name,age, height, weight)

        self.privileges = ('can delete post', 'can ban user', 'can promote user', 'can change motd')

    def show_privileges(self):
        """Show the list of admin privileges"""

        print(f'Hello {self.first_name} you are an Administrator, Your current privileges are:\n')

        for p in self.privileges:
            print(f'  -{p}')

ricardo = Admin('Richard', 'Sharpe', '26', 175, 95)

ricardo.show_privileges()