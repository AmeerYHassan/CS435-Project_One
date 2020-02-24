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
        # If the tree is empty, just insert a root Node
        if (self.root == None):
            self.root = Node(value)
        else:
            currNode = self.root
            newNode = Node(value)

            # Infinite loop, find the new nodes place in the tree, place it and set the parent.
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
    
    # Function that finds a node and returns it.
    def findNode(self, value):
        # Start at the root. If the value is less than the currNode, go left.
        # If it's greater, go right. If you go to a node that has a None child,
        # Return None, else, if you find the node, return the Node.
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
    
    # Function that iteratively deletes nodes.
    def deleteIter (self, value):
        # Find the Node
        currNode = self.findNode(value)
        # Case One: No children.
        # If there are no children, make the parent point to None.
        if (currNode.right is None and currNode.left is None):
            if (currNode.parent.right is currNode):
                currNode.parent.right = None
            elif (currNode.parent.left is currNode):
                currNode.parent.left = None
            currNode.parent = None
        # Case Two: One child
        # If there is a child, set the parent to point to the Node's children instead
        # Of the node.
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
        # If there are two nodes, replace the node with the next greatest.
        elif (currNode.right is not None and currNode.left is not None):
            nextBiggestNode = self.findNextIter(currNode.value)
            self.deleteIter(nextBiggestNode)
            currNode.value = nextBiggestNode

    # Find the next greatest node.
    def findNextIter (self, value):
        # Find the Node
        currNode = self.findNode(value)
        
        # If there is a right branch, go to the right one, and return the left most child of that Node.
        if (currNode.right is not None):
            currNode = currNode.right
            while (currNode.left is not None):
                currNode = currNode.left
            return currNode.value
        # If there is no right branch, you already past the next greatest. Traverse through the parents until you come up from
        # A left subtree
        else:
            while(currNode.parent is not None):
                if (currNode.parent.left is currNode):
                    return currNode.parent.value
                currNode = currNode.parent
        
        return(None)

    # Find the previous node.
    def findPrevIter (self, value):
        # Find the node
        currNode = self.findNode(value)

        # If the node has a left subtree, go to the left once, and then all the way down to the right.
        if (currNode.left is not None):
            currNode = currNode.left
            while (currNode.right is not None):
                currNode = currNode.right
            return currNode.value
        # If there is no subtree, go up the parents until you come up from a right subtree.
        else:
            while(currNode.parent is not None):
                if (currNode.parent.right is currNode):
                    return currNode.parent.value
                currNode = currNode.parent

        return None

    # Find the minimum. Go all the way to the left, return the value
    def findMinIter (self):
        currNode = self.root
        while (currNode.left != None):
            currNode = currNode.left
        else:
            return (currNode.value)
        return None
    
    # Find the maximum. Go all the way to the right, return the value.
    def findMaxIter (self):
        currNode = self.root
        while (currNode.right != None):
            currNode = currNode.right
        else:
            return (currNode.value)
        return None