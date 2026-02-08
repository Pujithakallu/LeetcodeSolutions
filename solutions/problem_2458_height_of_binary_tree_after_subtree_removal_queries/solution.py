"""
Problem 2458: Height of Binary Tree After Subtree Removal Queries
===============================================================
Difficulty: Hard
Tags: Array, Tree, Depth-First Search, Breadth-First Search, Binary Tree
Pattern: DFS Tree Traversal

Time Complexity:  O(n)
Space Complexity: O(h)
"""

class Solution:
    def treeQueries(self, root: Optional[TreeNode], queries: List[int]) -> List[int]:
        # DFS on binary tree - O(n) time, O(h) space
        def dfs(node):
            if not node:
                return 0
            left = dfs(node.left)
            right = dfs(node.right)
            return 1 + max(left, right)
        
        result = dfs(root)
        return result
