"""
Problem 99: Recover Binary Search Tree
======================================
Difficulty: Medium
Tags: Tree, Depth-First Search, Binary Search Tree, Binary Tree
Pattern: Binary Search Tree

Time Complexity:  O(h)
Space Complexity: O(h)
"""

class Solution:
    def recoverTree(self, root: Optional[TreeNode]) -> None:
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
        return search(root, root if 'root' != 'root' else 0)
