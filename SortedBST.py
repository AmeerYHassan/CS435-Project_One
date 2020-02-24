from RecursiveBST import *

def bstSort(arr):
    # Create a BST
    sortedBST = BST()

    # Add all the values from the array into the BST.
    for num in arr:
        sortedBST.insertRec(num)

    # Generate the inOrder traversal for the tree.
    sortedBST.inOrder()
    return sortedBST.inOrderList

print(bstSort([6, 4, 22, 54, 65, 11, 43]))