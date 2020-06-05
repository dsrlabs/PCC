print()
ten_mult = input("Hello, enter a number and I'll tell you whether it's a multiple of 10 or not. ")
# The following line of code sets the input number to an integer numerical input is accepted
ten_mult = int(ten_mult)
# The following LOC uses the modulo operator to divide one number by another and return the remainder. If no remainder is returned, the number is divisible 
# by another, yielding an even number. If a remainder is returned, the number is not divisible by itself, yielding an odd number.
# The if-else chain returns the results.
if ten_mult % 10 == 0:
    print("\nThe number " + str(ten_mult)  + " is a multiple of 10.")
else:
    print("\nThe number " + str(ten_mult)  + " is not a multiple of 10.")
