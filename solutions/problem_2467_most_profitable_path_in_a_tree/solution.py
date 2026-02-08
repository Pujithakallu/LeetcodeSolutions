"""
Problem 2467: Most Profitable Path in a Tree
==========================================
Difficulty: Medium
Tags: Array, Tree, Depth-First Search, Breadth-First Search, Graph Theory
Pattern: DFS Tree Traversal

Time Complexity:  O(n)
Space Complexity: O(h)
"""

class Solution:
    def mostProfitablePath(self, edges: List[List[int]], bob: int, amount: List[int]) -> int:
        # DFS on binary tree - O(n) time, O(h) space
        def dfs(node):
            if not node:
                return 0
            left = dfs(node.left)
            right = dfs(node.right)
            return 1 + max(left, right)
        
        result = dfs(edges)
        return result
