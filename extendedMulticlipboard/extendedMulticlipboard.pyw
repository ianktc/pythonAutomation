# Program to keep track of multiple pieces of text
# Saves and loads pieces of text to the clipboard

# Usage: py.exe mcb.extendedMulticlipboard save <keyword> - Saves keyword to clipboard.
#        py.exe mcb.extendedMulticlipboard <keyword> - Loads keyword to clipboard.
#        py.exe mcb.extendedMulticlipboard list - Loads all keywords to clipboard.

# run from cmd using above commands

import shelve, pyperclip, sys

mcbShelf = shelve.open('mcb')

# TO-DO: Save clipboard content

if len(sys.argv) == 3 and sys.argv[1].lower() == 'save':
    mcbShelf[sys.argv[2]] = pyperclip.paste()

# TO-DO: List keywords and load content
elif len(sys.argv) == 2:
    if sys.argv[1].lower() == 'list':
        pyperclip.copy(str(list(mcbShelf.keys())))

    elif sys.argv[1].lower() == 'delete':
        for key in list(mcbShelf.keys()):
            del mcbShelf[key]
        pyperclip.copy('')
    
    elif sys.argv[1] in mcbShelf:
        pyperclip.copy(mcbShelf[sys.argv[1]])

mcbShelf.close()
