#C3-10 make a project that does one thing from each thing learned so far p.50
#(list,print,print ea,append,insert,replace,pop,remove value,sorting,len)

print('this is a list project trying to implement everything learned up to page 50 in the book\n\n'.title())

#I will start with towns
towns = ['dildo', 'conception bay south', 'torbay']

#print the list of towns using join to get rid of the square brackets, title to capitalize each town name
print(', '.join(towns).title() + '\n')

#printing towns with index
print(towns[1].title() + '\n')

#appending a town to the end of the list
towns.append('st. philips')

#using a for loop to append multiple towns in another list
appendlist = ['mount pearl', 'carbonear', 'marystown']
i = 0
for t in appendlist:
  towns.append(appendlist[i])
  i += 1

#inserting a new value into the first position
towns.insert(0, 'clarenville')

#using for loop to print towns by line then sorted, use += to increment var
#note that variable i can be reused in this case as it is after the first loop
i = 0
n = 1
for t in towns:
  print(str(n) + '. ' + sorted(towns)[i].title())
  i += 1
  n += 1
print('\n')

#replacing an item in the list, note that it is after the sort so it won't be sorted
towns[-1] = 'gander'
print('Here is the unsorted towns list with gander replacing the last spot:')
print(', '.join(towns).title() + '\n')

#now printing that list in reverse, but with sorted to preserve original list
print('Here is that list again, but sorted in reverse order:')
print(', '.join(sorted(towns, reverse = True)).title() + '\n')

 
#printing the length of the list
lLength = len(towns)
print('There are ' + str(lLength) + ' towns in the list\n')

#now popping the last and first items off of the list and adding them to another list

popped_towns = [
  towns.pop(0),
  towns.pop()
  ]
print('This is the first and last items of the list popped:\n' + ', '.join(popped_towns).title() + '.\n')

#now reprinting the original list
print('Here is our first list now with the first and last values removed:\n' + ', '.join(towns).title() + '\n')

#now going to remove some list items by index, then by value
#first the index with del statement
del towns[0]
print('Here are the towns with the first list item(dildo) deleted by index:\n' + ', '.join(towns).title() +'\n')

#now removing by value
towns.remove('torbay')
print('Here is the towns list again, but now with torbay deleted by value:\n' + ', '.join(towns).title())

#finally, printing the towns list in reverse permantly with .reverse
towns.reverse()
print('\nHere is the towns list permanently reversed with .reverse:\n' + ', '.join(towns).title())

#return list to normal by reversing it again
towns.reverse()
print('\nHere is the list reverted to original by reversing it again right away:\n' + ', '.join(towns).title())