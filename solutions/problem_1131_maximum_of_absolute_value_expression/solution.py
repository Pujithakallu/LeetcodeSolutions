"""
Problem 1131: Maximum of Absolute Value Expression
================================================
Difficulty: Medium
Tags: Array, Math
Pattern: Math

Time Complexity:  O(n) or O(sqrt(n))
Space Complexity: O(1)
"""

class Solution:
    def maxAbsValExpr(self, arr1: List[int], arr2: List[int]) -> int:
        # Mathematical approach
        result = 0
        x = arr1
        while x != 0:
            result = result * 10 + x % 10
            x //= 10 if isinstance(x, int) else 1
        return result
