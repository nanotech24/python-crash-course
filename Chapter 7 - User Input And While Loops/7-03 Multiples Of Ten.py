#C7-03 P.121 ask for a number, and print if it is a multiple of ten.

number = int(input(
    'Please enter a number and I will check if it is a multiple of 10: '
    ))

if number % 10 == 0:
    print('The number is a multiple of 10!')

else:
    print('The number is not a multiple of 10.')