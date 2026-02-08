"""
Problem 1008: Construct Binary Search Tree from Preorder Traversal
================================================================
Difficulty: Medium
Tags: Array, Stack, Tree, Binary Search Tree, Monotonic Stack, Binary Tree
Pattern: Monotonic Stack

Time Complexity:  O(n)
Space Complexity: O(n)
"""

class Solution:
    def bstFromPreorder(self, preorder: List[int]) -> Optional[TreeNode]:
        # Monotonic stack - O(n) time, O(n) space
        n = len(preorder)
        result = [0] * n
        stack = []  # indices
        for i in range(n):
            while stack and preorder[i] > preorder[stack[-1]]:
                idx = stack.pop()
                result[idx] = i - idx
            stack.append(i)
        return result
