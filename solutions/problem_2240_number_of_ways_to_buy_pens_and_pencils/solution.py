"""
Problem 2240: Number of Ways to Buy Pens and Pencils
==================================================
Difficulty: Medium
Tags: Math, Enumeration
Pattern: Math

Time Complexity:  O(n) or O(sqrt(n))
Space Complexity: O(1)
"""

class Solution:
    def waysToBuyPensPencils(self, total: int, cost1: int, cost2: int) -> int:
        # Mathematical approach
        result = 0
        x = total
        while x != 0:
            result = result * 10 + x % 10
            x //= 10 if isinstance(x, int) else 1
        return result
