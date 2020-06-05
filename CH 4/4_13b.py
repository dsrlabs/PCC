#This program shows how to iddentify items in tuples
restaurant_foods = ('Chicken', 'Seafood', 'Pasta', 'Beef', 'Lamb')
print()
print("Here is a list of foods this restaurant serves:")
for restaurant_food in restaurant_foods:
    print(restaurant_food)

# Now two food types will be replaced to show that a tuple can be overwritten​
restaurant_foods = ('Rabbit', 'Seafood', 'Buffalo', 'Beef', 'Lamb')
print()
print("Two foods have been substituted. Here is the new list of foods this restaurant serves:")
for restaurant_food in restaurant_foods:
    print(restaurant_food)