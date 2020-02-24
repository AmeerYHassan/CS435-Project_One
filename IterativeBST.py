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
    
    def insertIter (self, value):
        currNode = self.root
        newNode = Node(value)

        while True:
            if (newNode.value > currNode.value):
                if(currNode.right == None):
                    currNode.right = newNode
                    break
                else:
                    currNode = currNode.right
                    continue
            elif (newNode.value < currNode.value):
                if(currNode.left == None):
                    currNode.left = newNode
                    break
                else:
                    currNode = currNode.left
                    continue
            else:
                break

    def inOrder(self):
        self.inOrderList = []
        self.inOrderHelper(self.root)

    def inOrderHelper(self, currNode):
        if currNode != None:
            self.inOrderHelper(currNode.left)
            self.inOrderList.append(currNode.value)
            self.inOrderHelper(currNode.right)              

    def deleteIter (self):
        pass
    def findNextIter (self):
        pass
    def findPrevIter (self):
        pass
    def findMinIter (self):
        pass
    def findMaxIter (self):
        pass

currBST = BST(5)
currBST.insertIter(6)
currBST.insertIter(4)
currBST.insertIter(46)
currBST.insertIter(24)
currBST.insertIter(14)
currBST.insertIter(47)
currBST.insertIter(2)
currBST.insertIter(455)
currBST.insertIter(47765)
currBST.insertIter(123414)
currBST.insertIter(42345324)
currBST.insertIter(12344)
currBST.insertIter(45634)
currBST.insertIter(132413244)


currBST.inOrder()
print(currBST.inOrderList)
