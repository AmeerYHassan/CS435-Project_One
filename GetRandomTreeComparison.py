import RecursiveBST as RBST
import IterativeBST as IBST
from IterativeAVL import *
from ArraysOfInteger import *
import time

numElements = 10000
randomList = getRandomArray(numElements)
sortedList = getSortedArray(numElements)

# Random Array Tree Population
AVLTreeRandom = AVL()
RecursiveBSTRandom = RBST.BST()
IterativeBSTRandom = IBST.BST()

AVLStart = time.time()
for randomElem in randomList:
    AVLTreeRandom.insertIter(randomElem)
AVLEnd = time.time()

RecursiveBSTStart = time.time()
for randomElem in randomList:
    RecursiveBSTRandom.insertRec(randomElem)
RecursiveBSTEnd = time.time()

IterativeBSTStart = time.time()
for randomElem in randomList:
    IterativeBSTRandom.insertIter(randomElem)
IterativeBSTEnd = time.time()

print(f"Stats to input {numElements} random elements:")
print(f"\tAVL Tree: {AVLEnd-AVLStart} seconds.")
print(f"\tAVL Tree Calls: {AVLTreeRandom.traverseCounter}\n")
print(f"\tRecursive BST: {RecursiveBSTEnd-RecursiveBSTStart} seconds.")
print(f"\tRecursive BST Calls: {RecursiveBSTRandom.traverseCounter}\n")
print(f"\tIterative BST: {IterativeBSTEnd-IterativeBSTStart} seconds.")
print(f"\tIterative BST Calls: {IterativeBSTRandom.traverseCounter}\n")

# Sorted Array Tree Population
AVLTreeSorted = AVL()
RecursiveBSTSorted = RBST.BST()
IterativeBSTSorted = IBST.BST()

AVLStart = time.time()
for randomElem in randomList:
    AVLTreeSorted.insertIter(randomElem)
AVLEnd = time.time()

RecursiveBSTStart = time.time()
for randomElem in randomList:
    RecursiveBSTSorted.insertRec(randomElem)
RecursiveBSTEnd = time.time()

IterativeBSTStart = time.time()
for randomElem in randomList:
    IterativeBSTSorted.insertIter(randomElem)
IterativeBSTEnd = time.time()

print(f"Stats to input {numElements} sorted elements:")
print(f"\tAVL Tree: {AVLEnd-AVLStart} seconds.")
print(f"\tAVL Tree Calls: {AVLTreeSorted.traverseCounter}\n")
print(f"\tRecursive BST: {RecursiveBSTEnd-RecursiveBSTStart} seconds.")
print(f"\tRecursive BST Calls: {RecursiveBSTSorted.traverseCounter}\n")
print(f"\tIterative BST: {IterativeBSTEnd-IterativeBSTStart} seconds.")
print(f"\tIterative BST Calls: {IterativeBSTSorted.traverseCounter}\n")