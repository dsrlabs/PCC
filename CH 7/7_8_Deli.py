# This code simulates a sandwidch order completion system
# A while loop and a dictionary will be used to determine when an samdwich order is completed 
# and added to a list.
print()
print("Welcome to Doug's Deli!")
print()
# Start with a list of sandwich types and and empty list for completed sandwhiches to be moved to.
sandwich_orders = ['tuna', 'turkey', 'ham', 'bologna', 'chicken']
finished_sandwiches = []
# Identify each order until there are none left.
# Move each other from the order list to the finished sandwich list
# The first finished sandwich in the list should be Chicken
while sandwich_orders:
    sandwich_name = sandwich_orders.pop()
    print("Your " + sandwich_name.title() + " sandwich is ready!")
    finished_sandwiches.append(sandwich_name)
# Display all finished sandwiches
print("\nThe following sandwiches have been made: ")
print()
for finished_sandwich in finished_sandwiches:
    print(finished_sandwich.title())
    print()
print("*** Thanks for visiting Doug's Deli! ***")
print()
