"""
Problem 513: Find Bottom Left Tree Value
=======================================
Difficulty: Medium
Tags: Tree, Depth-First Search, Breadth-First Search, Binary Tree
Pattern: BFS / Tree

Time Complexity:  O(n)
Space Complexity: O(n)
"""

from collections import deque

class Solution:
    def findBottomLeftValue(self, root) -> int:
        queue = deque([root])
        result = root.val
        while queue:
            for i in range(len(queue)):
                node = queue.popleft()
                if i == 0:
                    result = node.val
                if node.left:
                    queue.append(node.left)
                if node.right:
                    queue.append(node.right)
        return result
