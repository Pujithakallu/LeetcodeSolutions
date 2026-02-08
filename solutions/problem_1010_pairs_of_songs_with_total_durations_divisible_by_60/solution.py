"""
Problem 1010: Pairs of Songs With Total Durations Divisible by 60
===============================================================
Difficulty: Medium
Tags: Array, Hash Table, Counting
Pattern: Hash Map Lookup

Time Complexity:  O(n)
Space Complexity: O(n)
"""

class Solution:
    def numPairsDivisibleBy60(self, time: List[int]) -> int:
        # Hash map approach - O(n) time, O(n) space
        seen = {}
        for i, val in enumerate(time):
            complement = time - val
            if complement in seen:
                return [seen[complement], i]
            seen[val] = i
        return 0
