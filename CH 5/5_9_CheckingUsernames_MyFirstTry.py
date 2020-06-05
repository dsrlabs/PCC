print()
current_users = ['doug', 'stine', 'danielle', 'michael', 'Rebecca']
new_users = ['Ree', 'annette', 'Tina', 'jackie', 'Stine']
current_users_lower = [user.lower() for user in current_users]
for new_user in new_users:
    if new_user in current_users:
        print("Sorry, the username " + new_user + " has already been used, please enter a new username.")
    else:
        print("Thank you, that username is available for use")
