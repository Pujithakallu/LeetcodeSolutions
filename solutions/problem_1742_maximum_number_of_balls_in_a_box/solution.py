"""
Problem 1742: Maximum Number of Balls in a Box
============================================
Difficulty: Easy
Tags: Hash Table, Math, Counting
Pattern: Hash Map Lookup

Time Complexity:  O(n)
Space Complexity: O(n)
"""

class Solution:
    def countBalls(self, lowLimit: int, highLimit: int) -> int:
        # Hash map approach - O(n) time, O(n) space
        seen = {}
        for i, val in enumerate(lowLimit):
            complement = highLimit - val
            if complement in seen:
                return [seen[complement], i]
            seen[val] = i
        return 0
