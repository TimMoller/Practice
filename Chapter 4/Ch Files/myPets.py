myPets = ["Zozo", "Jojo", "Nunu"]
print("Enter a pet name")
name = input()
if name not in myPets:
    print("I dont have a pet by that name.")
else:
    print(name + " is my pet.")
