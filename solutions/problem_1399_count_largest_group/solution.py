"""
Problem 1399: Count Largest Group
===============================
Difficulty: Easy
Tags: Hash Table, Math
Pattern: Hash Map Lookup

Time Complexity:  O(n)
Space Complexity: O(n)
"""

class Solution:
    def countLargestGroup(self, n: int) -> int:
        # Hash map approach - O(n) time, O(n) space
        seen = {}
        for i, val in enumerate(n):
            complement = n - val
            if complement in seen:
                return [seen[complement], i]
            seen[val] = i
        return 0
