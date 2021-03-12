# C9-15 p.181(v2) Lottery Analysis

from random import choices

lottery_numbers = ['0', '1', '2', '3', '4', '5', '6', '7', '8', '9', 'a', 'b', 'c', 'd', 'e']


my_ticket = ['2', '4', 'e', 'd']

attempts = 0

winner = False
while not winner:

    winning_numbers = choices(lottery_numbers, k=4)

    if my_ticket == winning_numbers:

        print(f'You won! it took {attempts} tries to win!')
        winner = True

    else:
        attempts += 1
        print(attempts, winning_numbers )
