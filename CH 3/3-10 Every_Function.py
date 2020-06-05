print()
guitars = ['stratocaster', 'telecaster', 'sheraton', 'cloud', 'symbol']
message1 = "Access the first guitar in the list."
print(message1)
print(guitars[0])
print()
message2 = "Repeat the first guitar in the list, as a title name."
print(message2)
print(guitars[0].title())
print()
message3 = "Access the last guitar in the list."
print(message3)
print(guitars[-1])
print()
message4 = "My favorite guitar in the list is the" + " " + guitars[0].title() + "."
print(message4)
print()
message5 = "Modify an element in the list by printing the original list then showing the modification."
print(message5)
print(guitars)
guitars[0] = 'explorer'
print(guitars)
print()
message6 = "Add an element in the list."
print(message6)
guitars.append('destroyer')
print(guitars)
message7 = "Insert an element at a specific place in the list."
print(message7)
guitars.insert(1, 'broadway')
print(guitars)
message8 = "Remove 'sheraton' from the list (print the list then show the new list)."
print(message8)
print(guitars)
del guitars[3]
print(guitars)
print()
message8 = "Pop a guitar from the list (this should be the last item)."
print(message8)
print(popped_guitars)
popped_guitars = guitars.pop()
print(guitars)
print(popped_guitars)