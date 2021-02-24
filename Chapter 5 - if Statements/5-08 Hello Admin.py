#C5-08 page 93

#defining list of names and looping through list
#printing a special message for the admin
user_names = ['admin', 'chett','matt','bob','jason']

for n in user_names:
    if n == 'admin':
        print('Hello Admin! Would you like to see a status report?')
    else:
        print('Hello ' + n.title() + ', Thanks for logging in again!')