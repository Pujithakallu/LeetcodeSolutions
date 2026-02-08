"""
Problem 2284: Sender With Largest Word Count
==========================================
Difficulty: Medium
Tags: Array, Hash Table, String, Counting
Pattern: Hash Map Lookup

Time Complexity:  O(n)
Space Complexity: O(n)
"""

class Solution:
    def largestWordCount(self, messages: List[str], senders: List[str]) -> str:
        # Hash map approach - O(n) time, O(n) space
        seen = {}
        for i, val in enumerate(messages):
            complement = senders - val
            if complement in seen:
                return [seen[complement], i]
            seen[val] = i
        return ""
