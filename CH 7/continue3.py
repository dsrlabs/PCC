age = "quit"

while age != "quit":
    age = input("How old you? Enter your age to find out ticket price, type 'quit' to end. ")
    age = int(age)
    if age < 3:
        print("  You get in free!")
    elif age < 13:
        print("  Your ticket is $10.")
    else:
        print("  Your ticket is $15.")
print()
print("You're done. Thanks, enjoy the movie! ")