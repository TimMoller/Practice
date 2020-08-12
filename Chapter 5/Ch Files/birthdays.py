birthdays = {'Alice': 'Apr 1', 'Bob': 'Dec 12', 'Carol': 'Mar 4'}

while True:
    print('Enter a name: (blank to quit)')
    name = input()
    if name == '':      # if input is left blank
        break           # Stop the program
    if name in birthdays:
        print(birthdays[name] + ' is the birthday of ' + name)
        # Search for the name in the dictionary
        # Name is "key", program returns the corresponding value
    else:
        print('I do not have birthday information for ' + name)
        print('What is their birthday?')
        bday = input()
        birthdays[name] = bday
        print('Birthday database updated.')
