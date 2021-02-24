#think of at least 3 animals with a comman charactaristic, store in list and print

animals = ['dog', 'cat', 'ferret', 'rat']

statement = [
  ' is an awesome pet, I love mine!',
  ' is a pretty good pet too!',
  ' might make a good pet, I would not know.',
  ' is fun, I have had them in the past!'
  ] 

s = 0

for a in animals: 
  print('A ' + a.title() + statement[s] + '\n')
  s +=1

print('Each of these animals each share a common trait.... They all have legs! :D')