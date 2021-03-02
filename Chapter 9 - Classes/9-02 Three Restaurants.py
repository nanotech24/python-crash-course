# c9-02 p.166 Three Restaurants
# I'm Going to take it one step further, and use an import
# restaurant.py was created to use as a module for this exercise
from restaurant import Restaurant

pizza_place = Restaurant('Pizza Pros', 'Pizza')

pizza_place.describe_restaurant()
print('\n')

burger_joint = Restaurant('Burger King', 'Flame Broiled Burgers')

burger_joint.describe_restaurant()
print('\n')

coffee_shop = Restaurant('Tim Hortons', 'Hot Coffee And Baked Goods')

coffee_shop.describe_restaurant()
