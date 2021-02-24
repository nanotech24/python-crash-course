#C7-07 P.128 see page example. re writing 7-05

age_free = '3'

age_range = list(str(range(3,12)))

prices = ['Free', '$10', '$15']

#Now going to do the same using a break statement to let the user quit.

message = ''

while message != 'quit':

    age = input('What is your age?: ')

    if age < age_free:
        print(f'Your ticket will be {prices[0]}.')       

    elif age in age_range:
        print(f'Your ticket cost will be {prices[1]}.')

    elif age == 'quit':
        break
    
    elif age not in age_range:
        print(f'Your ticket cost will be {prices[2]}.')
