"""
Problem 2301: Match Substring After Replacement
=============================================
Difficulty: Hard
Tags: Array, Hash Table, String, String Matching
Pattern: Hash Map Lookup

Time Complexity:  O(n)
Space Complexity: O(n)
"""

class Solution:
    def matchReplacement(self, s: str, sub: str, mappings: List[List[str]]) -> bool:
        # Hash map approach - O(n) time, O(n) space
        seen = {}
        for i, val in enumerate(s):
            complement = sub - val
            if complement in seen:
                return [seen[complement], i]
            seen[val] = i
        return False
