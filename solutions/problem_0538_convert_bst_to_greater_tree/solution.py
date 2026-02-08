"""
Problem 538: Convert BST to Greater Tree
=======================================
Difficulty: Medium
Tags: Tree, Depth-First Search, Binary Search Tree, Binary Tree
Pattern: BST / Reverse Inorder

Time Complexity:  O(n)
Space Complexity: O(h)
"""

class Solution:
    def convertBST(self, root):
        self.total = 0
        def traverse(node):
            if not node:
                return
            traverse(node.right)
            self.total += node.val
            node.val = self.total
            traverse(node.left)
        traverse(root)
        return root
