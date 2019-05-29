# Program that takes the files with size > 100MB and deletes them

# NOTE BE AWARE THAT THE os.unlink METHOD IS PERMANENT

import os, shutil

def prompt(userInput):

    # prompting for the directory to search
    if userInput == 1:
        print("Input a directory to search: ")
        response = input()

    # prompting for the size of file to delete
    else:
        print("Input a size of file to delete: ")
        response = input()

    return response

def fileParse(dirName, fileSize):
    
    # listdir method extracts both files and directories
    contents = os.listdir(dirName)

    # print(contents)
    for file in contents:

        # create path for each file
        path = (dirName + "\\" + file)
        # print(path)

        # finds whether it is file or dir (ignore if dir)
        if os.path.isfile(path):
            # print(os.path.getsize(path))
            if (os.path.getsize(path) > int(fileSize)):
                print("File deleted. ")
                os.unlink(path)


if __name__ == "__main__":
    
    dirName = prompt(1)
    fileSize = prompt(2)

    fileParse(dirName, fileSize)
