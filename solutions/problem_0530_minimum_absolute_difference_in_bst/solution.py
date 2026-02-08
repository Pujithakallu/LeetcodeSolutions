"""
Problem 530: Minimum Absolute Difference in BST
==============================================
Difficulty: Easy
Tags: Tree, Depth-First Search, Breadth-First Search, Binary Search Tree, Binary Tree
Pattern: BST / Inorder Traversal

Time Complexity:  O(n)
Space Complexity: O(h)
"""

class Solution:
    def getMinimumDifference(self, root) -> int:
        self.prev = None
        self.min_diff = float('inf')
        def inorder(node):
            if not node:
                return
            inorder(node.left)
            if self.prev is not None:
                self.min_diff = min(self.min_diff, node.val - self.prev)
            self.prev = node.val
            inorder(node.right)
        inorder(root)
        return self.min_diff
