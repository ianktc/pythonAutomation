# Program to search for files with a given extension, and then copy them into a new folder

import os, shutil

def prompt(userInput):

    # if userInput = 1, prompting for folder name
    if userInput == 1:
        print("Enter a folder to search within. Provide the entire path: ", end = '')
        response = input()

    # if userInput = 2, prompting for file extension type
    if userInput == 2:
        print("Enter an extension type to search for: ", end = '')
        response = input()

    # if userInput = 3, prompting for new folder name
    if userInput == 3:
        print("Enter a name for the new folder. Note that the new folder will be located within the directory the user provided. ", end = '')
        response = input()

    return response

def selectiveCopy(folderName, extensionType, newFolderName):
    # making a list containing contents of the directory
    contents = os.listdir(folderName)

    # making a new directory with os module
    os.makedirs(folderName + "\\" + newFolderName)
    
    # populating the new folder which contains files with specified extension 
    for file in contents:
        # copy method accepts two parameters (source and destination)
        if file.endswith(extensionType):
            shutil.copy(folderName + "\\" + file, folderName + "\\" + newFolderName)

    finalPath = (folderName + "\\" + newFolderName) 
    
    return finalPath
    

if __name__ == "__main__":
   
    # ask for folder to search within
    folderName = prompt(1)

    # ask for file extension type
    extensionType = prompt(2)

    # ask for new folder name
    newFolderName = prompt(3)

    # run program
    finalPath = selectiveCopy(folderName, extensionType, newFolderName)

    print("You will find the directory containing the copied files under the path: \n%s" % finalPath)