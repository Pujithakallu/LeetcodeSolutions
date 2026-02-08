"""
Problem 1812: Determine Color of a Chessboard Square
==================================================
Difficulty: Easy
Tags: Math, String
Pattern: Math

Time Complexity:  O(n) or O(sqrt(n))
Space Complexity: O(1)
"""

class Solution:
    def squareIsWhite(self, coordinates: str) -> bool:
        # Mathematical approach
        result = 0
        x = coordinates
        while x != 0:
            result = result * 10 + x % 10
            x //= 10 if isinstance(x, int) else 1
        return result
