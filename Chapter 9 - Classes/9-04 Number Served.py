# C9-04 p.171 Number Served

class Restaurant:
    """A class to represent a restaurant"""
    def __init__(self, restaurant_name, cuisine_type):
        self.restaurant_name = restaurant_name
        self.cuisine_type = cuisine_type
        self.number_served = 0

    def describe_restaurant(self):
        """Describe the Restaurant"""
        print(f'Welcome to {self.restaurant_name}, here we serve {self.cuisine_type}')

    def open_restaurant(self):
        print(f'{self.restaurant_name} is open for business!')

    def set_number_served(self, number_to_set):
        """Set how many people were served in the restaurant"""
        self.number_served = number_to_set

    def increment_number_served(self, increment=1):
        """Increment the number of people served by a specified amount"""
        self.number_served = self.number_served + increment


restaurant = Restaurant('Pizza Pros', 'Pizza')

print(restaurant.number_served)

restaurant.number_served = 10

print(restaurant.number_served)

restaurant.set_number_served(20)

print(restaurant.number_served)

restaurant.increment_number_served()

print(restaurant.number_served)
