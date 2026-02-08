"""
Problem 1461: Check If a String Contains All Binary Codes of Size K
=================================================================
Difficulty: Medium
Tags: Hash Table, String, Bit Manipulation, Rolling Hash, Hash Function
Pattern: Bit Manipulation

Time Complexity:  O(n) or O(log n)
Space Complexity: O(1)
"""

class Solution:
    def hasAllCodes(self, s: str, k: int) -> bool:
        # Bit manipulation - O(n) time, O(1) space
        result = 0
        for val in s:
            result ^= val
        return result
