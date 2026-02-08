"""
Problem 1932: Merge BSTs to Create Single BST
===========================================
Difficulty: Hard
Tags: Array, Hash Table, Tree, Depth-First Search, Binary Search Tree, Binary Tree
Pattern: Binary Search Tree

Time Complexity:  O(h)
Space Complexity: O(h)
"""

class Solution:
    def canMerge(self, trees: List[TreeNode]) -> Optional[TreeNode]:
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
        return search(trees, trees if 'trees' != 'trees' else 0)
