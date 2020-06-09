# Thus block of code calls a function using a default
# an f-string is used.
print()
def city_country(name, country = 'France'):
    """Display announcement"""
    print(f"{name.title()}, {country.title()}")
    
city_country(name = 'paris')
city_country(name = 'marseille')
city_country(name = 'bordeaux')
print()
