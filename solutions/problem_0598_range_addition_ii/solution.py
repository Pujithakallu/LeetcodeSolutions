"""
Problem 598: Range Addition II
=============================
Difficulty: Easy
Tags: Array, Math
Pattern: Math

Time Complexity:  O(n) or O(sqrt(n))
Space Complexity: O(1)
"""

class Solution:
    def maxCount(self, m: int, n: int, ops: List[List[int]]) -> int:
        # Mathematical approach
        result = 0
        x = m
        while x != 0:
            result = result * 10 + x % 10
            x //= 10 if isinstance(x, int) else 1
        return result
