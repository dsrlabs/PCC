# The following code block passes an argument to a parameter of a function
print()
def favorite_book(title):
    """Display announcement"""
    print("My favorite book is " + title.title() + ".")
    
favorite_book('snow crash') 
print()

# The following code block does the same as the previous but uses an f-string
print()
def favorite_book(title):
    """Display announcement"""
    print(f"{title.title()} is my favorite book.")
    
favorite_book('snow crash') 
print()