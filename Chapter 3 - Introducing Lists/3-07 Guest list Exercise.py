#here the list is created of the guests
guest_list = ["sarah", "mother", "gran"]

#here each guest is given an invitation to the dinner
print("Hello " + guest_list[0].title() + "! You are invited to dinner!")
print("Also you, " + guest_list[1].title() + "!")
print("And I can't forget about you too, " + guest_list[2].title() + "!")

#someone cannot make it, so we overwrite the list index[2] with a new name string
print(guest_list[2].title() + " cannot make it! oh no :(")
guest_list[2] = "maggie"
print(guest_list[2].title() + " is now comming to dinner!")

guest_list.insert(0, "tony")
guest_list.insert(1, "daniel")
guest_list.append("anne")
print("We now have room for more!\n" + guest_list[0].title() +
      ", you are now invited!")
print(guest_list[1].title() + " is going to come now too.")
print("And last but not least, " + guest_list[5].title() + "!")

print("Sadly, it turns out only two people can be invited.")
#Here the guests are removed and added to removed_guests. don't forget that once something is popped from the list its removed from the list!
removed_guests = [
    guest_list.pop(0),
    guest_list.pop(0),
    guest_list.pop(1),
    guest_list.pop(2)
    ]
#handy thing I learned online (', '.join(guest_list)) prints list items without the qutoes and boxes. Notice how title works here when used with join.
print(', '.join(guest_list).title() + ", You are both still invited!")

print(guest_list)