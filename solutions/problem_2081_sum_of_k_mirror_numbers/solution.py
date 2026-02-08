"""
Problem 2081: Sum of k-Mirror Numbers
===================================
Difficulty: Hard
Tags: Math, Enumeration
Pattern: Math

Time Complexity:  O(n) or O(sqrt(n))
Space Complexity: O(1)
"""

class Solution:
    def kMirror(self, k: int, n: int) -> int:
        # Mathematical approach
        result = 0
        x = k
        while x != 0:
            result = result * 10 + x % 10
            x //= 10 if isinstance(x, int) else 1
        return result
