#store 5 peoples favorite numbers in a dict

fav_numbers = {
    'richard' : '24',
    'sarah' : '69',
    'brandon' : '54',
    'kayla' : '18',
    'rebecca' : '21'
    }

#print the name and number
print(
    "Richard's favorite number is " + fav_numbers['richard'] + '.\n' + 
    "Sarah's favorite number is " + fav_numbers['sarah'] + '.\n' +
    "Brandon's favorite number is " + fav_numbers['brandon'] + '.\n' +
    "Kayla's favorite number is " + fav_numbers['kayla'] + '.\n' +
    "Rebecca's favorite number is " + fav_numbers['rebecca'] + '.\n'
    )


#same thing accomplished above with a for loop.
for k, v in fav_numbers.items():
    print(k.title() + "'s favorite number is " + v + '.')
