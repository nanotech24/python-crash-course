#C6-12 P.115 using one of the programs from this chapter, extend something
#you have written with more keys,values, or improve the output formatting.


#I have chosen the first project. I will loop through output



person_dict = {

    'first name' : 'Richard',
    'last name' : 'Sharpe',
    'age' : '26',
    'city' : 'Mount Pearl',

    }

#non looping pring method
print(
    person_dict['first name'] + ' ' + person_dict['last name'] + ' is ' +
    person_dict['age'] + ' years old and lives in ' + person_dict['city'] +
    '.\n'
)

# new looping print method using if else

for key, value in person_dict.items():
    if key == 'age':
        print(
            key.title() + ' is ' + value + ' years old.'
        )

    else:
        print(
            key.title() + ' is ' + value.title() + '.'
        )