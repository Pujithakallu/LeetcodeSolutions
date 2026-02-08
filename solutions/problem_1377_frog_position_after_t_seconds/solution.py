"""
Problem 1377: Frog Position After T Seconds
=========================================
Difficulty: Hard
Tags: Tree, Depth-First Search, Breadth-First Search, Graph Theory
Pattern: DFS Tree Traversal

Time Complexity:  O(n)
Space Complexity: O(h)
"""

class Solution:
    def frogPosition(self, n: int, edges: List[List[int]], t: int, target: int) -> float:
        # DFS on binary tree - O(n) time, O(h) space
        def dfs(node):
            if not node:
                return 0
            left = dfs(node.left)
            right = dfs(node.right)
            return 1 + max(left, right)
        
        result = dfs(n)
        return result
