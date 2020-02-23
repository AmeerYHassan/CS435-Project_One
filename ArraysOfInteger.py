import random
random.seed()

def getRandomArray(n: int) -> list:
    """Generates a list with random elements given array size (n).

    Each element in the array is distinct, there are no
    repeating elements.

    Args:
        n (int): The size of the resulting array.

    Returns:
        returnList: The list of random elements of size n.
    """

    # Initializing the list and maximum value of random integers, in this case
    # The maximum value is set to double the list length to prevent any huge 
    # numbers.
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
    """Generates a list with decrementing size given array size (n).

    Args:
        n (int): The size of the resulting array.

    Returns:
        returnList: The list of consecutive elements of size n.
    """
    returnList = []

    # Start at n, append n to the list, decrement n until list is finished.
    while (n > 0):
        returnList.append(n)
        n-=1
    return returnList