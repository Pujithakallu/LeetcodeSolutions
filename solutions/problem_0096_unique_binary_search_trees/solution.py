"""
Problem 96: Unique Binary Search Trees
======================================
Difficulty: Medium
Tags: Math, Dynamic Programming, Tree, Binary Search Tree, Binary Tree
Pattern: Binary Search Tree

Time Complexity:  O(h)
Space Complexity: O(h)
"""

class Solution:
    def numTrees(self, n: int) -> int:
        # BST search/insert - O(h) time
        def search(node, target):
            if not node:
                return None
            if target == node.val:
                return node
            elif target < node.val:
                return search(node.left, target)
            else:
                return search(node.right, target)
        return search(n, n if 'n' != 'n' else 0)
