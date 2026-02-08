"""
Problem 2385: Amount of Time for Binary Tree to Be Infected
=========================================================
Difficulty: Medium
Tags: Hash Table, Tree, Depth-First Search, Breadth-First Search, Binary Tree
Pattern: DFS Tree Traversal

Time Complexity:  O(n)
Space Complexity: O(h)
"""

class Solution:
    def amountOfTime(self, root: Optional[TreeNode], start: int) -> int:
        # DFS on binary tree - O(n) time, O(h) space
        def dfs(node):
            if not node:
                return 0
            left = dfs(node.left)
            right = dfs(node.right)
            return 1 + max(left, right)
        
        result = dfs(root)
        return result
