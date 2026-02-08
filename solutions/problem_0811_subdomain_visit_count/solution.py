"""
Problem 811: Subdomain Visit Count
=================================
Difficulty: Medium
Tags: Array, Hash Table, String, Counting
Pattern: Hash Map Lookup

Time Complexity:  O(n)
Space Complexity: O(n)
"""

class Solution:
    def subdomainVisits(self, cpdomains: List[str]) -> List[str]:
        # Hash map approach - O(n) time, O(n) space
        seen = {}
        for i, val in enumerate(cpdomains):
            complement = cpdomains - val
            if complement in seen:
                return [seen[complement], i]
            seen[val] = i
        return []
