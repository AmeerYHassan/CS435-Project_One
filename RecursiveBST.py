class Node():
    def __init__ (self, value):
        self.value = value
        self.right = None
        self.left = None
        self.parent = None

class BST():
    def __init__ (self):
        self.root = None
        self.inOrderList = []
    
    # Set the root if the Tree is empty, else, find the spot and put the node in.
    def insertRec(self, value):
        if(self.root is None):
            self.root = Node(value)
        else:
            self.insertRecHelper(self.root, value)
    
    def insertRecHelper(self, currNode, value):
        if (value > currNode.value):
            if(currNode.right is None):
                currNode.right = Node(value)
                currNode.right.parent = currNode
            else:
                self.insertRecHelper(currNode.right, value)
        elif (value < currNode.value):
            if (currNode.left is None):
                currNode.left = Node(value)
                currNode.left.parent = currNode
            else:
                self.insertRecHelper(currNode.left, value)
    
    def deleteRec(self, value):
        self.deleteRecHelper(self.root, value)

    def deleteRecHelper(self, currNode, value):
        if (value > currNode.value):
            self.deleteRecHelper(currNode.right, value)
        elif (value < currNode.value):
            self.deleteRecHelper(currNode.left, value)
        elif (currNode.value is value):
            # Case one: Leaf Node
            if (currNode.right is None and currNode.left is None):
                if (currNode.parent.left is currNode):
                    currNode.parent.left = None
                    currNode.parent = None
                    return
                elif (currNode.parent.right is currNode):
                    currNode.parent.right = None
                    currNode.parent = None
                    return
            # Case two: Node with one child
            elif ((currNode.right is None and currNode.left is not None) or (currNode.left is None and currNode.right is not None)):
                if(currNode.parent.left is currNode):
                    if(currNode.left is not None):
                        currNode.parent.left = currNode.left
                    elif(currNode.right is not None):
                        currNode.parent.left = currNode.right
                if(currNode.parent.right is currNode):
                    if(currNode.left is not None):
                        currNode.parent.right = currNode.left
                    elif(currNode.right is not None):
                        currNode.parent.right = currNode.right

            # Case Three: Node with two children
            elif (currNode.right is not None and currNode.left is not None):
                nextBiggestVal = self.findNextRec(value)
                self.deleteRecHelper(self.root, nextBiggestVal)
                currNode.value = nextBiggestVal
    
    # Resets the inOrder list, does the inOrder traversal.
    def inOrder(self):
        self.inOrderList = []
        self.inOrderHelper(self.root)
    
    def inOrderHelper(self, currNode):
        if currNode != None:
            self.inOrderHelper(currNode.left)
            self.inOrderList.append(currNode.value)
            self.inOrderHelper(currNode.right)
    
    # Generate the inOrder traversal, check if it is in the list, return the value of the index after it.
    def findNextRec(self, value):
        self.inOrder()
        if value in self.inOrderList:
            targetIdx = self.inOrderList.index(value)+1
            if (targetIdx >= 0):
                return(self.inOrderList[targetIdx])
            else:
                return(self.inOrderList[0])
    
    # Generate the inOrder traversal, check if it is in the list, return the value of the index before it.
    def findPrevRec(self, value):
        self.inOrder()
        if value in self.inOrderList:
            targetIdx = self.inOrderList.index(value)-1
            if (targetIdx <= len(self.inOrderList)):
                return(self.inOrderList[targetIdx])
            else:
                return(self.inOrderList[-1])
        else:
            return None
    
    # Generate the inOrder traversal, return the first element.
    def findMinRec(self):
        self.inOrder()
        return(self.inOrderList[0])
    
    # Generate the inOrder traversal, return the last element.
    def findMaxRec(self):
        self.inOrder()
        return(self.inOrderList[-1])