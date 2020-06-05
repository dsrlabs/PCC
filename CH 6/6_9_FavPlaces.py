print()
# The following block of code shows a nested dictionary containing data on three people and their favorite place to visit.
# To show that a person has more than one favorite place, model the code after favorite_languages.py on page 112
favorite_places = {
    'jan': 'the virgin islands',
    'angie': 'london'  ,
    'david': 'jamaica' ,
    }
# The following block of code iterates through data on each persoo's favorite place to visit, then prints that data on a new line for each person.
for name, place in favorite_places.items():
    print(name.title() + "'s favorite place to visit is " + place.title() + ".")
    print()