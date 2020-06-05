# This program polls users about their dream vacation and asks if they could visit anywhere in the world
# where would it be.
# The results of the code are then printed

# A flag is set to indicate polling is active
polling_active = True
# An empty dictionary is created to store the responses
print("Welcome to The Dream Vacation Poll!")
responses ={}
# Prompt is set for the user name and response in the while loop
while polling_active:
    print()
    name = input("What is your name? ")
    response = input("What would be your dream vacation destination? ")
# Store the response in a dictionary
    responses[name] = response
# Invite another user to take the poll
    next_user = input("Would you like another user to take the poll? (yes/ no) ")
    if next_user == 'no':
        polling_active = False
# Print poll results
print("\n*** Poll Results ***")
for name, response in responses.items():
    print (name + " would love to take a dream vacation to " + response + ".")
print()
print("Thanks for taking the Dream Vacation Poll!")
