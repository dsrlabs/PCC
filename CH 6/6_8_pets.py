print()
# The following block of code shows a nested dictionary containing data on three pet owners and their pet's information.
pets= {
    'rover': {
        'ownername': 'doug',
        'pettype': 'dog',
        'color': 'black',
           },
    'jessica': {
        'ownername': 'danielle',
        'pettype': 'rabbit',
        'color': 'black',
        },
    'felix': {
        'ownername': 'stine',
        'pettype': 'cat',
        'color': 'tan',    
        }, 
    }
# The following block of code iterates through data on each owner and pet's info, then prints that data on a new line for each person.
for name, pets_info in pets.items():
    print("\nPet's name: " + name.title())
    Owner = pets_info['ownername']
    Pet  = pets_info['pettype']
    Color = pets_info['color']
    
    print("\tOwner: " + Owner.title())
    print("\tPet Type: " + Pet.title())
    print("\tPet Color: " + Color.title())
    print()