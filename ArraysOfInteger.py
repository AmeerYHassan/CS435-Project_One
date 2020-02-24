import random
random.seed()

def getRandomArray(n: int) -> list:
    # Make an empty list, set the maximum value of the list to be twice the size of the list.
    returnList = []
    maxVal = n*2

    # Loop, decrement the loop counter only when a new element is added.
    while (n > 0):
        currValue = random.randint(0, maxVal)
        if (currValue in returnList):
            continue
        else:
            returnList.append(currValue)
            n -= 1
    return returnList

def getSortedArray(n: int) -> list:
    # Make an empty list.
    returnList = []

    # Start at n, append n to the list, decrement n until list is finished.
    while (n > 0):
        returnList.append(n)
        n-=1
    return returnList