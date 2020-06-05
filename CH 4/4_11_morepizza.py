print()
pizzatalk = "Let's talk about pizza!"
print(pizzatalk)
print()
pizzas = ['pepperoni', 'sausage', 'cheese']
for pizza in pizzas:
    print("I like " + pizza.title() + " pizza. ")
print("I reeeally like pizza!")
print()
adding_my_pizza = "Now adding to my list of favorite pizzas:"
print(adding_my_pizza)
pizzas.append('meatball')
print("My favorite pizzas are now:")

# minor edit from line 16 to 23 - i guess it's time we start using commenting
for pizza in pizzas[:]:
    print(pizza.title() + " pizza. \n")

print("Now listing my friend's favorite pizzas:")
# line 21 is how you copy a list ( the new list is called friend_pizzas)
friend_pizzas = pizzas[:]
# line 23 is you ading an item(Veggie) to the new list (friend_pizzas)
friend_pizzas.append('Veggie')
print("My friend's favorite pizzas are:")
# line 26 is printing out the new list(friend_pizzas) vertically;
for pizza in friend_pizzas:
    print(pizza)

# we can also print out the list like this on a single line
print("My friend's favorite pizzas are:")

print(friend_pizzas)