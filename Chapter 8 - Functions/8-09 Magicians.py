# C8-09 p.150 make a list of magicians names, pass it to a function
# and print the name of each

def show_magicians(magicians):
    for magician in magicians:
        print(f"It's Magician {magician}.")

magicians = ['Marvin', 'Ganderf', 'Bleck']

show_magicians(magicians)