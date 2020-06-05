print()
# The following block of code shows a nested dictionary containing data on three people.
people = {
    'mramsay': {
        'firstname': 'Michael',
        'lastname': 'Ramsay',
        'age': '17',
        'city': 'Bowie',
        },
    'dramsay': {
        'firstname': 'Danielle',
        'lastname': 'Ramsay',
        'age': '23',
        'city': 'Paris',
        },
    'eramsay': {
        'firstname': 'Ernestine',
        'lastname': 'Ramsay',
        'age': '56',
        'city': 'Bowie',
        }, 
    }
# The following block of code iterates through data on each person, then prints that data on a new line for each person.
for name, people_info in people.items():
    print("\nUsername: " + name)
    full_name = people_info['firstname'] + " " + people_info['lastname']
    age = people_info['age']
    city = people_info['city']
    print("\tFull Name: " + full_name.title())
    print("\tAge: " + age.title())
    print("\tCity: " + city.title())
print()