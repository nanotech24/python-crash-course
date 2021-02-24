#C6-10 P.115 start with program from 6-02. make it so each person has 
#multiple favorite numbers. print each name and number



fav_numbers = {
    'richard' : ['24', '54', '69',],
    'sarah' : ['69','28','18',],
    'brandon' : ['54','666','45',],
    'kayla' : ['18','23'],
    'rebecca' : ['21', '22', '26',],
    }


for name, numbers in fav_numbers.items():
    print(name.title() + "'s Favorite numbers are: ")
    for number in numbers:
        print('\t' + number)