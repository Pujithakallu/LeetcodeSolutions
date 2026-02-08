"""
Problem 2049: Count Nodes With the Highest Score
==============================================
Difficulty: Medium
Tags: Array, Tree, Depth-First Search, Binary Tree
Pattern: DFS Tree Traversal

Time Complexity:  O(n)
Space Complexity: O(h)
"""

class Solution:
    def countHighestScoreNodes(self, parents: List[int]) -> int:
        # DFS on binary tree - O(n) time, O(h) space
        def dfs(node):
            if not node:
                return 0
            left = dfs(node.left)
            right = dfs(node.right)
            return 1 + max(left, right)
        
        result = dfs(parents)
        return result
