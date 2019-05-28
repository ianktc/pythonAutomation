# A program that opens all .txt files in a folder and searches for a user provided string
# Return: The matched strings 

# TODO: 
# Prompt user for directory name and open directory
# Walk the directory searching for .txt files
# Prompt user for string to search for
# Open each file and search

# USAGE:
# The program prompts for a dir and a string to search for
# The program will copy the string to the clipboard

import re, os, pyperclip

def prompt(query):

    # detects if the user is inputting a dir name or string
    # takes two arguments (1 or 2)
    if (query == 1):
        print("Enter a directory to search within. Provide the absolute path: ", end = '')
        response = input()
    else:
        print("Enter a string to search for: ", end = '')
        response = input()
    return response

# finds all files with .txt extension in the given directory
def findFiles(directoryName):

    # this function opens lists the files within a directory
    files = os.listdir(directoryName)

    # list containing all files with .txt type
    textFiles = []

    # populates textFiles list with appropriate file names
    for file in files:
        if file.endswith(".txt"):
            textFiles.append(file)

    return textFiles

def regex(file, dirName, searchedString):
    
    # creating regex for string to be searched
    stringRegex = re.compile(searchedString)

    # creating path variable that leads to file's location by 
    # appending the file name to the provided directory
    path = (dirName + "\\" + file)
    # print(dirName)
    # print(path)

    # open and read file
    textFile = open(path)
    textFileContent = textFile.read()

    # using regex to find string
    mo = stringRegex.search(textFileContent)
    mo = mo.group()
    if mo != None: 
        pyperclip.copy(mo)
        pyperclip.paste()



# prompting for directory to walk
dirName = prompt(1)

# finds files with .txt type in a given directory 
files = findFiles(dirName)

# prompting for string to search for
searchedString = prompt(2)

# finds the string within the file. uses for loop to loop through each file
# print(files[0])
for file in files:
    regex(file, dirName, searchedString)

