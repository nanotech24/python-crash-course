# C8-10 p.150 make a function that adds the word great

def show_magicians(magicians):
    for magician in magicians:
        print(f"It's Magician {magician}.")


def make_great(magicians):
    great_magicians = []
    for magician in magicians:
        great = f'Great {magician}'

        great_magicians.append(great)

    return great_magicians


magicians = ['Marvin', 'Ganderf', 'Bleck']

show_magicians(magicians)

great_magicians = make_great(magicians)

show_magicians(great_magic)