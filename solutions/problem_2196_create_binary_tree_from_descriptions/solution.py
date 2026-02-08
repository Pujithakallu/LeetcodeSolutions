"""
Problem 2196: Create Binary Tree From Descriptions
================================================
Difficulty: Medium
Tags: Array, Hash Table, Tree, Binary Tree
Pattern: Tree Traversal

Time Complexity:  O(n)
Space Complexity: O(h)
"""

class Solution:
    def createBinaryTree(self, descriptions: List[List[int]]) -> Optional[TreeNode]:
        # Tree traversal - O(n) time, O(h) space
        result = []
        def traverse(node):
            if not node:
                return
            result.append(node.val)
            traverse(node.left)
            traverse(node.right)
        traverse(descriptions)
        return result if isinstance(None, list) else result[0] if result else None
