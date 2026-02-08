"""
Problem 101: Symmetric Tree
==========================
Difficulty: Easy
Tags: Tree, Depth-First Search, Breadth-First Search, Binary Tree
Pattern: Tree / DFS

Time Complexity:  O(n)
Space Complexity: O(h)
"""

class Solution:
    def isSymmetric(self, root) -> bool:
        def mirror(l, r):
            if not l and not r:
                return True
            if not l or not r:
                return False
            return l.val == r.val and mirror(l.left, r.right) and mirror(l.right, r.left)
        return mirror(root.left, root.right) if root else True
