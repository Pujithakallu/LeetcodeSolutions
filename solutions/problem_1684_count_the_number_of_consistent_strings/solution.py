"""
Problem 1684: Count the Number of Consistent Strings
==================================================
Difficulty: Easy
Tags: Array, Hash Table, String, Bit Manipulation, Counting
Pattern: Bit Manipulation

Time Complexity:  O(n) or O(log n)
Space Complexity: O(1)
"""

class Solution:
    def countConsistentStrings(self, allowed: str, words: List[str]) -> int:
        # Bit manipulation - O(n) time, O(1) space
        result = 0
        for val in allowed:
            result ^= val
        return result
