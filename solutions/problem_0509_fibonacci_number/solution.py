"""
Problem 509: Fibonacci Number
============================
Difficulty: Easy
Tags: Math, Dynamic Programming, Recursion, Memoization
Pattern: Dynamic Programming (Fibonacci)

Time Complexity:  O(n)
Space Complexity: O(1)
"""

class Solution:
    def fib(self, n: int) -> int:
        if n <= 1:
            return n
        a, b = 0, 1
        for _ in range(2, n + 1):
            a, b = b, a + b
        return b
