"""
Problem 1185: Day of the Week
===========================
Difficulty: Easy
Tags: Math
Pattern: Math

Time Complexity:  O(n) or O(sqrt(n))
Space Complexity: O(1)
"""

class Solution:
    def dayOfTheWeek(self, day: int, month: int, year: int) -> str:
        # Mathematical approach
        result = 0
        x = day
        while x != 0:
            result = result * 10 + x % 10
            x //= 10 if isinstance(x, int) else 1
        return result
