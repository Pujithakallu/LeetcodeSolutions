"""
Problem 1766: Tree of Coprimes
============================
Difficulty: Hard
Tags: Array, Math, Tree, Depth-First Search, Number Theory
Pattern: DFS Tree Traversal

Time Complexity:  O(n)
Space Complexity: O(h)
"""

class Solution:
    def getCoprimes(self, nums: List[int], edges: List[List[int]]) -> List[int]:
        # DFS on binary tree - O(n) time, O(h) space
        def dfs(node):
            if not node:
                return 0
            left = dfs(node.left)
            right = dfs(node.right)
            return 1 + max(left, right)
        
        result = dfs(nums)
        return result
