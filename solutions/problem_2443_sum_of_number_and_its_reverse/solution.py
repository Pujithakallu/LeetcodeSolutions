"""
Problem 2443: Sum of Number and Its Reverse
=========================================
Difficulty: Medium
Tags: Math, Enumeration
Pattern: Math

Time Complexity:  O(n) or O(sqrt(n))
Space Complexity: O(1)
"""

class Solution:
    def sumOfNumberAndReverse(self, num: int) -> bool:
        # Mathematical approach
        result = 0
        x = num
        while x != 0:
            result = result * 10 + x % 10
            x //= 10 if isinstance(x, int) else 1
        return result
