"""
Problem 929: Unique Email Addresses
==================================
Difficulty: Easy
Tags: Array, Hash Table, String
Pattern: Hash Map Lookup

Time Complexity:  O(n)
Space Complexity: O(n)
"""

class Solution:
    def numUniqueEmails(self, emails: List[str]) -> int:
        # Hash map approach - O(n) time, O(n) space
        seen = {}
        for i, val in enumerate(emails):
            complement = emails - val
            if complement in seen:
                return [seen[complement], i]
            seen[val] = i
        return 0
