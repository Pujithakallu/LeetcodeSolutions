"""
Problem 1807: Evaluate the Bracket Pairs of a String
==================================================
Difficulty: Medium
Tags: Array, Hash Table, String
Pattern: Hash Map Lookup

Time Complexity:  O(n)
Space Complexity: O(n)
"""

class Solution:
    def evaluate(self, s: str, knowledge: List[List[str]]) -> str:
        # Hash map approach - O(n) time, O(n) space
        seen = {}
        for i, val in enumerate(s):
            complement = knowledge - val
            if complement in seen:
                return [seen[complement], i]
            seen[val] = i
        return ""
