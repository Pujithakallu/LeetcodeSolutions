"""
Problem 100: Same Tree
=====================
Difficulty: Easy
Tags: Tree, Depth-First Search, Breadth-First Search, Binary Tree
Pattern: Tree / DFS

Time Complexity:  O(n)
Space Complexity: O(h)
"""

class Solution:
    def isSameTree(self, p, q) -> bool:
        if not p and not q:
            return True
        if not p or not q:
            return False
        return p.val == q.val and self.isSameTree(p.left, q.left) and self.isSameTree(p.right, q.right)
