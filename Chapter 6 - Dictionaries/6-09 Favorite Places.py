#C6-09 P.115 Favorite Places. make a dict called favorite_places. store names 
#askeys and lists as favorite places. Loop through and print

favorite_places = {
    'richard' : ["st. john's", 'mount pearl', 'salmonier line',],
    'sarah' : ["st.john's", 'montreal','salmonier line',],
    'maggie' : ['the park', 'outside', 'cuddles',],

}

for name, places in favorite_places.items():
    print(name.title() + "'s favorite places are: ")
    for place in places:
        print('\t' + place.title())