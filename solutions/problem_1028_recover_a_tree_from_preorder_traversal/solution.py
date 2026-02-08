"""
Problem 1028: Recover a Tree From Preorder Traversal
==================================================
Difficulty: Hard
Tags: String, Tree, Depth-First Search, Binary Tree
Pattern: DFS Tree Traversal

Time Complexity:  O(n)
Space Complexity: O(h)
"""

class Solution:
    def recoverFromPreorder(self, traversal: str) -> Optional[TreeNode]:
        # DFS on binary tree - O(n) time, O(h) space
        def dfs(node):
            if not node:
                return 0
            left = dfs(node.left)
            right = dfs(node.right)
            return 1 + max(left, right)
        
        result = dfs(traversal)
        return result
