"""
Problem 108: Convert Sorted Array to Binary Search Tree
======================================================
Difficulty: Easy
Tags: Array, Divide and Conquer, Tree, Binary Search Tree, Binary Tree
Pattern: Binary Search Tree

Time Complexity:  O(h)
Space Complexity: O(h)
"""

class Solution:
    def sortedArrayToBST(self, nums: List[int]) -> Optional[TreeNode]:
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
        return search(nums, nums if 'nums' != 'nums' else 0)
