# Program Brief

# program to print a list of strings in a formatted table

strings = []

# accepts strings from user
def userInput(strings):

    loop = True
    while(loop):
        print("Input a string: (press space to quit) ")
        entry = input()
        if (entry == ' '):
            break
        strings.append(entry)

# finds longest string in list
def findMaxLength(strings):
    maxLength = 0
    for string in strings:
        length = len(string)
        if (length > maxLength):
            maxLength = length
    print ("Max length is " + str(maxLength))
    return maxLength

# prints the formatted table
def printTable(strings, maxLength, alignment):
    print("\n")

    for string in strings:
        if (alignment.lower() == "left"):
            print(string.ljust(maxLength, ' ') + " ", end = '')
        elif (alignment.lower() == "right"):
            print(string.rjust(maxLength, ' ') + " ", end = '')
        elif (alignment.lower() == "middle"):
            print(string.center(maxLength, ' ') + " ", end = '')
        if ((strings.index(string) + 1) % 3 == 0):
            print("\n" , end = '')
                
    print("\n")

userInput(strings)
maxLength = findMaxLength(strings)

# prints out strings unformatted, and the maximum length
print("Strings are: %s where the maximum length is %d \n" % (strings, maxLength))

# prompts user for type of format
loop = True
while(loop): 
    print("Enter the alignment: (left, middle, right) " , end = '')
    alignment = input()
    printTable(strings, maxLength, alignment)
    if (alignment == ' '):
        break