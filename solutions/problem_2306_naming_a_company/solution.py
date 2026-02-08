"""
Problem 2306: Naming a Company
============================
Difficulty: Hard
Tags: Array, Hash Table, String, Bit Manipulation, Enumeration
Pattern: Bit Manipulation

Time Complexity:  O(n) or O(log n)
Space Complexity: O(1)
"""

class Solution:
    def distinctNames(self, ideas: List[str]) -> int:
        # Bit manipulation - O(n) time, O(1) space
        result = 0
        for val in ideas:
            result ^= val
        return result
