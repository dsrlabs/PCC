# First using no for loop
print()
odd_numbers = list(range(3, 21, 2))
print(odd_numbers)
print()
# Now using a for loop to do the same.
odd_numbers = []
for value in range(1, 19, 2):
    odd_number = value + 2
    odd_numbers.append(odd_number)
print(odd_numbers)
print()
