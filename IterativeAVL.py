import time


class Node():
    def __init__(self, value):
        self.value = value
        self.right = None
        self.left = None
        self.parent = None
        self.height = 1

    def __str__(self):
        if (self.value is not None):
            return str(self.value)
        return None


class AVL():
    def __init__(self):
        self.root = None
        self.traverseCounter = 0

    def insertIter(self, value):
        newNode = Node(value)
        # If the tree is empty, just insert a root Node
        if (self.root == None):
            self.root = newNode
            return
        else:
            currNode = self.root

            # Infinite loop, find the new nodes place in the tree, place it and set the parent.
            while currNode is not None:
                if (newNode.value > currNode.value):
                    if (currNode.right is None):
                        newNode.parent = currNode
                        currNode.right = newNode
                        break
                    else:
                        currNode = currNode.right
                        self.traverseCounter += 1
                elif (newNode.value < currNode.value):
                    if (currNode.left is None):
                        newNode.parent = currNode
                        currNode.left = newNode
                        break
                    else:
                        currNode = currNode.left
                        self.traverseCounter += 1
                else:
                    break

        self.updateHeights(newNode)

    def updateHeightsNoBF(self, newNode):
        while (newNode is not None):
            if (newNode.left is None and newNode.right is None):
                newNode.height = 1
            if (newNode.left is None and newNode.right is not None):
                newNode.height = newNode.right.height + 1
            elif (newNode.left is not None and newNode.right is None):
                newNode.height = newNode.left.height + 1
            elif (newNode.left is not None and newNode.right is not None):
                newNode.height = max(newNode.left.height, newNode.right.height) + 1
            newNode = newNode.parent

    def updateHeights(self, newNode):
        # Update the height of each node, starting from the new node.
        # While updating the height, calculate the balance factor.
        # If the balance factor is >1 or < -1, call the balance function.
        nodeList = []
        while (newNode is not None):
            balanceFactor = 0
            if (newNode.left is None and newNode.right is None):
                newNode.height = 1
                nodeList.append(newNode)
            if (newNode.left is None and newNode.right is not None):
                newNode.height = newNode.right.height + 1
                balanceFactor = newNode.right.height * -1
                nodeList.append(newNode)
            elif (newNode.left is not None and newNode.right is None):
                newNode.height = newNode.left.height + 1
                balanceFactor = newNode.left.height
                nodeList.append(newNode)
            elif (newNode.left is not None and newNode.right is not None):
                newNode.height = max(newNode.left.height, newNode.right.height) + 1
                balanceFactor = newNode.left.height - newNode.right.height
                nodeList.append(newNode)

            if (balanceFactor > 1 or balanceFactor < -1):
                self.balance(nodeList[-3], balanceFactor)
                break

            newNode = newNode.parent

    def balance(self, newNode, balanceFactor):
        # Balance functions determine what rotation to do.
        if (balanceFactor > 1):
            if (newNode.value < newNode.parent.value):
                self.left_left(newNode)
            else:
                self.left_right(newNode)
        if (balanceFactor < -1):
            if (newNode.value > newNode.parent.value):
                self.right_right(newNode)
            else:
                self.right_left(newNode)

    def left_left(self, C):
        #             A                     B
        #            / \                 /    \
        #           B  T4               C      A
        #          / \     -->         / \    / \
        #         C  T3               T1 T2  T3 T4
        #        / \
        #       T1 T2

        # Do the rotation
        A = C.parent.parent
        B = C.parent

        P = A.parent
        if (B.right is not None):
            B.right.parent = A

        A.left = B.right
        B.right = A
        A.parent = B
        B.parent = P

        # If the parent of the first node is not None, set the child of the parent.
        if (P is not None):
            if (P.left is A):
                P.left = B
            else:
                P.right = B

        # If we changed the root of the tree, change the root to the new root.
        if (self.root is A):
            self.root = B

        self.updateHeightsNoBF(C)
        self.updateHeightsNoBF(A)

    def right_right(self, C):
        #      A                      B
        #     / \                  /     \
        #    T1  B        ->      A       C
        #       / \              / \     / \
        #      T2  C            T1 T2   T3  T4
        #         / \
        #        T3  T4
        A = C.parent.parent
        B = C.parent
        P = A.parent

        if (B.left is not None):
            B.left.parent = A

        A.right = B.left
        B.left = A
        B.right = C

        A.parent = B
        B.parent = P

        if (P is not None):
            if (P.left is A):
                P.left = B
            else:
                P.right = B

        if (self.root is A):
            self.root = B

        self.updateHeightsNoBF(C)
        self.updateHeightsNoBF(A)

    def left_right(self, C):
        #         A                  A                 C
        #        / \                / \              /   \
        #       B  T1              C  T1            B     A
        #      / \       -->      / \     -->     /  \   /  \
        #     T2  C              B  T4           T2  T3 T4  T1
        #        / \            / \
        #       T3 T4          T2 T3
        A = C.parent.parent
        B = C.parent
        P = A.parent

        if (C.left is not None):
            C.left.parent = B

        A.left = C
        B.right = C.left
        C.left = B

        B.parent = C
        C.parent = A

        self.left_left(B)

    def right_left(self, C):
        #        A                  A                      C
        #       /  \      ->       / \       ->         /     \
        #      T1  B              T1  C                A       B
        #         / \                / \              / \     / \
        #        C  T2              T3  B            T1 T3  T4   T2
        #       / \                   /  \
        #      T3  T4                T4   T2
        A = C.parent.parent
        B = C.parent
        P = A.parent

        if (C.right is not None):
            C.right.parent = B

        B.left = C.right
        C.right = B
        A.right = C

        C.parent = A
        B.parent = C

        self.right_right(B)

    # Function that finds a node and returns it.
    def findNode(self, value):
        # Start at the root. If the value is less than the currNode, go left.
        # If it's greater, go right. If you go to a node that has a None child,
        # Return None, else, if you find the node, return the Node.
        currNode = self.root
        while (currNode.value != value):
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
    def deleteIter(self, value):
        pass

    # Find the next greatest node.
    def findNextIter(self, value):
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
            while (currNode.parent is not None):
                if (currNode.parent.left is currNode):
                    return currNode.parent.value
                currNode = currNode.parent

        return (None)

    # Find the previous node.
    def findPrevIter(self, value):
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
            while (currNode.parent is not None):
                if (currNode.parent.right is currNode):
                    return currNode.parent.value
                currNode = currNode.parent

        return None

    # Find the minimum. Go all the way to the left, return the value
    def findMinIter(self):
        currNode = self.root
        while (currNode.left != None):
            currNode = currNode.left
        else:
            return (currNode.value)
        return None

    # Find the maximum. Go all the way to the right, return the value.
    def findMaxIter(self):
        currNode = self.root
        while (currNode.right != None):
            currNode = currNode.right
        else:
            return (currNode.value)
        return None