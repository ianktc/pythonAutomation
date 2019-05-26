# Program to ensure a given password is strong enough

''' Password Requirements: 
- at least eight characters long
- has both upper and lower case characters
- has at least one digit
'''

# it is assumed that the password that is passed to this program is a one word string

import re

def password():
    print("Input a password: " , end = '')
    password = input()
    return password

def strength(userInput):

    strong = False

    # password regex which accepts characters (below)
    passwordRegexLower = re.compile(r'[a-z]+')
    passwordRegexUpper = re.compile(r'[A-Z]+')
    passwordRegexDigits = re.compile(r'[0-9]+')
    
    # checking if the password meets requirements
    if (passwordRegexLower.findall(userInput) and passwordRegexUpper.findall(userInput) and passwordRegexDigits.findall(userInput)):
        strong = True

    # testing if the password is 8 characters 
    if (len(userInput) < 9):
        strong = False

    return strong    

# main loop to ask for password
loop = False

while(not loop):

    userInput = password()
    goodPassword = strength(userInput)

    if (goodPassword):
        print("Password is strong. ")
        break
    else:
        print("Password is not strong enough. Please re-enter a password.")
