# Defining the function to copy and add to the list
def make_great(magicians):
    '''Take a list of magicians, add "The Great" to the end'''

    # Copying the list
    greatmagicians = magicians[:]

    # Using var i as an iterator number
    i = 0

    # Adding to each list item, then move to next index
    for m in greatmagicians:
        greatmagicians[i] += ' The Great'
        i += 1

    # Returning the new list
    return greatmagicians


# Defining a function to print the magicians
def show_magicians(magicians):
  '''A Funtion to print the list of magicians'''
  for m in magicians:
    print(m)
