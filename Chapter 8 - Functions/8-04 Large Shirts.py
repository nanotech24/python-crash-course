# C8-08 p141 Modify the make_shirt function so that shirts are large by default
# And have a message that reads "I love Python"
# Make a large shirt and a medium shirt with the default message
# Make a shirt of any size with a different message

def make_shirt(size='Large', text='I Love Python'):
    """Creates a shirt at desired size and text"""

    print(
        f'You ordered a size {size} shirt, which will have "{text}" printed on it.\n'
        )


make_shirt()

make_shirt('Medium')

make_shirt('small', 'I love C#')