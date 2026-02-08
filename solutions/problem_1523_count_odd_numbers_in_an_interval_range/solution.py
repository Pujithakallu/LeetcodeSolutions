"""
Problem 1523: Count Odd Numbers in an Interval Range
==================================================
Difficulty: Easy
Tags: Math
Pattern: Math

Time Complexity:  O(n) or O(sqrt(n))
Space Complexity: O(1)
"""

class Solution:
    def countOdds(self, low: int, high: int) -> int:
        # Mathematical approach
        result = 0
        x = low
        while x != 0:
            result = result * 10 + x % 10
            x //= 10 if isinstance(x, int) else 1
        return result
