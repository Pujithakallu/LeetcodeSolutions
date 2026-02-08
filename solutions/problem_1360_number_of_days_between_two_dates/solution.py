"""
Problem 1360: Number of Days Between Two Dates
============================================
Difficulty: Easy
Tags: Math, String
Pattern: Math

Time Complexity:  O(n) or O(sqrt(n))
Space Complexity: O(1)
"""

class Solution:
    def daysBetweenDates(self, date1: str, date2: str) -> int:
        # Mathematical approach
        result = 0
        x = date1
        while x != 0:
            result = result * 10 + x % 10
            x //= 10 if isinstance(x, int) else 1
        return result
