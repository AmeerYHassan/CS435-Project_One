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
    
    def inOrder(self):
        self.inOrderList = []
        self.inOrderHelper(self.root)
    
    def inOrderHelper(self, currNode):
        if currNode != None:
            self.inOrderHelper(currNode.left)
            self.inOrderList.append(currNode.value)
            self.inOrderHelper(currNode.right)
    
    def findNextRec(self, value):
        self.inOrder()
        if value in self.inOrderList:
            targetIdx = self.inOrderList.index(value)+1
            if (targetIdx >= 0):
                return(self.inOrderList[targetIdx])
            else:
                return(self.inOrderList[0])
    
    def findPrevRec(self, value):
        self.inOrder()
        if value in self.inOrderList:
            targetIdx = self.inOrderList.index(value)-1
            if (targetIdx <= len(self.inOrderList)):
                return(self.inOrderList[targetIdx])
            else:
                return(self.inOrderList[-1])
    
    def findMinRec(self):
        self.inOrder()
        return(self.inOrderList[0])
    
    def findMaxRec(self):
        self.inOrder()
        return(self.inOrderList[-1])

def bstSort(arr):
    sortedBST = BST()

    for num in range(len(arr)):
        sortedBST.insertRec(sortedBST.root, Node(arr[num]))
    
    sortedBST.inOrder(sortedBST.root)
    return sortedBST.inOrderList

currBST = BST()
currBST.insertRec(5)
currBST.insertRec(3)
currBST.insertRec(12)
currBST.insertRec(54)
currBST.insertRec(86)
currBST.insertRec(35)
currBST.insertRec(75)
currBST.insertRec(32)
currBST.insertRec(30)
currBST.insertRec(31)
currBST.insertRec(92)
currBST.insertRec(83)
currBST.insertRec(2)

currBST.inOrder()
print(currBST.inOrderList)

currBST.deleteRec(86)
currBST.inOrder()
print(currBST.inOrderList)

currBST.deleteRec(54)
currBST.inOrder()
print(currBST.inOrderList)

currBST.deleteRec(5)
currBST.inOrder()
print(currBST.inOrderList)