# C8-14 p.154 Cars

# Write a function that creates car dict, takes 2 args, manufacture and model, then accept and arbitrary no of kwargs

def Make_Car(manu, model, **kwargs):

    # If you know a few items of a dict, create it like this instead of the method shown in C8-13
    car = { 'manufacturer' : manu, 'model' : model}

    for k, v in kwargs.items():
        car[k] = v

    return car


car = Make_Car('Chevrolet', 'Corvette', color='red', supersport=True)

print(car)
