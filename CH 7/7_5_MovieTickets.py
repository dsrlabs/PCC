prompt = "How old are you?"
prompt += "\nEnter 'quit' when you are finished. "
# The following line of code accepts the age of the moviegoer as an integer
print() 
# The following lines of code compares uses an if-elif-else chain to determine the ticket cose per age range
while True:
    age = input(prompt)
    if age == 'quit':
        break
    age = int(age)

    if age < 3:
        print ("The ticket is free")
    elif age < 13:
        print ("The ticket cost = $10.")
    elif age > 13:
        print ("The ticket cost = $15.")
#The following lines of code are purely cosmetic
print()
print('-'*77)
print("Thanks for choosing Ramsay Theater - Enjoy the movie!")
print()
import datetime
import time
now_date = datetime.date.today()
now_now = time.strftime("%H:%M %p")
print(f"Date: {now_date}\nTime: {now_now}")
print('-'*77)
print()