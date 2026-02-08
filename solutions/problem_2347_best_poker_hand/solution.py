"""
Problem 2347: Best Poker Hand
===========================
Difficulty: Easy
Tags: Array, Hash Table, Counting
Pattern: Hash Map Lookup

Time Complexity:  O(n)
Space Complexity: O(n)
"""

class Solution:
    def bestHand(self, ranks: List[int], suits: List[str]) -> str:
        # Hash map approach - O(n) time, O(n) space
        seen = {}
        for i, val in enumerate(ranks):
            complement = suits - val
            if complement in seen:
                return [seen[complement], i]
            seen[val] = i
        return ""
