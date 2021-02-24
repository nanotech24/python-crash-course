#C5-10 p.93

current_users = ['dave','bob','chad','mike','brad']

new_users = ['DAVE','brad','chris']

for user in new_users:   
    
    #I got stuck here with this part
    #using a list comprehension to compare new_user titles to current_user titles
    if user.title() in [user.title() for user in current_users]:
        print('The username "' + user + '" is unavailable. Please choose a different name')

    else:
        print('the name "' + user + '" is available.')
    