#C7-05 P.127 A movie ticket cost varies base on age. if under 3 its free
#if between 3 and 12, it is $10; and if they are over 12, it is $15.

age = int(input('What is your age?: '))

age_free = 3

age_range = list(range(3,12))


prices = ['Free', '$10', '$15']


#while loop using a flag, keep in mind for this exercise a break statement
#can also be used.

active = True

while active == True:
    if age < age_free:
        print(f'Your ticket will be {prices[0]}.')
        active = False

    elif age in age_range:
        print(f'Your ticket cost will be {prices[1]}.')
        active = False

    else:
        if age not in age_range:
            print(f'Your ticket cost will be {prices[2]}.')
            active = False