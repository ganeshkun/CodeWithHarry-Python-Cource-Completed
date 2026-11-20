username = input("Enter your username: ")

if(len(username)<10):
    print("Username must be at least 10 characters long.",len(username))

else:
    print("Username accepted.",len(username))
