guest_list = ["sarah", "mother", "gran"]
print("Hello " + guest_list[0].title() + "! You are invited to dinner!")
print("Also you, " + guest_list[1].title() + "!")
print("And I can't forget about you too, " + guest_list[2].title() + "!")
print(guest_list[2].title() + " cannot make it! oh no :(")
guest_list[2] = "maggie"
print(guest_list[2].title() + " is now comming to dinner!")