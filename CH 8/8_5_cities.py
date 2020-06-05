# Thus block of code calls a function using a default
# an f-string is used.
print()
def describe_city(name, country = 'United States'):
    """Display announcement"""
    print(f"{name.title()} is in the {country.title()}.")
    
describe_city(name = 'milwaukee')
describe_city(name = 'east orange')
describe_city(name = 'reykjavik')
print()
