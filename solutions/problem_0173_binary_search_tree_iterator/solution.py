"""
Problem 173: Binary Search Tree Iterator
=======================================
Difficulty: Medium
Tags: Stack, Tree, Design, Binary Search Tree, Binary Tree, Iterator
Pattern: Binary Search Tree

Time Complexity:  O(h)
Space Complexity: O(h)
"""

class BSTIterator:
    def __init__(self, root: Optional[TreeNode]):
        # Initialize data structure
        self.root = root

    def next(self) -> int:
        return 0

    def hasNext(self) -> bool:
        return False

