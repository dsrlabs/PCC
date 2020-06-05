print()
current_users = ['doug', 'stine', 'danielle', 'Michael', 'rebecca']
new_users = ['ree', 'Stine', 'JOY', 'michael', 'Jackie']
current_users_lower = [user.lower() for user in current_users]
for new_user in new_users:
    if new_user.lower()in current_users_lower:
        print("Sorry, the username " + new_user + ", has already been used. Please enter a new username.")
    else:
        print("Thank you, the username " + new_user + " is available for use.")
