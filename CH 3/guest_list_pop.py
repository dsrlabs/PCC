guest_list2 = ['Delta', 'Ivanhoe', 'Beryl']
message = "Hello" + " " + guest_list2[0].title() + "," + " " + "I would like to invite you to dinner" + "."
message2 = "Hello" + " " + guest_list2[1].title() + "," + " " + "I would like to invite you to dinner" + "."
message3 = "Hello" + " " + guest_list2[2].title() + "," + " " + "I would like to invite you to dinner" + "."
print(message)
print(message2)
print(message3)
print()
message3 = "Hello" + " " + guest_list2[2].title() + "," + " " + "Sorry you can't make it  to dinner" + "."
print(message3)
print()
del guest_list2[2]
guest_list2.append('Polly')
message4 = "Hello" + " " + guest_list2[0].title() + "," + " " + "I would like to invite you to dinner" + "."
message5 = "Hello" + " " + guest_list2[1].title() + "," + " " + "I would like to invite you to dinner" + "."
message6 = "Hello" + " " + guest_list2[2].title() + "," + " " + "I would like to invite you to dinner" + "."
print(message4)
print(message5)
print(message6)
print()
message7 = "To my current guests, I have found a bigger table and will be inviting others."
print(message7)
print()
guest_list2.insert(0, 'Del')
guest_list2.insert(3, 'Betty')
guest_list2.append('Jazmine')
print()
message8 = "Hello" + " " + guest_list2[0].title() + "," + " " + "I would like to invite you to dinner" + "."
message9 = "Hello" + " " + guest_list2[1].title() + "," + " " + "I would like to invite you to dinner" + "."
message10 = "Hello" + " " + guest_list2[2].title() + "," + " " + "I would like to invite you to dinner" + "."
message11 = "Hello" + " " + guest_list2[3].title() + "," + " " + "I would like to invite you to dinner" + "."
message12 = "Hello" + " " + guest_list2[4].title() + "," + " " + "I would like to invite you to dinner" + "."
message13 = "Hello" + " " + guest_list2[5].title() + "," + " " + "I would like to invite you to dinner" + "."
print(message8)
print(message9)
print(message10)
print(message11)
print(message12)
print(message13)
print()
print(guest_list2)
message14 = "Sorry, guests, it seems I can only invite two of you to dinner."
print(message14)
popfirst = guest_list2.pop(0)
print("Sorry" + " " + popfirst.title() + "," + "maybe next time" + ".")
popfirst = guest_list2.pop(0)
print("Sorry" + " " + popfirst.title() + "," + "maybe next time" + ".")
ppopfirst = guest_list2.pop(0)
print("Sorry" + " " + popfirst.title() + "," + "maybe next time" + ".")
popfirst = guest_list2.pop(0)
print("Sorry" + " " + popfirst.title() + "," + "maybe next time" + ".")
message15 = "Hello" + " " + guest_list2[0].title() + "," + " " + "thank you for staying" + "."
message16 = "Hello" + " " + guest_list2[1].title() + "," + " " + "Ithank you for staying also" + "."
print(message15)
print(message16)
del guest_list2[0]
del guest_list2[0]
print(guest_list2)