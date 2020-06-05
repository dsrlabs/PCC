#This code demonstrates how to list items in tuples

print("Here is a list of foods this restaurant serves:")
restaurant_foods = ('Chicken', 'Seafood', 'Pasta', 'Beef', 'Lamb')
for restaurant_food in restaurant_foods:

    print(restaurant_food)

# Now one food type will be changed to show that Python will not allow assigning a new value to an item in a tuple
restaurant_foods = ('Chicken', 'Seafood', 'Pasta', 'Beef', 'Lamb')
restaurant_foods[0] = ('Deer')
print("Here is a list of foods this restaurant serves:")
for restaurant_food in restaurant_foods:
    print(restaurant_food)
