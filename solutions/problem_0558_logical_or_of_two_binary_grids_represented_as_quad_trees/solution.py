"""
Problem 558: Logical OR of Two Binary Grids Represented as Quad-Trees
====================================================================
Difficulty: Medium
Tags: Divide and Conquer, Tree
Pattern: Tree Traversal

Time Complexity:  O(n)
Space Complexity: O(h)
"""

class Node:
    def __init__(self, val: int, isLeaf: int, topLeft: int, topRight: int, bottomLeft: int, bottomRight: int):
        # Initialize data structure
        self.val = val
        self.isLeaf = isLeaf
        self.topLeft = topLeft
        self.topRight = topRight
        self.bottomLeft = bottomLeft
        self.bottomRight = bottomRight

    def intersect(self, quadTree1: 'Node', quadTree2: 'Node') -> 'Node':
        return None

