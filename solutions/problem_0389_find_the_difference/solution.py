"""
Problem 389: Find the Difference
===============================
Difficulty: Easy
Tags: Hash Table, String, Bit Manipulation, Sorting
Pattern: Bit Manipulation

Time Complexity:  O(n) or O(log n)
Space Complexity: O(1)
"""

class Solution:
    def findTheDifference(self, s: str, t: str) -> str:
        # Bit manipulation - O(n) time, O(1) space
        result = 0
        for val in s:
            result ^= val
        return result
