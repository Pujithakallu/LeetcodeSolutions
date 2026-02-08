"""
Problem 2469: Convert the Temperature
===================================
Difficulty: Easy
Tags: Math
Pattern: Math

Time Complexity:  O(n) or O(sqrt(n))
Space Complexity: O(1)
"""

class Solution:
    def convertTemperature(self, celsius: float) -> List[float]:
        # Mathematical approach
        result = 0
        x = celsius
        while x != 0:
            result = result * 10 + x % 10
            x //= 10 if isinstance(x, int) else 1
        return result
