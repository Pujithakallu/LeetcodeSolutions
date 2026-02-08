"""
Problem 94: Binary Tree Inorder Traversal
=========================================
Difficulty: Easy
Tags: Stack, Tree, Depth-First Search, Binary Tree
Pattern: Tree Traversal / Stack

Time Complexity:  O(n)
Space Complexity: O(n)
"""

class Solution:
    def inorderTraversal(self, root) -> list[int]:
        result = []
        stack = []
        curr = root
        while curr or stack:
            while curr:
                stack.append(curr)
                curr = curr.left
            curr = stack.pop()
            result.append(curr.val)
            curr = curr.right
        return result
