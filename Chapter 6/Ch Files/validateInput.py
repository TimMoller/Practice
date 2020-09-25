while True:
    print("Enter your age: ")
    age = input()
    if age.isdecimal():         #testing for the input to be a number,
        break                   #if it is a number move on to the next set of code
    print("Please enter a number for your age")

while True:
    print("Select a new password (Letters and numbers only): ")
    password = input()
    if password.isalnum():      #test if the password is alphanumeric
        break                   #if it is alphanumeric, move on to the next set of code
    print("Password can only have numbers and letters.")
