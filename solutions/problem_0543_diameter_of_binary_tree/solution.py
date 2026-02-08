"""
Problem 543: Diameter of Binary Tree
===================================
Difficulty: Easy
Tags: Tree, Depth-First Search, Binary Tree
Pattern: Tree / DFS

Time Complexity:  O(n)
Space Complexity: O(h)
"""

class Solution:
    def diameterOfBinaryTree(self, root) -> int:
        self.diameter = 0
        def depth(node):
            if not node:
                return 0
            left = depth(node.left)
            right = depth(node.right)
            self.diameter = max(self.diameter, left + right)
            return 1 + max(left, right)
        depth(root)
        return self.diameter
