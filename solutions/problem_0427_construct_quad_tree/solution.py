"""
Problem 427: Construct Quad Tree
===============================
Difficulty: Medium
Tags: Array, Divide and Conquer, Tree, Matrix
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

    def construct(self, grid: List[List[int]]) -> 'Node':
        return None

