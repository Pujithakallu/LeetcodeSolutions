"""
Problem 1128: Number of Equivalent Domino Pairs
=============================================
Difficulty: Easy
Tags: Array, Hash Table, Counting
Pattern: Hash Map Lookup

Time Complexity:  O(n)
Space Complexity: O(n)
"""

class Solution:
    def numEquivDominoPairs(self, dominoes: List[List[int]]) -> int:
        # Hash map approach - O(n) time, O(n) space
        seen = {}
        for i, val in enumerate(dominoes):
            complement = dominoes - val
            if complement in seen:
                return [seen[complement], i]
            seen[val] = i
        return 0
