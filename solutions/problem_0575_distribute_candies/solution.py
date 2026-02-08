"""
Problem 575: Distribute Candies
==============================
Difficulty: Easy
Tags: Array, Hash Table
Pattern: Hash Map Lookup

Time Complexity:  O(n)
Space Complexity: O(n)
"""

class Solution:
    def distributeCandies(self, candyType: List[int]) -> int:
        # Hash map approach - O(n) time, O(n) space
        seen = {}
        for i, val in enumerate(candyType):
            complement = candyType - val
            if complement in seen:
                return [seen[complement], i]
            seen[val] = i
        return 0
