# Design a program that will ask for a name and age
# It will then tell me the length of my name and how old I will be next year

print("Hello There!")
myName = input("What is your name? \n") #ask for a name input
print("The length of your name is:")
print(str(len(myName)) + " characters long.")  #state the length of the name provided
age = input("How old are you?: \n") #ask for an age input
print("So next year your will be " + str(int(age) + 1)) #state how old the person will be next year
