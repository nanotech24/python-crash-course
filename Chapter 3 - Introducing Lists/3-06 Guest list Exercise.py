guest_list = ["sarah", "mother", "gran"]
print("Hello " + guest_list[0].title() + "! You are invited to dinner!")
print("Also you, " + guest_list[1].title() + "!")
print("And I can't forget about you too, " + guest_list[2].title() + "!")
print(guest_list[2].title() + " cannot make it! oh no :(")
guest_list[2] = "maggie"
print(guest_list[2].title() + " is now comming to dinner!")
guest_list.insert(0, "tony")
guest_list.insert(1, "daniel")
guest_list.append("anne")
print("We now have room for more!\n" + guest_list[0].title() + ", you are now invited!")
print(guest_list[1].title() + " is going to come now too.")
print("And last but not least, " +guest_list[5].title() + "!")