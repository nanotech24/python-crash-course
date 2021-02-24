#4-11 start with list from program 4-01, copy the list to friend_pizzas
#Add a new za to list, different za to friend_pizzas
#Print each list with a message, using for loops

my_pizzas = ['meat lovers', 'pepperoni', '3 cheese', 'italian', 'square', 'deluxe']

#copying the list
friend_pizzas = my_pizzas[:]

#adding a different za to each list with append and insert

my_pizzas.append('hawaiian')

friend_pizzas.insert(0, 'mushroom')

#storing my different messages in a list
my_messages = [
  ' is probably my favorite pizza!\n',
  ' is fairly plain, but it is ok!\n',
  ' is great, I love cheese!\n',
  ' is an excellent option, the sausage is great!\n',
  ' is simply the best, that is all there is to say\n',
  ' is great for when you want a little variety\n',
  ' is alright, I will eat if I am offered, but I would not order one\n'
  ]

#creating variable m for incrementing the index for the message selection
m = 0

#for loop to print my pizza and my message
for p in my_pizzas:
  print(p.title() + my_messages[m])
  m += 1

#now to store my friends messages in a list
friend_messages = [
  'My friend loves ',
  'He also enjoys the occasional ',
  'I do not think he enjoys ',
  'My friend has told me before that they really enjoy ',
  'He really likes ',
  'Not one for a ',
  'The best pizza for him is a '
  ]

#variable now for friend message index
fm = 0

#and now the friend loop
for p in friend_pizzas:
  print(friend_messages[fm] + p.title() + '!\n')
  fm += 1