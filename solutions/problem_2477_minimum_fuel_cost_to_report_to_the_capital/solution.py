"""
Problem 2477: Minimum Fuel Cost to Report to the Capital
======================================================
Difficulty: Medium
Tags: Tree, Depth-First Search, Breadth-First Search, Graph Theory
Pattern: DFS Tree Traversal

Time Complexity:  O(n)
Space Complexity: O(h)
"""

class Solution:
    def minimumFuelCost(self, roads: List[List[int]], seats: int) -> int:
        # DFS on binary tree - O(n) time, O(h) space
        def dfs(node):
            if not node:
                return 0
            left = dfs(node.left)
            right = dfs(node.right)
            return 1 + max(left, right)
        
        result = dfs(roads)
        return result
