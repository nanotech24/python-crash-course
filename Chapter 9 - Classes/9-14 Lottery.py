# C9-14 p.181(v2) Lottery

from random import choices

lottery_numbers = ['0', '1', '3', '4', '5', '6', '7', '8', '9', 'a', 'b', 'c', 'd', 'e']

winning_numbers = choices(lottery_numbers, k = 4)

print(f'The winning numbers are {"".join(winning_numbers)}')

