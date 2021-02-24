#C6-11 P.115 Make a dict called cities. use 3 cities as keys.
#Create a dict for some information about each city, using keys to describe



cities = {
    "st. john's" : {
        'country' : 'canada',
        'population' :  "108,900",
        'fact' : 'This is the oldest city in North America.',
        },
    
    'new york' : {
        'country' : 'United States',
        'population' : '8,398,748',
        'fact' : 'More than 800 languages are spoken in New York City. Yes, 800!',
        },
    
    'venice' : {
        'country' : 'italy',
        'population' : '260,900',
        'fact' : 'venice is built on logs.',
        },
    }

for city, info in cities.items():
    print('Here is some info about ' + city.title() + ':')
    for label, fact in info.items():
        print('\t' + label.title() + ': ' + fact.title()) 