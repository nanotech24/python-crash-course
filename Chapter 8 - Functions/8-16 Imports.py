# C8-16 p.159 Imports

# Defining the list of magicians to be modified
# REMEMBER, IMPORTS USUALLY GO AT THE TOP OF THE FILE, THIS IS JUST FOR THE EXERCISE
mymagicians = ['Bob', 'Fred', 'Joe']


# Importing myfuncs with an alias
import magicianfuncs as greatmagician

mygreatmagicians = greatmagician.make_great(mymagicians)

greatmagician.show_magicians(mygreatmagicians)
print('\n')

# Importing myfuncs as itself
import magicianfuncs

mygreatmagicians2 = magicianfuncs.make_great(mymagicians)

magicianfuncs.show_magicians(mygreatmagicians2)
print('\n')

# Importing a single function from myfuncs

from magicianfuncs import make_great

mygreatmagicians3 = make_great(mymagicians)

for m in mygreatmagicians3:
    print(m)

print('\n')

# Importing the module with an alias

import magicianfuncs as mf

mygreatmagicians4 = mf.make_great(mymagicians)

mf.show_magicians(mygreatmagicians4)
print('\n')

# Importing all functions from the module, note that this may cause conflict if things are named similarly
# Works the same as line 24, but I will use the other function in myfuncs to show that it worked

from magicianfuncs import *

show_magicians(mygreatmagicians4)