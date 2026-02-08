"""
Problem 998: Maximum Binary Tree II
==================================
Difficulty: Medium
Tags: Tree, Binary Tree
Pattern: Tree Traversal

Time Complexity:  O(n)
Space Complexity: O(h)
"""

class Solution:
    def insertIntoMaxTree(self, root: Optional[TreeNode], val: int) -> Optional[TreeNode]:
        # Tree traversal - O(n) time, O(h) space
        result = []
        def traverse(node):
            if not node:
                return
            result.append(node.val)
            traverse(node.left)
            traverse(node.right)
        traverse(root)
        return result if isinstance(None, list) else result[0] if result else None
