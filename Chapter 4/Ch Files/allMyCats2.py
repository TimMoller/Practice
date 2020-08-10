catNames = []

while True:
    print('Enter the name of cat ' + str(len(catNames) + 1) + ' or enter nothing to stop.')
    name = input()
    if name == '':
        break
    catNames = catNames + [name]    # list concatenation, the brackets around the variable 'name' change it to a list indexed item
print("the cats' names are:")
for name in catNames:
    print(' ' + name)
