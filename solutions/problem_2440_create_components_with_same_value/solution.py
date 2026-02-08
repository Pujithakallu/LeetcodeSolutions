"""
Problem 2440: Create Components With Same Value
=============================================
Difficulty: Hard
Tags: Array, Math, Tree, Depth-First Search, Enumeration
Pattern: DFS Tree Traversal

Time Complexity:  O(n)
Space Complexity: O(h)
"""

class Solution:
    def componentValue(self, nums: List[int], edges: List[List[int]]) -> int:
        # DFS on binary tree - O(n) time, O(h) space
        def dfs(node):
            if not node:
                return 0
            left = dfs(node.left)
            right = dfs(node.right)
            return 1 + max(left, right)
        
        result = dfs(nums)
        return result
