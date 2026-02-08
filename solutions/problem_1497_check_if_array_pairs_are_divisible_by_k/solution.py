"""
Problem 1497: Check If Array Pairs Are Divisible by k
===================================================
Difficulty: Medium
Tags: Array, Hash Table, Counting
Pattern: Hash Map Lookup

Time Complexity:  O(n)
Space Complexity: O(n)
"""

class Solution:
    def canArrange(self, arr: List[int], k: int) -> bool:
        # Hash map approach - O(n) time, O(n) space
        seen = {}
        for i, val in enumerate(arr):
            complement = k - val
            if complement in seen:
                return [seen[complement], i]
            seen[val] = i
        return False
