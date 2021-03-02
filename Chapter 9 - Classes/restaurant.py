class Restaurant:
    """A class to represent a restaurant"""
    def __init__(self, restaurant_name, cuisine_type):
        self.restaurant_name = restaurant_name
        self.cuisine_type = cuisine_type

    def describe_restaurant(self,):
        """Describe the Restaurant"""
        print(f'Welcome to {self.restaurant_name}, here we serve {self.cuisine_type}')

    def open_restaurant(self):
        print(f'{self.restaurant_name} is open for business!')