stuff = {'rope': 1, 'torch': 6, 'gold coin': 42, 'dagger': 1, 'arrow': 12}

def displayInventory(inv):
    print('Inventory:')
    itemNumber = 0
    itemTotal = 0
    for k, v in inv.items():
        print(k + ': ' + str(inv.get(k, 0)))
    for k in inv:
        itemNumber += 1
    for k in inv:
        itemTotal += inv.get(k, 0)
    print('There are ' + str(itemNumber) + ' types of items.')
    print('Tere are ' + str(itemTotal) + ' total items.')

displayInventory(stuff)
