"""
Problem 617: Merge Two Binary Trees
==================================
Difficulty: Easy
Tags: Tree, Depth-First Search, Breadth-First Search, Binary Tree
Pattern: Tree / DFS

Time Complexity:  O(n)
Space Complexity: O(h)
"""

class Solution:
    def mergeTrees(self, root1, root2):
        if not root1:
            return root2
        if not root2:
            return root1
        root1.val += root2.val
        root1.left = self.mergeTrees(root1.left, root2.left)
        root1.right = self.mergeTrees(root1.right, root2.right)
        return root1
