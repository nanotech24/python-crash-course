# C8-03 p.141 Write a shirt function that accepts size and text to be printed.
# Call the function using positional arguments to make a shirt.
# Call it again a second time using keyword arguments

def make_shirt(size, text):
    """Creates a shirt at desired size and text"""

    print(
        f'You ordered a size {size} shirt, which will have "{text}" printed on it.\n'
        )


shirt_size = input('What size of shirt would you like to order?\n')

shirt_text = input('What text would you like written in the shirt?\n')

make_shirt(shirt_size, shirt_text)

# Calling the function a second time with keyword arguments

make_shirt(text=shirt_text, size=shirt_size)