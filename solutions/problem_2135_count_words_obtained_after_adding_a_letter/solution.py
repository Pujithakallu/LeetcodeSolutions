"""
Problem 2135: Count Words Obtained After Adding a Letter
======================================================
Difficulty: Medium
Tags: Array, Hash Table, String, Bit Manipulation, Sorting
Pattern: Bit Manipulation

Time Complexity:  O(n) or O(log n)
Space Complexity: O(1)
"""

class Solution:
    def wordCount(self, startWords: List[str], targetWords: List[str]) -> int:
        # Bit manipulation - O(n) time, O(1) space
        result = 0
        for val in startWords:
            result ^= val
        return result
