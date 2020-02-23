# A node class that keeps track of the value, children, and parent of each node in the tree
class Node():
    def __init__ (self, value):
        self.value = value
        self.right = None
        self.left = None
        self.parent = None
    
# A tree class that stores the root node, as well as a list of the inOrder Traversal
class BST():
    def __init__ (self, rootVal):
        self.root = Node(rootVal)
        self.inOrderList = []
    
    # Recursively insert into a BST
    def insertRec(self, currNode, newNode):
        # If the new node is less than the current node, it belongs in the left subtree.
        # If the left subtree of the node is None, insert the node. Else, call insert on the left subtree
        if (newNode.value < currNode.value):
            if (currNode.right is None):
                currNode.right = newNode
                newNode.parent = currNode
            else:
                self.insertRec(currNode.right, newNode)
        # If the new node is greater than the current node, it belongs in the right subtree.
        # If the right subtree of the node is None, insert the node, Else, call insert on the right subtree
        elif (newNode.value > currNode.value):
            if (currNode.left is None):
                currNode.left = newNode
                newNode.parent = currNode
            else:
                self.insertRec(currNode.left, newNode)
    
    # Delete a value from a tree.
    def deleteRec(self, currNode, value):
        # First, find the value in the tree.
        if (currNode.value > value):
            self.deleteRec(currNode.right, value)
        elif (currNode.value < value):
            self.deleteRec(currNode.left, value)
        # Found the Node
        else:
            # Delete node with no children
            if (currNode.right is None and currNode.left is None):
                # If the node has no children, just set the parent node to point to None.
                if (currNode.parent.left is currNode):
                    currNode.parent.left = None
                    return
                elif (currNode.parent.right is currNode):
                    currNode.parent.right = None
                    return
            # Delete node with one child
            if ((currNode.right is None and currNode.left is not None) or (currNode.left is None and currNode.right is not None)):
                # If the node has one child, set the parent node to point to the current Node's child
                if (currNode.parent.left is currNode):
                    currNode.parent.left = currNode.left
                    return
                elif (currNode.parent.right is currNode):
                    currNode.parent.right = currNode.right
                    return
            # Delete node with two children
            # If the node has two children, find the next biggest node from the subtree, replace it
            # with the new node, delete the node you replaced it with.
            nextBiggestVal = self.findNextRec(value)
            self.deleteRec(self.root, nextBiggestVal)
            currNode.value = nextBiggestVal
                
    # Helper function for inOrder, resets the inOrder list and starts an inOrder traversal
    def inOrder(self, currNode):
        self.inOrderList = []
        self.inOrderHelper(currNode)

    # Visit left child, then append, then right child.
    def inOrderHelper(self, currNode):
        if currNode != None:
            self.inOrderHelper(currNode.left)
            self.inOrderList.append(currNode.value)
            self.inOrderHelper(currNode.right)
    
    # Generate an inorder traversal, return the value of the item at index(value) - 1
    def findNextRec(self, value):
        self.inOrder(self.root)
        targetIdx = self.inOrderList.index(value)-1
        if (targetIdx >= 0):
            return(self.inOrderList[targetIdx])
        else:
            return(self.inOrderList[0])

    # Generate an inorder traversal, return the value of the item at index(value) + 1 
    def findPrevRec(self, value):
        self.inOrder(self.root)
        targetIdx = self.inOrderList.index(value)+1
        if (targetIdx <= len(self.inOrderList)):
            return(self.inOrderList[targetIdx])
        else:
            return(self.inOrderList[-1])
    
    # Generate an inorder traversal, return the value of the item at the end of the list
    def findMinRec(self, value):
        self.inOrder(self.root)
        return(self.inOrderList[-1])

    # Generate an inorder traversal, return the value of the item at the start of the list
    def findMaxRec(self, value):
        self.inOrder(self.root)
        return(self.inOrderList[0])
    
def bstSort(arr):
    # Create a new BST using the first element in the array
    sortedBST = BST(arr[0])

    # Iterate through the rest of the array, add it to the BST.
    for num in range(1, len(arr)):
        sortedBST.insertRec(sortedBST.root, Node(arr[num]))
    
    # Return the inOrder traversal of the BST.
    sortedBST.inOrder(sortedBST.root)
    return sortedBST.inOrderList

print(bstSort([4, 3, 1, 5, 22, 42, 65, 21, 42]))