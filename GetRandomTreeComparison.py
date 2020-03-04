from RecursiveBST import *
from IterativeAVL import *
from ArraysOfInteger import *
import time

randomList = getRandomArray(20)
sortedList = getSortedArray(20)

AVLTreeRandom = AVL()
BSTreeRandom = BST()

AVLStart = time.time()
for randomElem in randomList:
    AVLTreeRandom.insertIter(randomElem)
AVLEnd = time.time()

BSTStart = time.time()
for randomElem in randomList:
    BSTreeRandom.insertRec(randomElem)
BSTEnd = time.time()

print(f"Time to input 20 random elements:\n-----------------------------\nAVL Tree: {AVLEnd-AVLStart} seconds.\nAVL Tree Calls: {AVLTreeRandom.traverseCounter}\n-----------------------------\nRecursive BST: {BSTEnd-BSTStart} seconds.\nRecursive BST Calls: {BSTreeRandom.traverseCounter}\n\n")

AVLTreeSorted = AVL()
BSTreeSorted = BST()

AVLStart = time.time()
for randomElem in randomList:
    AVLTreeSorted.insertIter(randomElem)
AVLEnd = time.time()

BSTStart = time.time()
for randomElem in randomList:
    BSTreeSorted.insertRec(randomElem)
BSTEnd = time.time()

print(f"Time to input 20 sorted elements:\n-----------------------------\nAVL Tree: {AVLEnd-AVLStart} seconds.\nAVL Tree Calls: {AVLTreeSorted.traverseCounter}\n-----------------------------\nRecursive BST: {BSTEnd-BSTStart} seconds. \nRecursive BST Calls: {BSTreeSorted.traverseCounter}")