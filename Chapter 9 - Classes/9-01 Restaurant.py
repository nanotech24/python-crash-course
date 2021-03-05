# C9-01 p.166 Restaurant

# Create a class for a restaurant with 2 attributes
# Define a method to describe the restaurant
# Define another method that indicates the restaurant is open

class Restaurant:
    """A class to represent a restaurant"""
    def __init__(self, restaurant_name, cuisine_type):
        self.restaurant_name = restaurant_name
        self.cuisine_type = cuisine_type

    def describe_restaurant(self):
        """Describe the Restaurant"""
        print(f'Welcome to {self.restaurant_name}, here we serve {self.cuisine_type}')

    def open_restaurant(self):
        print(f'{self.restaurant_name} is open for business!')


restaurant = Restaurant('Pizza Pros', 'Pizza')

print(restaurant.restaurant_name, '\n')
print(restaurant.cuisine_type, '\n')

restaurant.describe_restaurant()
restaurant.open_restaurant()
