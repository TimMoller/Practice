name = input("what is your name? ")
age = int(input("How old are you? "))
if name == "Alice":
    print("Hi, Alice")
elif age < 12:
    print("A bit young there Kiddo")
elif age > 50 and age < 70:
    print("nogo zone pops")
elif age > 70:
    print("Get off the computer gramps")
else:
    print("You're not Alice, access denied")
