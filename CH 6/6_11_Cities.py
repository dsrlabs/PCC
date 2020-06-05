print()
# The following block of code shows a nested dictionary containing data on three pet owners and their pet's information.
cities = {
    'new york city': {
        'country': 'USA',
        'population': '8M',
        'fact': 'It is the only city in the US with five boroughs.',
           },
    'east orange': {
        'country': 'USA',
        'population': '75K',
        'fact': 'A section of the city is called Presidential Square.',
        },
    'Lacoste': {
        'country': 'France',
        'population': '40K',
        'fact': 'Tt is south of France.',    
        }, 
    }
# The following block of code iterates through data on each city and it's assocated data, then prints each  on a new line for each person.
for city, citydata in cities.items():
    print("\nCity Name: " + city.title())
    Country = citydata['country']
    Population  = citydata['population']
    Fact = citydata['fact']
    
    print("\tCountry: " + Country)
    print("\tPopulation: " + Population)
    print("\tFact: " + Fact)
    print()