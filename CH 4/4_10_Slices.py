note = "(Note: See the section on Looping Through a Slice, pg 64 on how to print the loop result)"
print
print(note)
print()
number_range = "The range of numbers are:"
print(number_range)
for value in range(1,21):
    print(value)
print()
numbers = list(range(1,21))
print(numbers)
first_three_msg = "The first three items in the list are: "
print(first_three_msg)
print(numbers[0:3])
middle_three_msg = "The three items from the middle of the list are: "
print(middle_three_msg)
print(numbers[9:12])
last_three_msg = "The three items from the end of the list are: "
print(last_three_msg)
print(numbers[17:20])
