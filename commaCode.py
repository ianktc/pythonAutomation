# program to convert a list into a string within quotation marks

# given list
spam = ['apples', 'bananas', 'tofu', 'cats']

# test lists
ian = ['18', 'Male', 'Blue']

for i in range(len(spam)):

    # if element is last one
    if (i == (len(spam) - 1)):
        print("and " + spam[i] + "'", end = '')

    # if element is first one
    elif (i == 0):
        print("'" + spam[i] + ", ", end = '')

    # printing each element
    else:
        print(spam[i] + ", ", end = '')
    

