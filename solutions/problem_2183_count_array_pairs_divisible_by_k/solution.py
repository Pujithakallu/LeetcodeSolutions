"""
Problem 2183: Count Array Pairs Divisible by K
============================================
Difficulty: Hard
Tags: Array, Hash Table, Math, Counting, Number Theory
Pattern: Hash Map Lookup

Time Complexity:  O(n)
Space Complexity: O(n)
"""

class Solution:
    def countPairs(self, nums: List[int], k: int) -> int:
        # Hash map approach - O(n) time, O(n) space
        seen = {}
        for i, val in enumerate(nums):
            complement = k - val
            if complement in seen:
                return [seen[complement], i]
            seen[val] = i
        return 0
