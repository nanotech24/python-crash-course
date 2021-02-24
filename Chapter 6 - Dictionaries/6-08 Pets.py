#6-08 P.115 Make several dicts with the name of each being a pet
#include type of animal and the name. store dicts in a list
#loop through info

maggie_dict = {
    'name' : 'maggie',
    'pet type' : 'dog',
    'owner' : 'richard',
    }

rigatoni_dict = {
    'name' : 'rigatoni',
    'pet type' : 'snake',
    'owner' : 'richard',
    }

angel_dict = {
    'name' : 'angel',
    'pet type' : 'dog',
    'owner' : 'sarah',
    }

pets = [maggie_dict, rigatoni_dict, angel_dict]

for pet in pets:
    print(pet['name'].title() + ' is a ' + 
    pet['pet type'] + ' and is owned by ' + 
    pet['owner'].title() + '.\n'
    )