# C8-12 p.154

# Make sandwich function which takes arbitrary number of toppings and has a default bread
def make_sandwich(*toppings, bread='white'):
    print(f'making a sandwich on {bread} bread and with:\n')
    for t in toppings:
        print(f'- {t}')

# Gathering the toppings for the make sandwich function into a list
def gather_toppings():
    gtoppings = []
    gathering = True
    while gathering:
        g = input('What topping would you like?: \n')
        if g == 'q':
            gathering = False

        else:
            gtoppings.append(g)
    # Returning the list
    return gtoppings

# getting the list of toppings
sandwich = gather_toppings()

# Note when passing a list as args, the usage of the * before hand
mysandwich = make_sandwich(*sandwich, bread='Whole Wheat')
