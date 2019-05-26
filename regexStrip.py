# Program that uses regex to recreate strip() method
# Note: strip() removes characters from beginning and end of parameter

import re
import pprint

# prompts user to input a string
def userInput():
    print("Input a string: " , end = '')
    string = input()    
    return string

# prompts user to choose a string to strip
def stripped():
    print("Input a string to strip out: (*space* to strip white space) " , end = '')
    strip = input()
    return strip

def regexStrip(string, strippedString):
    
    # first, strip the white space using the sub method 

    # NOTE: THE CARET AND DOLLAR SIGN CHARS DO NOT OPERATE AS YOU THINK
    # You have to use them one at a time
    
    # searching the beginning, and then end for white space
    regexWhiteSpaceStart = re.compile(r'^\s+')
    regexWhiteSpaceEnd = re.compile(r'\s+$')

    intermediary = regexWhiteSpaceStart.sub('', string)
    noWhiteSpace = regexWhiteSpaceEnd.sub('' , intermediary)
    print("No white space: " + noWhiteSpace)

    # searching the beginning, and then the end for the stripped string
    # do all permutations of the stripped string OR find the letters in the stripped string
    # the latter method was chosen

    # for loop to iterate through each character in the string to strip
        
    for character in noWhiteSpace:

        if character in strippedString:

            # this creates a new regex for each character of the string

            # searches beginning, then end
            regexStart = re.compile('^%s' % character)
            regexEnd = re.compile('%s$' % character)

            # this continually strips the latest string to account for each letter
            noWhiteSpace = regexStart.sub('', noWhiteSpace)
            noWhiteSpace = regexEnd.sub('' , noWhiteSpace)
            print(noWhiteSpace)

    # for some reason, there has to be a reverse for loop to catch the tail end of the string

    for character in reversed(noWhiteSpace):

        if character in strippedString:

            # this creates a new regex for each character of the string

            # searches beginning, then end
            regexStart = re.compile('^%s' % character)
            regexEnd = re.compile('%s$' % character)

            # this continually strips the latest string to account for each letter
            noWhiteSpace = regexStart.sub('', noWhiteSpace)
            noWhiteSpace = regexEnd.sub('' , noWhiteSpace)
            # print(noWhiteSpace)

    return noWhiteSpace

    # error, this does not stop stripping from the end, it parses the entire thing (wrong) -- solved

startString = userInput()
removedString = stripped()
finalString = regexStrip(startString, removedString)
print(finalString)