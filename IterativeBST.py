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
    
    def deleteNoChildrenIter(self, currNode):
        # If there are no children, make the parent point to None.
        if (currNode.parent.right is currNode):
                currNode.parent.right = None
                currNode.parent = None
        elif (currNode.parent.left is currNode):
                currNode.parent.left = None
                currNode.parent = None

    def deleteOneChildIter(self, currNode):
         # If there is a child, set the parent to point to the Node's children instead
        # Of the node.
        if (currNode.parent.left is currNode):
            if(currNode.left is not None):
                currNode.parent.left = currNode.left
            else:
                currNode.parent.left = currNode.right
        else:
            if(currNode.left is not None):
                currNode.parent.right = currNode.left
            else:
                currNode.parent.right = currNode.right

    def deleteTwoChildrenIter(self, currNode):
        # If there are two nodes, replace the node with the next greatest.
        nextBiggestNode = self.findNextIter(currNode.value)
        self.deleteIter(nextBiggestNode)
        currNode.value = nextBiggestNode
        
    # Function that iteratively deletes nodes.
    def deleteIter (self, value):
        # Find the Node
        currNode = self.findNode(value)
        # Case One: No children.
        if (currNode.right is None and currNode.left is None):
            self.deleteNoChildrenIter(currNode)
            return

        # Case Two: One child
        if ((currNode.right is None and currNode.left is not None) or
                (currNode.left is None and currNode.right is not None)):
            self.deleteOneChildIter(currNode)
            return

        # Case Three: Two children
        elif (currNode.right is not None and currNode.left is not None):
            self.deleteTwoChildrenIter(currNode)

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

myBST = BST()
myList = [676, 643, 1248, 1813, 1874, 316, 1252, 84, 1989, 1683, 1913, 1411, 1435, 589, 517, 1216, 989, 905, 960, 1620, 1605, 797, 1099, 1870, 371, 596, 1586, 1777, 1705, 409, 1635, 1194, 786, 791, 1886, 55, 690, 477, 1384, 264, 305, 1600, 1509, 294, 521, 1859, 997, 1203, 307, 410, 1632, 1571, 818, 1075, 1835, 201, 1541, 1243, 1843, 566, 258, 1133, 1151, 803, 369, 1697, 1064, 1333, 1992, 674, 471, 1294, 1397, 1360, 1458, 1287, 848, 1792, 1106, 746, 828, 1289, 881, 1279, 704, 1176, 946, 568, 200, 1606, 219, 472, 1155, 1531, 1297, 1812, 379, 837, 999, 488, 1469, 1358, 1908, 1147, 711, 202, 826, 917, 154, 1112, 1766, 732, 629, 1326, 8, 787, 1196, 1315, 473, 652, 140, 867, 941, 874, 915, 1809, 1274, 965, 1264, 1819, 1656, 1755, 1012, 33, 556, 387, 1626, 1533, 1548, 580, 1807, 1653, 1997, 986, 1104, 785, 1468, 161, 1839, 1308, 1588, 1375, 490, 435, 346, 1161, 1595, 1818, 1402, 1428, 666, 313, 633, 211, 555, 1090, 543, 1507, 681, 1785, 1783, 693, 401, 280, 1088, 1028, 734, 1356, 623, 1919, 520, 569, 1065, 1975, 871, 1837, 1538, 431, 395, 641, 1964, 1236, 1247, 1359, 324, 1730, 1815, 240, 1385, 279, 519, 932, 1771, 1060, 1782, 203, 1877, 668, 461, 1576, 1199, 1912, 1214, 767, 525, 1738, 1417, 212, 1164, 957, 1056, 77, 342, 1984, 322, 966, 1085, 458, 402, 1561, 649, 385, 62, 1372, 494, 1893, 1327, 1301, 226, 1462, 1865, 1011, 296, 921, 953, 1175, 1220, 821, 532, 842, 1149, 1377, 1669, 534, 1495, 1485, 835, 1659, 1211, 1497, 1714, 1145, 529, 254, 934, 1712, 805, 428, 958, 1899, 1422, 845, 50, 878, 360, 1299, 222, 1324, 1593, 1944, 1642, 1528, 1664, 1655, 1231, 1152, 1651, 1110, 1810, 1464, 984, 1621, 1158, 576, 950, 1676, 1157, 673, 129, 1496, 1798, 1217, 1935, 1035, 502, 1213, 189, 650, 1037, 29, 21, 1937, 1254, 347, 1928, 1562, 1933, 707, 1178, 24, 382, 1690, 1862, 450, 1429, 1673, 1668, 1087, 425, 575, 1416, 1502, 1909, 1228, 1319, 1282, 1344, 1405, 616, 1126, 1767, 1366, 291, 755, 1325, 215, 1480, 1604, 1568, 0, 559, 1725, 1066, 1486, 833, 448, 1271, 1888, 1863, 344, 739, 1160, 748, 194, 1102, 572, 56, 862, 1167, 470, 725, 1003, 1894, 951, 1882, 667, 645, 179, 653, 900, 1051, 620, 309, 717, 1276, 424, 265, 442, 380, 1367, 1257, 1687, 124, 780, 86, 283, 964, 19, 814, 1266, 743, 552, 407, 207, 1521, 935, 341, 1589, 1680, 486, 841, 1587, 285, 1323, 1601, 478, 499, 1670, 1131, 1756, 562, 1451, 303, 1665, 945, 1795, 1791, 1433, 635, 1754, 736, 439, 794, 1779, 1739, 1302, 542, 1698, 10, 474, 295, 1749, 1044, 1156, 1923, 687, 1840, 1475, 516, 859, 1298, 632, 1700, 1557, 1744, 467, 560, 1663, 1479, 1166, 577, 636, 1049, 1534, 1759, 105, 1965, 1379, 404, 1005, 1191, 1173, 1753, 1478, 1684, 1245, 642, 1369, 190, 1526, 45, 391, 1554, 1907, 581, 868, 1230, 807, 170, 1311, 1432, 230, 535, 1689, 108, 1853, 1283, 74, 843, 11, 1244, 320, 14, 656, 1022, 890, 646, 1020, 1038, 1875, 1332, 806, 40, 720, 15, 70, 333, 289, 492, 1392, 1946, 1184, 1027, 464, 1969, 1743, 1351, 1284, 290, 462, 1776, 1111, 1896, 51, 1868, 34, 682, 860, 270, 1758, 1532, 1535, 1341, 420, 1336, 849, 1154, 1455, 1122, 1609, 1645, 930, 994, 1679, 166, 1080, 727, 1752, 749, 1494, 399, 493, 1074, 536, 122, 253, 1960, 1695, 851, 260, 1361, 311, 973, 1855, 1746, 701, 151, 680, 1598, 1942, 220, 982, 1584, 1306, 1072, 611, 969, 799, 1261, 1124, 366, 36, 1867, 852, 1346, 441, 1253, 564, 1431, 1212, 1490, 132, 1648, 744, 390, 916, 25, 1579, 1305, 1138, 1962, 1866, 273, 1985, 1484, 730, 116, 1267, 1828, 1098, 663, 1639, 978, 149, 816, 329, 774, 1116, 1205, 1030, 82, 798, 745, 1014, 1820, 698, 1409, 1506, 397, 1394, 904, 249, 1103, 1641, 1850, 400, 864, 1258, 1550, 1434, 1186, 1910, 789, 1218, 143, 1135, 1614, 1805, 996, 776, 1511, 79, 1263, 1608, 1542, 1602, 714, 1941, 225, 465, 1780, 1234, 1338, 223, 443, 338, 1125, 241, 282, 1329, 1662, 1644, 910, 1129, 197, 829, 38, 830, 987, 584, 511, 735, 1312, 824, 42, 1000, 1950, 1727, 432, 350, 1892, 1007, 1833, 1543, 1765, 1086, 896, 1209, 30, 1493, 1107, 1915, 1518, 1210, 1841, 1688, 858, 1010, 54, 1317, 1790, 1904, 1500, 205, 1911, 3]

for elem in myList:
    myBST.insertIter(elem)