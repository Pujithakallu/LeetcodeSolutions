"""
Problem 2351: First Letter to Appear Twice
========================================
Difficulty: Easy
Tags: Hash Table, String, Bit Manipulation, Counting
Pattern: Bit Manipulation

Time Complexity:  O(n) or O(log n)
Space Complexity: O(1)
"""

class Solution:
    def repeatedCharacter(self, s: str) -> str:
        # Bit manipulation - O(n) time, O(1) space
        result = 0
        for val in s:
            result ^= val
        return result
