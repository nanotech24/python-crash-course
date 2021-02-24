#5-06 Write an if-elif-else statement as instructed on page 89

pAge = 1

if pAge < 2:
    print('This person is a baby.')

elif pAge >= 2 and pAge < 4:
    print('This person is a toddler') 

elif pAge >= 4 and pAge < 13:
    print('This person is a kid')

elif pAge >= 13 and pAge < 20:
    print('This person is teenager.')

elif pAge >= 20 and pAge < 65:
    print('This person is an adult')

else:
    print('This person is an elder')