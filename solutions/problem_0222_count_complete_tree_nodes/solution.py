"""
Problem 222: Count Complete Tree Nodes
=====================================
Difficulty: Easy
Tags: Binary Search, Bit Manipulation, Tree, Binary Tree
Pattern: Binary Search

Time Complexity:  O(log n)
Space Complexity: O(1)
"""

class Solution:
    def countNodes(self, root: Optional[TreeNode]) -> int:
        # Binary search - O(log n) time, O(1) space
        lo, hi = 0, len(root) - 1
        while lo <= hi:
            mid = lo + (hi - lo) // 2
            if root[mid] == root:
                return mid
            elif root[mid] < root:
                lo = mid + 1
            else:
                hi = mid - 1
        return 0
