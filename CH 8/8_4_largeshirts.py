# The following code block uses a defaut value of 'large' to print the shirt size and a message.
print()
def make_shirt(shirt_size, message='"i love python" '):
    """Display announcement"""
    print("I would like to order a " + shirt_size  + " shirt that says " + message.title() + ".")
    
make_shirt('large', message='"i love python" ') 
print()

# The following code block uses a default value of 'medium' to print the shirt size and a message.
print() 

def make_shirt(shirt_size, message='"i love python" '):
    """Display announcement"""
    print("I would like to order a " + shirt_size  + " shirt that says " + message.title() + ".")
    
make_shirt('medium', message='"i love python" ') 
print()

# The following code block uses a defaut value of 'medium' to print the shirt size and a message.
print()
def make_shirt(shirt_size, message='"i love python" '):
    """Display announcement"""
    print("I would like to order a shirt of " + shirt_size  + " that says " + message.title() + ".")
    
make_shirt('any size', message='"to be pythonic is to be iconic!" ') 
print()