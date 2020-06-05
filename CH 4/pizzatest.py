print()
pizzatalk = "Let's talk about pizza!"
print(pizzatalk)
print()
pizzas = ['pepperoni', 'sausage', 'cheese']
for pizza in pizzas:
    print("I like " + pizza.title() +  " pizza. ")
print("I reeeally like pizza!")
print()
adding_my_pizza = "Now adding to my list of favorite pizzas:"
print(adding_my_pizza)
pizzas.append('meatball')
print ("My favorite pizzas are now:")
for pizza in pizzas[:]:
    print( pizza.title() +  " pizza. ")
print()
listing_my_friends_pizzas = "Now listing my friend's favorite pizzas:"
friend_pizzas = pizzas[:]
friend_pizzas.append('Veggie')
print(listing_my_friends_pizzas)
print ("My friend's favorite pizzas are:")