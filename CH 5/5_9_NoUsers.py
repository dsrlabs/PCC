#First, add an if-test to make sure the list is not empty
print()
print("(...checking the list for users logged in...)")
usernames = ['Doug', 'Stine', 'Danielle', 'Michael']
if usernames:
    for username in usernames:
        print("Hello " + username)
else:
    print("We need to find some users!")
#Now, empty the list and make sure the if-test prints ight message 
print()
print("(... now checking to see if the user list is empty...)")
print()
usernames = []
if usernames:
    for username in usernames:
        print("Hello " + username)
else:
    print("Yes, we need to find some users! Please check back later.")
print()