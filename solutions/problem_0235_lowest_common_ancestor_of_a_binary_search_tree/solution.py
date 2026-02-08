"""
Problem 235: Lowest Common Ancestor of a Binary Search Tree
==========================================================
Difficulty: Medium
Tags: Tree, Depth-First Search, Binary Search Tree, Binary Tree
Pattern: Binary Search Tree

Time Complexity:  O(h)
Space Complexity: O(h)
"""

class Solution:
    def lowestCommonAncestor(self, root: 'TreeNode', p: 'TreeNode', q: 'TreeNode') -> 'TreeNode':
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
        return search(root, p if 'p' != 'root' else 0)
