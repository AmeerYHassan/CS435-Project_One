from RecursiveBST import *

def bstSort(arr):
    sortedBST = BST()

    for num in arr:
        sortedBST.insertRec(num)

    sortedBST.inOrder()
    return sortedBST.inOrderList

print(bstSort([6, 4, 22, 54, 65, 11, 43]))