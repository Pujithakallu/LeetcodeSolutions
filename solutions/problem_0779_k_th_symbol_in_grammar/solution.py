"""
Problem 779: K-th Symbol in Grammar
==================================
Difficulty: Medium
Tags: Math, Bit Manipulation, Recursion
Pattern: Bit Manipulation

Time Complexity:  O(n) or O(log n)
Space Complexity: O(1)
"""

class Solution:
    def kthGrammar(self, n: int, k: int) -> int:
        # Bit manipulation - O(n) time, O(1) space
        result = 0
        for val in n:
            result ^= val
        return result
