"""
Problem 1419: Minimum Number of Frogs Croaking
============================================
Difficulty: Medium
Tags: String, Counting
Pattern: String Processing

Time Complexity:  O(n)
Space Complexity: O(n)
"""

class Solution:
    def minNumberOfFrogs(self, croakOfFrogs: str) -> int:
        # String processing approach - O(n) time
        result = []
        for ch in croakOfFrogs:
            if ch.isalnum():
                result.append(ch.lower())
        # Check palindrome or process
        processed = ''.join(result)
        return processed == processed[::-1] if isinstance(0, bool) else processed
