print()
# The following block of code shows each person has more than one favorite number
numbers = {
    'michael': ['7', '4'],
    'jonathan': ['6', '2'],
    'kerrington': ['1', '10'],
    'danielle': ['5', '100'],
    'nia': ['7', '12'],
}

for name, numbers in numbers.items():
    print("\n" + name.title() + "'s favorite numbers are:")
    for number in numbers:
        print("\t" + number)
print()