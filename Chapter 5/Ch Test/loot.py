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
    print('You have ' + str(itemNumber) + ' types of items.')
    print('You have ' + str(itemTotal) + ' total items.')

def addToInventory(inventory, addItems):
    for i in addItems:
        inventory.setdefault(i, 0)
        if i in inventory:
            inventory[i] += 1

inv = {'gold coin':42, 'rope':1}

dragonLoot = ['gold coin', 'dagger', 'gold coin', 'gold coin', 'ruby']

print("You have defeted the dragon.")
print('the dragon has: ' + str(dragonLoot))

displayInventory(inv)
print('You loot the dragon.')

addToInventory(inv, dragonLoot)
displayInventory(inv)
