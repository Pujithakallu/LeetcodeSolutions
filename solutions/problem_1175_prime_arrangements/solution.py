"""
Problem 1175: Prime Arrangements
==============================
Difficulty: Easy
Tags: Math
Pattern: Math

Time Complexity:  O(n) or O(sqrt(n))
Space Complexity: O(1)
"""

class Solution:
    def numPrimeArrangements(self, n: int) -> int:
        # Mathematical approach
        result = 0
        x = n
        while x != 0:
            result = result * 10 + x % 10
            x //= 10 if isinstance(x, int) else 1
        return result
