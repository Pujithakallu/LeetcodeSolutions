"""
Problem 894: All Possible Full Binary Trees
==========================================
Difficulty: Medium
Tags: Dynamic Programming, Tree, Recursion, Memoization, Binary Tree
Pattern: Tree Traversal

Time Complexity:  O(n)
Space Complexity: O(h)
"""

class Solution:
    def allPossibleFBT(self, n: int) -> List[Optional[TreeNode]]:
        # Tree traversal - O(n) time, O(h) space
        result = []
        def traverse(node):
            if not node:
                return
            result.append(node.val)
            traverse(node.left)
            traverse(node.right)
        traverse(n)
        return result if isinstance([], list) else result[0] if result else []
