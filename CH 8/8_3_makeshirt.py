# Thus block of code calls a function using positional arguments and instead of concatentation,
# an f-string is used.
print()
def make_shirt(shirt_size, message):
    """Display announcement"""
    print(f"I would like to order a {shirt_size} shirt that says {message.title()}.")
    
make_shirt('large', ' "hello world" ') 
print()

# Thus block of code calls a function using keyword arguments and an f-string
print()
def make_shirt(shirt_size, message):
    """Display announcement"""
    print(f"I would like to order a {shirt_size} shirt that says {message.title()}.")
    
make_shirt(shirt_size = 'large', message = ' "hello world" ') 
print()