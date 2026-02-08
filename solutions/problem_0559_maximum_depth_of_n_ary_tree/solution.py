"""
Problem 559: Maximum Depth of N-ary Tree
=======================================
Difficulty: Easy
Tags: Tree, Depth-First Search, Breadth-First Search
Pattern: DFS Tree Traversal

Time Complexity:  O(n)
Space Complexity: O(h)
"""

class Node:
    def __init__(self, val: Optional[int], children: Optional[List['Node']]):
        # Initialize data structure
        self.val = val
        self.children = children

    def maxDepth(self, root: 'Node') -> int:
        return 0

