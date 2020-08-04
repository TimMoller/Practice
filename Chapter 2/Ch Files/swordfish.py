while True:
    print("Who are you?")
    name = input()
    if name != "Joe":
        continue
    print("Hello, Joe. Enter your Password please: (Hint: it's a fish)")
    password = input()
    if password == "swordfish":
        break

print("Access Granted, welcome " + name)
