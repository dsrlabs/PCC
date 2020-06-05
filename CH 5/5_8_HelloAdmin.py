print()
usernames = ['Doug', 'Jan', 'Angie', 'David', 'Admin']
for username in usernames:
  if username == 'Admin':
    print('Hello Admin, would you like to see a login status report?')
  else:
    print("Hello " + username + ", " +  "thank you for logging in again!")