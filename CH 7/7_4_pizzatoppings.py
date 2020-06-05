print()
print("Welcome To Doug's Pizzeria - Online Ordering!")
print()
print("*** Pizza Menu ***")

prompt = "\nPlease enter your pizza topping:"
prompt += "\n(Enter 'done' when you are finished.) "
age = integer(age)

    if topping == 'done':
        break
    else:
        print("Adding " + topping + ".")
print()
print('-'*77)
print("Finished making your pizza - your wait time until delivery is 30 minutes!")
print("Thanks for placing your order online with Doug's Pizzeria!")
print()
import datetime
import time
now_date = datetime.date.today()
now_now = time.strftime("%H:%M %p")
print(f"Date: {now_date}\nTime: {now_now}")
print('-'*77)
print()
