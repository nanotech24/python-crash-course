#C6-07 P.114 start with program from 6-01 and make 2 new people dics.
#Store all dicts in a list, and loop through each printing the info inside

richard_dict = {

    'first_name' : 'Richard',
    'last_name' : 'Sharpe',
    'age' : '26',
    'city' : 'Mount Pearl',

    }

sarah_dict = {
    'first_name' : 'Sarah',
    'last_name' : 'Sloan',
    'age' : '25',
    'city' : 'Mount Pearl',

    }

brandon_dict = {
    'first_name' : 'Brandon',
    'last_name' : 'Drover',
    'age' : '26',
    'city' : 'goulds',
    }

people = [richard_dict, sarah_dict, brandon_dict]

for person in people:

    print(
        person['first_name'] + ' ' + person['last_name'] + ' is ' +
        person['age'] + ' years old and lives in ' + person['city'].title() +'\n'
        )