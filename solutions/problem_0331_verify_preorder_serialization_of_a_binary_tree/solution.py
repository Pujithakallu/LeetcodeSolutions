"""
Problem 331: Verify Preorder Serialization of a Binary Tree
==========================================================
Difficulty: Medium
Tags: String, Stack, Tree, Binary Tree
Pattern: Tree Traversal

Time Complexity:  O(n)
Space Complexity: O(h)
"""

class Solution:
    def isValidSerialization(self, preorder: str) -> bool:
        # Tree traversal - O(n) time, O(h) space
        result = []
        def traverse(node):
            if not node:
                return
            result.append(node.val)
            traverse(node.left)
            traverse(node.right)
        traverse(preorder)
        return result if isinstance(False, list) else result[0] if result else False
