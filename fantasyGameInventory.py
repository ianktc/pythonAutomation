# Program Brief:

# program that prompts user for input regarding several possible inventory items (quantity)
# the program then prompts for other inventory items
# the program then prints the entire update inventory

# additional: add items to inventory from a LIST data type



# this initializes the dictionary inventory with each key set to 'none'
inventory = dict.fromkeys(['arrows', 'daggers', 'goldCoins','torches', 'ropes'])

# takes in input from user for each inventory item
def userInput(inventory):
    print("Number of arrows: " , end = '')
    inventory['arrows'] = input()
    print("Number of daggers: " , end = '')
    inventory['daggers'] = input()
    print("Number of gold coins: " , end = '')
    inventory['goldCoins'] = input()
    print("Number of torches: " , end = '')
    inventory['torches']= input()
    print("Number of ropes: " , end = '')
    inventory['ropes'] = input()

    return inventory

#  prompts user for additional items that were not listed
def additionalItems(inventory):
    
    loop = True
    # use while loop to continue to prompt user for input until they are done
    while(loop):
        print("Input a new item: (Enter space to exit) " , end = '')
        item = input()
        if (item == ' '):
            break
        print("Input amount: " , end = ' ')
        amount = input()
        inventory[item] = amount

    return inventory

# prints the inventory
def printInventory(inventory):
    print("INVENTORY: ")
    count = 0

    # for loop to print out the inventory
    for i, j in inventory.items():
        print(i + ": " + j)
        count = count + int(inventory.get(i,j))

    print("Total number of items: %d" % count)

# accepts additional input in form of list
def additionalList(inventory):
    newList = []

    loop = True
    # use while loop to continue to prompt user for input until they are done
    while(loop):
        print("Input items: (space to exit) " , end = '')
        item = input()
        if (item == ' '):
            break
        newList.append(item)

    print (newList[:])
    return inventory
    
userInput(inventory)
additionalItems(inventory)
printInventory(inventory)
additionalList(inventory)