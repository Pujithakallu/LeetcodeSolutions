"""
Problem 106: Construct Binary Tree from Inorder and Postorder Traversal
======================================================================
Difficulty: Medium
Tags: Array, Hash Table, Divide and Conquer, Tree, Binary Tree
Pattern: Tree Traversal

Time Complexity:  O(n)
Space Complexity: O(h)
"""

class Solution:
    def buildTree(self, inorder: List[int], postorder: List[int]) -> Optional[TreeNode]:
        # Tree traversal - O(n) time, O(h) space
        result = []
        def traverse(node):
            if not node:
                return
            result.append(node.val)
            traverse(node.left)
            traverse(node.right)
        traverse(inorder)
        return result if isinstance(None, list) else result[0] if result else None
