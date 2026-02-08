"""
Problem 653: Two Sum IV - Input is a BST
=======================================
Difficulty: Easy
Tags: Hash Table, Two Pointers, Tree, Depth-First Search, Breadth-First Search, Binary Search Tree, Binary Tree
Pattern: Binary Search Tree

Time Complexity:  O(h)
Space Complexity: O(h)
"""

class Solution:
    def findTarget(self, root: Optional[TreeNode], k: int) -> bool:
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
        return search(root, k if 'k' != 'root' else 0)
