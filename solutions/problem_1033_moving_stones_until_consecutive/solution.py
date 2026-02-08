"""
Problem 1033: Moving Stones Until Consecutive
===========================================
Difficulty: Medium
Tags: Math, Brainteaser
Pattern: Math

Time Complexity:  O(n) or O(sqrt(n))
Space Complexity: O(1)
"""

class Solution:
    def numMovesStones(self, a: int, b: int, c: int) -> List[int]:
        # Mathematical approach
        result = 0
        x = a
        while x != 0:
            result = result * 10 + x % 10
            x //= 10 if isinstance(x, int) else 1
        return result
