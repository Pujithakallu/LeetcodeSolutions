"""
Problem 230: Kth Smallest Element in a BST
=========================================
Difficulty: Medium
Tags: Tree, Depth-First Search, Binary Search Tree, Binary Tree
Pattern: Tree / Inorder Traversal

Time Complexity:  O(h+k)
Space Complexity: O(h)
"""

class Solution:
    def kthSmallest(self, root, k: int) -> int:
        stack = []
        curr = root
        while curr or stack:
            while curr:
                stack.append(curr)
                curr = curr.left
            curr = stack.pop()
            k -= 1
            if k == 0:
                return curr.val
            curr = curr.right
        return -1
