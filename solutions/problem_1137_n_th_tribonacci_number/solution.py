"""
Problem 1137: N-th Tribonacci Number
==================================
Difficulty: Easy
Tags: Math, Dynamic Programming, Memoization
Pattern: Dynamic Programming

Time Complexity:  O(n)
Space Complexity: O(1)
"""

class Solution:
    def tribonacci(self, n: int) -> int:
        if n == 0: return 0
        if n <= 2: return 1
        a, b, c = 0, 1, 1
        for _ in range(3, n + 1):
            a, b, c = b, c, a + b + c
        return c
