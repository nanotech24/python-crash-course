#Choose a version of foods.py
#write two for loops to print each list of foods

my_foods = ['pizza','felafel','carrot cake']

friend_foods = my_foods[:]

for f in my_foods:
    print(f, '\n')

for f in friend_foods:
    print('my friend also likes ', f, '\n')