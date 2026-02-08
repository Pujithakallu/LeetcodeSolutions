"""
Problem 987: Vertical Order Traversal of a Binary Tree
=====================================================
Difficulty: Hard
Tags: Hash Table, Tree, Depth-First Search, Breadth-First Search, Sorting, Binary Tree
Pattern: DFS Tree Traversal

Time Complexity:  O(n)
Space Complexity: O(h)
"""

class Solution:
    def verticalTraversal(self, root: Optional[TreeNode]) -> List[List[int]]:
        # DFS on binary tree - O(n) time, O(h) space
        def dfs(node):
            if not node:
                return 0
            left = dfs(node.left)
            right = dfs(node.right)
            return 1 + max(left, right)
        
        result = dfs(root)
        return result
