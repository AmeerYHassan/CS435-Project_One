class Node():
    def __init__ (self, value):
        self.value = value
        self.right = None
        self.left = None
        self.parent = None
    
class BST():
    def __init__ (self):
        self.root = None
    
    def insertIter (self, value):
        if (self.root == None):
            self.root = Node(value)
        else:
            currNode = self.root
            newNode = Node(value)

            while True:
                if (newNode.value > currNode.value):
                    if(currNode.right == None):
                        newNode.parent = currNode
                        currNode.right = newNode
                        break
                    else:
                        currNode = currNode.right
                        continue
                elif (newNode.value < currNode.value):
                    if(currNode.left == None):
                        newNode.parent = currNode
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
             
    def findNode(self, value):
        currNode = self.root
        while(currNode.value != value):
            if (value > currNode.value):
                if (currNode.right is None):
                    return None
                currNode = currNode.right
                continue
            elif (value < currNode.value):
                if (currNode.left is None):
                    return None
                currNode = currNode.left
                continue
        return currNode

    def deleteIter (self, value):
        # Case One: No children.
        currNode = self.findNode(value)
        if (currNode.right is None and currNode.left is None):
            if (currNode.parent.right is currNode):
                currNode.parent.right = None
            elif (currNode.parent.left is currNode):
                currNode.parent.left = None
            currNode.parent = None
        # Case Two: One child
        elif (currNode.right is not None and currNode.left is None):
            if (currNode.parent.right is currNode):
                currNode.parent.right = currNode.right
            elif (currNode.parent.left is currNode):
                currNode.parent.left = currNode.right
        elif (currNode.right is None and currNode.left is not None):
            if (currNode.parent.right is currNode):
                currNode.parent.right = currNode.left
            elif (currNode.parent.left is currNode):
                currNode.parent.left = currNode.left
        # Case Three: Two children
        elif (currNode.right is not None and currNode.left is not None):
            nextBiggestNode = self.findNextIter(currNode.value)
            self.deleteIter(nextBiggestNode)
            currNode.value = nextBiggestNode

    def findNextIter (self, value):
        currNode = self.findNode(value)
        
        if (currNode.right is not None):
            currNode = currNode.right
            while (currNode.left is not None):
                currNode = currNode.left
            return currNode.value
        else:
            while(currNode.parent is not None):
                if (currNode.parent.left is currNode):
                    return currNode.parent.value
                currNode = currNode.parent
        
        return(None)

    def findPrevIter (self, value):
        currNode = self.findNode(value)

        if (currNode.left is not None):
            currNode = currNode.left
            while (currNode.right is not None):
                currNode = currNode.right
            return currNode.value
        else:
            while(currNode.parent is not None):
                if (currNode.parent.right is currNode):
                    return currNode.parent.value
                currNode = currNode.parent

        return None

    def findMinIter (self):
        currNode = self.root
        while (currNode.left != None):
            currNode = currNode.left
        else:
            return (currNode.value)
        return None
    
    def findMaxIter (self):
        currNode = self.root
        while (currNode.right != None):
            currNode = currNode.right
        else:
            return (currNode.value)
        return None