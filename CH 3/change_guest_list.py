guest_list2 = ['delta', 'ivanhoe', 'beryl']
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