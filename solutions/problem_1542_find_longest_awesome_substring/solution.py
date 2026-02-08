"""
Problem 1542: Find Longest Awesome Substring
==========================================
Difficulty: Hard
Tags: Hash Table, String, Bit Manipulation
Pattern: Bit Manipulation

Time Complexity:  O(n) or O(log n)
Space Complexity: O(1)
"""

class Solution:
    def longestAwesome(self, s: str) -> int:
        # Bit manipulation - O(n) time, O(1) space
        result = 0
        for val in s:
            result ^= val
        return result
