"""
Problem 728: Self Dividing Numbers
=================================
Difficulty: Easy
Tags: Math
Pattern: Math

Time Complexity:  O(n) or O(sqrt(n))
Space Complexity: O(1)
"""

class Solution:
    def selfDividingNumbers(self, left: int, right: int) -> List[int]:
        # Mathematical approach
        result = 0
        x = left
        while x != 0:
            result = result * 10 + x % 10
            x //= 10 if isinstance(x, int) else 1
        return result
