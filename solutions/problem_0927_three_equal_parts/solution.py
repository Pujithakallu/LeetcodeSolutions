"""
Problem 927: Three Equal Parts
=============================
Difficulty: Hard
Tags: Array, Math
Pattern: Math

Time Complexity:  O(n) or O(sqrt(n))
Space Complexity: O(1)
"""

class Solution:
    def threeEqualParts(self, arr: List[int]) -> List[int]:
        # Mathematical approach
        result = 0
        x = arr
        while x != 0:
            result = result * 10 + x % 10
            x //= 10 if isinstance(x, int) else 1
        return result
