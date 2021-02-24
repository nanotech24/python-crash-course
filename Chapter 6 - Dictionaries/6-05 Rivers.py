#6-05 p.108 make a dict containing 3 major rivers and the country it runs
#print a sentence about each river, then the river name, then the country

river_dict = {
    'nile' : 'egypt',
    'mississippi' : 'missouri',
    'mackenzie' : 'canada',
    }

#looping through keys and values with .items()
for river, country in river_dict.items():
    print('The ' + river.title() + 
    ' river is found in ' + country.title() + '.\n'
    )

#looping through keys is the default behaviour, but .keys() can be used too
for river in river_dict:
    print('River name: ' + river.title() + '.\n')

#looping through values using .valueS()
for country in river_dict.values():
    print('Country name: ' + country.title() + '.\n')