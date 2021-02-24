#6-06 P.108 polling. make a list of those who should take the poll
#Include some names that did and some that did not
#loop through the list and 

favorite_languages = {
    'jen' : 'python',
    'sarah' : 'c',
    'edward' : 'ruby',
    'phil' : 'python'
    }

should_poll = ['jen','sarah','richard','jordan']

for p in should_poll:

    if p in favorite_languages.keys():
        print(
            'Thank you ' + p.title() + ' for responding!\n'
            )

    else:
        print(
            'Hello ' + p.title() + ', would take a moment to answer a poll?\n'
            )