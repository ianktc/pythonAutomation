# Program to fill in gaps in a series of files given a prefix

import os, re

# prompts user for inputs
def prompt(userInput):

    # prompting for the directory to search
    if userInput == 1:
        print("Input a directory to search: ")
        response = input()

    # prompting for the size of file to delete
    else:
        print("Input the prefix to search for: ")
        response = input()

    return response

# finds the files with the same prefix
def findPrefix(dirName, prefixName):

    # listdir method extracts both files and directories
    contents = os.listdir(dirName)

    # creating regex to find prefix
    prefixRegex = re.compile(prefixName)

    # creating a list to hold the files with the prefix
    filesPrefix = []

    # checking each file if it has the prefix
    for file in contents:

        # create path for each file
        path = (dirName + "\\" + file)

        # finds whether it is file or dir (ignore if dir)
        if os.path.isfile(path):

            # check if it has prefix
            if prefixRegex.search(file):
                filesPrefix.append(file)

    print("Files with prefix are: " + str(filesPrefix))
    return filesPrefix

# finds the number of files with the prefix
def findNumber(filesPrefix, prefixName):

    """ approach: parse through each element in filesPrefix, then find the one out of order
    then rename the remaining ones starting from the end that was last in order!
    """

    # creating a regex to find the suffixes (numbers)
    numberRegex = re.compile(r'[0-9]+')

    # creating list to store the number of files with prefix
    number = []

    for file in filesPrefix:
        mo = numberRegex.search(file)

        # int casting the list so it can be sorted
        number.append(int(mo.group()))

    print("File numbers are: " + str(number))
    return number

# finds the last in-order file
def findIndex(number):

    for i in range(len(number)):
        # print(number[i])
        if number[i] != i + 1:
            number[i] = i + 1
            inOrder = i

    print(number)

    # where inOrder is the last index that is in order
    print("Last in order is " + str(inOrder))
    return inOrder

def removeGaps(index, number):
    '''use string indexing to order the remaining stuff appropriately'''

    # starting index
    start = index
    # print("hi")
    for i in range(start, len(number)):
        # print(i)
        number[i] = i + 1
    # print(number)



    
if __name__ == "__main__":

    dirName = prompt(1)
    prefixName = prompt(2)

    # filesPrefix holds all the files with the provided prefix
    filesPrefix = findPrefix(dirName, prefixName)

    # finds number of files with prefix
    number = findNumber(filesPrefix, prefixName)

    # finds the last in-order file number
    index = findIndex(number)    

    removeGaps(index, number)
    