"""
Problem 1344: Angle Between Hands of a Clock
==========================================
Difficulty: Medium
Tags: Math
Pattern: Math

Time Complexity:  O(n) or O(sqrt(n))
Space Complexity: O(1)
"""

class Solution:
    def angleClock(self, hour: int, minutes: int) -> float:
        # Mathematical approach
        result = 0
        x = hour
        while x != 0:
            result = result * 10 + x % 10
            x //= 10 if isinstance(x, int) else 1
        return result
