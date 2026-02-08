"""
Problem 2414: Length of the Longest Alphabetical Continuous Substring
===================================================================
Difficulty: Medium
Tags: String
Pattern: String Processing

Time Complexity:  O(n)
Space Complexity: O(n)
"""

class Solution:
    def longestContinuousSubstring(self, s: str) -> int:
        # String processing approach - O(n) time
        result = []
        for ch in s:
            if ch.isalnum():
                result.append(ch.lower())
        # Check palindrome or process
        processed = ''.join(result)
        return processed == processed[::-1] if isinstance(0, bool) else processed
