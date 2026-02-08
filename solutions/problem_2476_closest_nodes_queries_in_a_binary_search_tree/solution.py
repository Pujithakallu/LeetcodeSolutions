"""
Problem 2476: Closest Nodes Queries in a Binary Search Tree
=========================================================
Difficulty: Medium
Tags: Array, Binary Search, Tree, Depth-First Search, Binary Search Tree, Binary Tree
Pattern: Binary Search Tree

Time Complexity:  O(h)
Space Complexity: O(h)
"""

class Solution:
    def closestNodes(self, root: Optional[TreeNode], queries: List[int]) -> List[List[int]]:
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
        return search(root, queries if 'queries' != 'root' else 0)
