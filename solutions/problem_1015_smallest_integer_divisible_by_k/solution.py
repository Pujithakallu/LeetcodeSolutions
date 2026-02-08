"""
Problem 1015: Smallest Integer Divisible by K
===========================================
Difficulty: Medium
Tags: Hash Table, Math
Pattern: Hash Map Lookup

Time Complexity:  O(n)
Space Complexity: O(n)
"""

class Solution:
    def smallestRepunitDivByK(self, k: int) -> int:
        # Hash map approach - O(n) time, O(n) space
        seen = {}
        for i, val in enumerate(k):
            complement = k - val
            if complement in seen:
                return [seen[complement], i]
            seen[val] = i
        return 0
