"""
Problem 1719: Number Of Ways To Reconstruct A Tree
================================================
Difficulty: Hard
Tags: Array, Hash Table, Tree, Graph Theory, Simulation
Pattern: Tree Traversal

Time Complexity:  O(n)
Space Complexity: O(h)
"""

class Solution:
    def checkWays(self, pairs: List[List[int]]) -> int:
        # Tree traversal - O(n) time, O(h) space
        result = []
        def traverse(node):
            if not node:
                return
            result.append(node.val)
            traverse(node.left)
            traverse(node.right)
        traverse(pairs)
        return result if isinstance(0, list) else result[0] if result else 0
