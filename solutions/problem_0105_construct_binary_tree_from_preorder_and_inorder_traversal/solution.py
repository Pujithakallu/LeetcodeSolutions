"""
Problem 105: Construct Binary Tree from Preorder and Inorder Traversal
=====================================================================
Difficulty: Medium
Tags: Array, Hash Table, Divide and Conquer, Tree, Binary Tree
Pattern: Tree Traversal

Time Complexity:  O(n)
Space Complexity: O(h)
"""

class Solution:
    def buildTree(self, preorder: List[int], inorder: List[int]) -> Optional[TreeNode]:
        # Tree traversal - O(n) time, O(h) space
        result = []
        def traverse(node):
            if not node:
                return
            result.append(node.val)
            traverse(node.left)
            traverse(node.right)
        traverse(preorder)
        return result if isinstance(None, list) else result[0] if result else None
