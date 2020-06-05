# This code simulates a sandwidch order completion system
# A while loop and a dictionary will be used to determine when an samdwich order is completed 
# and added to a list.
print()
print("Welcome to Doug's Cafe!")
print()
# Start with a list of sandwich types and and empty list for completed sandwhiches to be moved to.
# Pastrami has been added three times to the sandwich list but will be removed from the list becauase
# the store has run out of it.
sandwich_orders = ['pastrami', 'tuna', 'turkey', 'pastrami', 'ham', 'bologna', 'pastrami', 'chicken']
finished_sandwiches = []
# Identify each order until there are none left.
# Move each other from the order list to the finished sandwich list
# The first finsihed sandwich in the list should be Chicken
print("Here is the sandwich order list:")
print(sandwich_orders)
print()
print("Sorry, the deli has run out of pastrami.")
print()
print("...making sandwiches...")
print()
#The following code block removes pastrami from the order list and then passes through a second wnile loop to print
#the remaining sandwiches made
while 'pastrami' in sandwich_orders:
    sandwich_orders.remove('pastrami')
while sandwich_orders:
    sandwich_name = sandwich_orders.pop()
    print("Your " + sandwich_name.title() + " sandwich is ready!")
    finished_sandwiches.append(sandwich_name)
# Display all finished sandwiches
print()
print("*** Thanks for visiting Doug's Deli! ***")
print()