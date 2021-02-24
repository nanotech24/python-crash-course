#copy of the previous project

game = 'Modern Warfare'

#1
print("is game == 'Modern Warfare'? I believe it is.\n")
print(game == 'Modern Warfare')

#2
print("\nis game == 'Counter Strike'? I predict false.\n")
print(game == 'Counter Strike')

#3
chocolate = 'good'

print('\nis chocolate any good?\n')
print(chocolate == 'good')

#4
print('\nis chocolate bad?\n')
print(chocolate == 'bad')

#5
computer = 'on'

print('\nMy computer is currently on.\n')
print(computer == 'on')

#6
print('\nDid I turn my computer off?\n')
print(computer == 'off')

#7
my_phone = 'samsung'

print('\nMy phone was made by samsung.\n')
print(my_phone == 'samsung')

#8
print('\nMy phone is made by apple.\n')
print(my_phone == 'apple')

#9 using lower()
my_keyboard = 'RaZeR'
print('\nI have a razer keyboard. ' +str(my_keyboard.lower() == 'razer'))

#10 using lower()
print('\nI have a corsair keyboard. ' + str(my_keyboard.lower() == 'corsair'))

#test for equality in game var ==
print('\ngame variable has 14 characters: ' + str(len(game) == 14))

#test for inequality !=
print('\ngame variable has is not 20 characters: ' + str(len(game) != 20))

#Numerical test for equality
number = 24
print("\nthe number is equal to 24. " + str(number == 24))

#Numerical test for inequality
print('\nThe number is not 25. ' + str(number != 25))

#numerical test for greater than
print('\nThe number is greater than 10, ' + str(number > 10))

#numerical test for less than
print('\nThe number is less than 100. ' + str(number < 100))

#numerical test for greater than or equal to
print('\nThe number is greater than or equal to 22. ' + str(number >= 22))

#numerical test for less than or equal to
print('\nThe number is less than or equal to 27. ' + str(number <= 27))

#checking list for value

tlst = [
    'titties',
     'booty'
     ]

print('\nAre titties in the list? ' + str('titties' in tlst))

print('\nAre vajayjays in the list? ' + str('vajayjay' in tlst))

#checking list for not value
print('\nAre vajayjays not in list? ' + str('vajayjaty' not in tlst))

print('\nIs booty not in list? ' +str('booty' not in tlst))