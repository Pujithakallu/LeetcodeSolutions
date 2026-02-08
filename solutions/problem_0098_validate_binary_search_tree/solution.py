"""
Problem 98: Validate Binary Search Tree
=======================================
Difficulty: Medium
Tags: Tree, Depth-First Search, Binary Search Tree, Binary Tree
Pattern: Tree / DFS

Time Complexity:  O(n)
Space Complexity: O(h)
"""

class Solution:
    def isValidBST(self, root) -> bool:
        def validate(node, lo, hi):
            if not node:
                return True
            if node.val <= lo or node.val >= hi:
                return False
            return validate(node.left, lo, node.val) and validate(node.right, node.val, hi)
        return validate(root, float('-inf'), float('inf'))
