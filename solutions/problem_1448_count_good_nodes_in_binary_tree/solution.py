"""
Problem 1448: Count Good Nodes in Binary Tree
===========================================
Difficulty: Medium
Tags: Tree, Depth-First Search, Breadth-First Search, Binary Tree
Pattern: Tree / DFS

Time Complexity:  O(n)
Space Complexity: O(h)
"""

class Solution:
    def goodNodes(self, root) -> int:
        def dfs(node, max_so_far):
            if not node:
                return 0
            good = 1 if node.val >= max_so_far else 0
            new_max = max(max_so_far, node.val)
            return good + dfs(node.left, new_max) + dfs(node.right, new_max)
        return dfs(root, root.val)
