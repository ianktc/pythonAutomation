def collatz (num):

    # checking if num is even
    if (num % 2) == 0:
        print (num / 2)
        return (num / 2)
    # checking if num is odd
    else:
        print(3 * num + 1)
        return(3 * num + 1)

# prompting user for input, and running collatz accordingly (until 1 is reached)
# implemented try and except to ensure an integer is entered

try:
    print("Input an integer: ")
    num = int(input())
    result = collatz(num)
    while(result != 1):
        result = collatz(result)
except ValueError:
    print("Please input an integer")