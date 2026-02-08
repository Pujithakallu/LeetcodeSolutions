"""
Problem 236: Lowest Common Ancestor of a Binary Tree
===================================================
Difficulty: Medium
Tags: Tree, Depth-First Search, Binary Tree
Pattern: Tree / DFS

Time Complexity:  O(n)
Space Complexity: O(h)
"""

class Solution:
    def lowestCommonAncestor(self, root, p, q):
        if not root or root == p or root == q:
            return root
        left = self.lowestCommonAncestor(root.left, p, q)
        right = self.lowestCommonAncestor(root.right, p, q)
        if left and right:
            return root
        return left or right
