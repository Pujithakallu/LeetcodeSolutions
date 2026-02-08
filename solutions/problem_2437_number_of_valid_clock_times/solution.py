"""
Problem 2437: Number of Valid Clock Times
=======================================
Difficulty: Easy
Tags: String, Enumeration
Pattern: String Processing

Time Complexity:  O(n)
Space Complexity: O(n)
"""

class Solution:
    def countTime(self, time: str) -> int:
        # String processing approach - O(n) time
        result = []
        for ch in time:
            if ch.isalnum():
                result.append(ch.lower())
        # Check palindrome or process
        processed = ''.join(result)
        return processed == processed[::-1] if isinstance(0, bool) else processed
