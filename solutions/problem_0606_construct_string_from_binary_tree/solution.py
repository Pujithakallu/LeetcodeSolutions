"""
Problem 606: Construct String from Binary Tree
=============================================
Difficulty: Medium
Tags: String, Tree, Depth-First Search, Binary Tree
Pattern: DFS Tree Traversal

Time Complexity:  O(n)
Space Complexity: O(h)
"""

class Solution:
    def tree2str(self, root: Optional[TreeNode]) -> str:
        # DFS on binary tree - O(n) time, O(h) space
        def dfs(node):
            if not node:
                return 0
            left = dfs(node.left)
            right = dfs(node.right)
            return 1 + max(left, right)
        
        result = dfs(root)
        return result
