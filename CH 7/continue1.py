age = True
while age > 0:
    age = input("How old you? [Type 'q' to quit]")
    age = int(age)
    if age < 3:
        print("  You get in free!")
    elif age < 13:
        print("  Your ticket is $10.")
    else:
        print("  Your ticket is $15.")