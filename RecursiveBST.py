class Node():
    def __init__ (self, value):
        self.value = value
        self.right = None
        self.left = None
        self.parent = None
    
class BST():
    def __init__ (self, rootVal):
        self.root = Node(rootVal)
        self.inOrderList = []
    
    def insertRec(self, currNode, newNode):
        if (newNode.value < currNode.value):
            if (currNode.right is None):
                currNode.right = newNode
                newNode.parent = currNode
            else:
                self.insertRec(currNode.right, newNode)
        elif (newNode.value > currNode.value):
            if (currNode.left is None):
                currNode.left = newNode
                newNode.parent = currNode
            else:
                self.insertRec(currNode.left, newNode)
    
    def deleteRec(self, currNode, value):
        if (currNode.value > value):
            self.deleteRec(currNode.right, value)
        elif (currNode.value < value):
            self.deleteRec(currNode.left, value)
        else:
            # Found the Node
            # Delete node with no children
            if (currNode.right is None and currNode.left is None):
                if (currNode.parent.left is currNode):
                    currNode.parent.left = None
                    return
                elif (currNode.parent.right is currNode):
                    currNode.parent.right = None
                    return
            # Delete node with one child
            if ((currNode.right is None and currNode.left is not None) or (currNode.left is None and currNode.right is not None)):
                if (currNode.parent.left is currNode):
                    currNode.parent.left = currNode.left
                    return
                elif (currNode.parent.right is currNode):
                    currNode.parent.right = currNode.right
                    return
            # Delete node with two children
            nextBiggestVal = self.findNextRec(value)
            self.deleteRec(self.root, nextBiggestVal)
            currNode.value = nextBiggestVal
                
    def inOrder(self, currNode):
        self.inOrderList = []
        self.inOrderHelper(currNode)

    def inOrderHelper(self, currNode):
        if currNode != None:
            self.inOrderHelper(currNode.left)
            self.inOrderList.append(currNode.value)
            self.inOrderHelper(currNode.right)
    
    def findNextRec(self, value):
        self.inOrder(self.root)
        targetIdx = self.inOrderList.index(value)-1
        if (targetIdx >= 0):
            return(self.inOrderList[targetIdx])
        else:
            return(self.inOrderList[0])
    
    def findPrevRec(self, value):
        self.inOrder(self.root)
        targetIdx = self.inOrderList.index(value)+1
        if (targetIdx <= len(self.inOrderList)):
            return(self.inOrderList[targetIdx])
        else:
            return(self.inOrderList[-1])
    
    def findMinRec(self, value):
        self.inOrder(self.root)
        return(self.inOrderList[-1])

    def findMaxRec(self, value):
        self.inOrder(self.root)
        return(self.inOrderList[0])

currBST = BST(1)
currBST.insertRec(currBST.root, Node(5))
currBST.insertRec(currBST.root, Node(3))
currBST.insertRec(currBST.root, Node(12))
currBST.insertRec(currBST.root, Node(54))
currBST.insertRec(currBST.root, Node(86))
currBST.insertRec(currBST.root, Node(35))
currBST.insertRec(currBST.root, Node(75))
currBST.insertRec(currBST.root, Node(32))
currBST.insertRec(currBST.root, Node(30))
currBST.insertRec(currBST.root, Node(31))
currBST.insertRec(currBST.root, Node(92))
currBST.insertRec(currBST.root, Node(83))
currBST.insertRec(currBST.root, Node(2))

currBST.inOrder(currBST.root)
print(currBST.inOrderList)

print("\nRemove 54")
currBST.deleteRec(currBST.root, 54)
currBST.inOrder(currBST.root)
print(currBST.inOrderList)

print("\nRemove 5")
currBST.deleteRec(currBST.root, 5)
currBST.inOrder(currBST.root)
print(currBST.inOrderList)