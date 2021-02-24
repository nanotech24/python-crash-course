#assigning a list of travel destinations
world_travel = ['italy', 'england', 'china', 'taiwan', 'cuba']

#printing the list
print(world_travel)

#using the sorted method to sort the list without changing the original

print(sorted(world_travel))

#printing the list again to show it was unchanged
print(world_travel)

#channging the original list to reverse order
world_travel.reverse()
print(world_travel)

#reversing the list again to get it back to the orignal order
world_travel.reverse()
print(world_travel)

#using sort to change the list order to alphabetic permanently
world_travel.sort()
print(world_travel)

#using sort with the reverse=true argument to reverse it permanently
world_travel.sort(reverse = True)
print(world_travel)