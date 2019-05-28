# Program that prompts user to input words for a madlib

# TODO: 
# Read the madlibsTest.txt file
# Use regex to find the adjectives, nouns, verbs etc
# Prompt user for input for each type
# Replace the types with the words provided by user

import re, shelve, pyperclip, sys

# prompts user for a word, depending on the word type
def prompt(wordType):
    # ensure proper usage of a versus an (catches adverbs and adjectives)
    if (wordType[0].lower() == 'a'):
        print("Enter an %s: " % wordType, end = '')
        word = input()
    else:
        print("Enter a %s: " % wordType, end = '')
        word = input()
    return word

# parses through the text file - the parameter is the text file string!
def parse():
    # regex for each word type
    adjectiveRegex = re.compile(r'ADJECTIVE')
    nounRegex = re.compile(r'NOUN')
    verbRegex = re.compile(r'VERB')

    # open and read the file
    madlibFile = open('C:\\Users\\iankt\\OneDrive\\Documents\\GitHub\\pythonAutomation\\madlibs\\madlibsTest.txt')
    madlibFileContent = madlibFile.read()

    finalMadlib = madlibFileContent
    finished = False

    # use regex to find and replace
    # use while loop to ensure that the regex only searches for one occurence at a time
    while (finished == False):
        if adjectiveRegex.search(finalMadlib):
            finalMadlib = adjectiveRegex.sub(prompt('ADJECTIVE'), finalMadlib, count = 1)
        if nounRegex.search(finalMadlib):          
            finalMadlib = nounRegex.sub(prompt('NOUN'), finalMadlib, count = 1)
        if verbRegex.search(finalMadlib):       
            finalMadlib = verbRegex.sub(prompt('VERB'), finalMadlib, count = 1)

        if ((nounRegex.search(finalMadlib) == None) and \
            (adjectiveRegex.search(finalMadlib) == None) and \
            (verbRegex.search(finalMadlib) == None)):
            finished = True        
    
    return(finalMadlib)


finalMadlib = parse()
print(finalMadlib)

