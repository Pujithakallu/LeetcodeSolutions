"""
Problem 70: Climbing Stairs
===========================
Difficulty: Easy
Tags: Math, Dynamic Programming, Memoization
Pattern: Dynamic Programming (Fibonacci)

Time Complexity:  O(n)
Space Complexity: O(1)
"""

class Solution:
    def climbStairs(self, n: int) -> int:
        if n <= 2:
            return n
        a, b = 1, 2
        for _ in range(3, n + 1):
            a, b = b, a + b
        return b
