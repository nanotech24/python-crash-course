#C7-03 P.127 Write a loop that promps the user to enter toppings until they
#enter a quit value. print a message saying you'll add each topping

added_toppings = []


active = True

while active:
    topping = input('Please enter the toppings you would like: ')

    

    if topping != 'quit':
        print('Adding ' + topping + ' to your order.')

        added_toppings.append(topping)
    

    else:
        print('quitting program')
        active = False
