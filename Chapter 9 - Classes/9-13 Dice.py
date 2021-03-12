# C9-13 p.181(v2) Dice
from random import randint


class Dice:
    """A simple model to roll different types of Dice"""

    def __init__(self, sides=6):

        self.sides = sides

    def roll_die(self, roll_count=1):
        """Roll the die"""

        current_roll = 0

        while current_roll < roll_count:

            die_roll = randint(1, self.sides)

            print(f'The die rolls a {die_roll}')

            current_roll += 1

        print('\n'.lstrip())


six_sided_die = Dice()

six_sided_die.roll_die(10)

ten_sided_die = Dice(10)

ten_sided_die.roll_die(10)

twenty_sided_die = Dice(20)

twenty_sided_die.roll_die(10)

