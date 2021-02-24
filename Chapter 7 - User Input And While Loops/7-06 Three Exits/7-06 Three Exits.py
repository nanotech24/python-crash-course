#C7-07 P.128 see page example. re writing 7-05

age = int(input('What is your age?: '))

age_free = 3

age_range = list(range(3,12))


prices = ['Free', '$10', '$15']


#Now going to do the same using a conditional test


active = 0

while active < 1:
    if age < age_free:
        print(f'Your ticket will be {prices[0]}.')
        active += 1

    elif age in age_range:
        print(f'Your ticket cost will be {prices[1]}.')
        active += 1

    else:
        if age not in age_range:
            print(f'Your ticket cost will be {prices[2]}.')
            active += 1