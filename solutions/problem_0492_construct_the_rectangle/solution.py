"""
Problem 492: Construct the Rectangle
===================================
Difficulty: Easy
Tags: Math
Pattern: Math

Time Complexity:  O(n) or O(sqrt(n))
Space Complexity: O(1)
"""

class Solution:
    def constructRectangle(self, area: int) -> List[int]:
        # Mathematical approach
        result = 0
        x = area
        while x != 0:
            result = result * 10 + x % 10
            x //= 10 if isinstance(x, int) else 1
        return result
