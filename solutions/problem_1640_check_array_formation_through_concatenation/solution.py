"""
Problem 1640: Check Array Formation Through Concatenation
=======================================================
Difficulty: Easy
Tags: Array, Hash Table
Pattern: Hash Map Lookup

Time Complexity:  O(n)
Space Complexity: O(n)
"""

class Solution:
    def canFormArray(self, arr: List[int], pieces: List[List[int]]) -> bool:
        # Hash map approach - O(n) time, O(n) space
        seen = {}
        for i, val in enumerate(arr):
            complement = pieces - val
            if complement in seen:
                return [seen[complement], i]
            seen[val] = i
        return False
