# C9-06 p.178 Ice Cream Stand

class Restaurant:
    """A class to represent a restaurant"""
    def __init__(self, restaurant_name, cuisine_type):
        self.restaurant_name = restaurant_name
        self.cuisine_type = cuisine_type

    def describe_restaurant(self):
        """Describe the Restaurant"""
        print(f'Welcome to {self.restaurant_name}, here we serve {self.cuisine_type}')

    def open_restaurant(self):
        """The Restaurant is open"""
        print(f'{self.restaurant_name} is open for business!')



class IceCreamStand(Restaurant):
    """A class inheriting from the restaurant class for an Ice Cream Stand"""

    def __init__(self, restaurant_name, cuisine_type):
        """
        Initialize attributes of the parent class,
        Then initialize attributes specific to an electric car
        """

        # Notice when creating subclass, the super()__init__ does note require "self"
        # And that super() goes inside the __init__ definition
        super().__init__(restaurant_name, cuisine_type)

        # Adding an attribute that stores a list of flavors
        self.flavors = ['Chocolate Chip', 'Banana Nut', 'Oreo']

    # Show the flavors served
    def show_flavors(self):
        """Show available ice cream flavors"""
        print('The Flavors we have available are:\n')
        for f in self.flavors:
            print(f'  -{f}')


# Creating an instance of IceCreamStand
ice_cream = IceCreamStand('Dairy Queen', 'Blizzard')

# Showing flavors available with the show_flavors() method, exclusive to the subclass
ice_cream.show_flavors()
