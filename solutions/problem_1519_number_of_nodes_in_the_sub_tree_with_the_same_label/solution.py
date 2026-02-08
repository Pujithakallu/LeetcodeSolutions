"""
Problem 1519: Number of Nodes in the Sub-Tree With the Same Label
===============================================================
Difficulty: Medium
Tags: Hash Table, Tree, Depth-First Search, Breadth-First Search, Counting
Pattern: DFS Tree Traversal

Time Complexity:  O(n)
Space Complexity: O(h)
"""

class Solution:
    def countSubTrees(self, n: int, edges: List[List[int]], labels: str) -> List[int]:
        # DFS on binary tree - O(n) time, O(h) space
        def dfs(node):
            if not node:
                return 0
            left = dfs(node.left)
            right = dfs(node.right)
            return 1 + max(left, right)
        
        result = dfs(n)
        return result
