"""
Problem 104: Maximum Depth of Binary Tree
========================================
Difficulty: Easy
Tags: Tree, Depth-First Search, Breadth-First Search, Binary Tree
Pattern: Tree / DFS

Time Complexity:  O(n)
Space Complexity: O(h)
"""

class Solution:
    def maxDepth(self, root) -> int:
        if not root:
            return 0
        return 1 + max(self.maxDepth(root.left), self.maxDepth(root.right))
