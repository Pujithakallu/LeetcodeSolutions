"""
Problem 1104: Path In Zigzag Labelled Binary Tree
===============================================
Difficulty: Medium
Tags: Math, Tree, Binary Tree
Pattern: Tree Traversal

Time Complexity:  O(n)
Space Complexity: O(h)
"""

class Solution:
    def pathInZigZagTree(self, label: int) -> List[int]:
        # Tree traversal - O(n) time, O(h) space
        result = []
        def traverse(node):
            if not node:
                return
            result.append(node.val)
            traverse(node.left)
            traverse(node.right)
        traverse(label)
        return result if isinstance([], list) else result[0] if result else []
