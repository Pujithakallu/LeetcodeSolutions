"""
Problem 2322: Minimum Score After Removals on a Tree
==================================================
Difficulty: Hard
Tags: Array, Bit Manipulation, Tree, Depth-First Search
Pattern: DFS Tree Traversal

Time Complexity:  O(n)
Space Complexity: O(h)
"""

class Solution:
    def minimumScore(self, nums: List[int], edges: List[List[int]]) -> int:
        # DFS on binary tree - O(n) time, O(h) space
        def dfs(node):
            if not node:
                return 0
            left = dfs(node.left)
            right = dfs(node.right)
            return 1 + max(left, right)
        
        result = dfs(nums)
        return result
