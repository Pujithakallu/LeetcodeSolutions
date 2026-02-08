"""
Problem 2236: Root Equals Sum of Children
=======================================
Difficulty: Easy
Tags: Tree, Binary Tree
Pattern: Tree Traversal

Time Complexity:  O(n)
Space Complexity: O(h)
"""

class Solution:
    def checkTree(self, root: Optional[TreeNode]) -> bool:
        # Tree traversal - O(n) time, O(h) space
        result = []
        def traverse(node):
            if not node:
                return
            result.append(node.val)
            traverse(node.left)
            traverse(node.right)
        traverse(root)
        return result if isinstance(False, list) else result[0] if result else False
