from User import *

class Privileges:
    """A class to represent privileges a user possesses"""

    def __init__(self):
        self.privileges = ('can delete post', 'can ban user', 'can promote user', 'can change motd')



class Admin(User):
    """A subclass of User, for administrators."""

    def __init__(self, first_name, last_name, age, height, weight):

        super().__init__(first_name,last_name,age, height, weight)

        self.priv_list = Privileges()


    def show_privileges(self):
        """Show the list of admin privileges"""

        print(f'Hello {self.first_name} you are an Administrator, Your current privileges are:\n')

        # Watch the naming conventions when using a class as an attribute, things can get confusing, FAST
        for p in self.priv_list.privileges:
            print(f'  -{p}')


