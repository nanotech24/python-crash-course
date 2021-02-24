# C7-09 p.131

# Starting with the list sandwich_orders and adding 'pastrami' 3 times

sandwich_orders = ['bologna', 'chicken', 'cold cut', 'steak', 'grilled cheese', 'pastrami', 'pastrami', 'pastrami', ]

print(f'The deli has run out of {sandwich_orders[5]}.')

while 'pastrami' in sandwich_orders:
    sandwich_orders.remove('pastrami')

print(f"{', '.join(sandwich_orders).title()} sandwiches were all made!")