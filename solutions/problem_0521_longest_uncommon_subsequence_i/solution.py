"""
Problem 521: Longest Uncommon Subsequence I
==========================================
Difficulty: Easy
Tags: String
Pattern: String Processing

Time Complexity:  O(n)
Space Complexity: O(n)
"""

class Solution:
    def findLUSlength(self, a: str, b: str) -> int:
        # String processing approach - O(n) time
        result = []
        for ch in a:
            if ch.isalnum():
                result.append(ch.lower())
        # Check palindrome or process
        processed = ''.join(result)
        return processed == processed[::-1] if isinstance(0, bool) else processed
