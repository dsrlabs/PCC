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
popped_guitars = guitars.pop()
print(guitars)
print(popped_guitars)
print()
message9 = "Renove 'explorer' from the iist."
print(message9)
print(guitars)
guitars.remove('explorer')
print(guitars)
print()
message10 = "Sort the list permanmently."
print(message10)
print(guitars)
guitars.sort()
print(guitars)
print()
message11 = "Sort the list in reverse alphabetical order."
print(message11)
guitars.sort(reverse=True)
print(guitars)
print()
message12 = "Sort the list temporarily with the sorted() function."
print(message12)
print(guitars)
print("\nHere is the sorted list:")
print(sorted(guitars))
print("\nHere is the original list again:")
print(guitars)
print()
message13 = "Sort the list in reverse alphabetically using the sorted(reverse=True) function."
print(message13)
rao = sorted(guitars, reverse=True)
print(rao)

