p1 = "Make a lot of money"
p2 = "buy now"
p3 = "subscribe this"
p4 = "click this"

messages = input("Enter a message: ")

if(p1 in messages or p2 in messages or p3 in messages or p4 in messages):
    print("This is a spam message.")

else:
    print("This is not a spam message")