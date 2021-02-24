#C4-10 using a program from earlier, add lines that print 3 slices from beginning, middle and end

million = list(range(1,1000001))

#for n in million:
#  print(n)

#here I will slice from the list. I commented out the for this part

print('\nThe first 3 numbers in the list are: ' + str(million[:3]))

print('\nHere are some of the numbers from the middle of the list: ' + str(million[500000:500003]))

print('\nAnd here are the last 3 entries in the list: ' +str(million[-3:]))