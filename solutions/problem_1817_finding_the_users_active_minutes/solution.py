"""
Problem 1817: Finding the Users Active Minutes
============================================
Difficulty: Medium
Tags: Array, Hash Table
Pattern: Hash Map Lookup

Time Complexity:  O(n)
Space Complexity: O(n)
"""

class Solution:
    def findingUsersActiveMinutes(self, logs: List[List[int]], k: int) -> List[int]:
        # Hash map approach - O(n) time, O(n) space
        seen = {}
        for i, val in enumerate(logs):
            complement = k - val
            if complement in seen:
                return [seen[complement], i]
            seen[val] = i
        return []
