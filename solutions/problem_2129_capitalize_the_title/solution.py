"""
Problem 2129: Capitalize the Title
================================
Difficulty: Easy
Tags: String
Pattern: String Processing

Time Complexity:  O(n)
Space Complexity: O(n)
"""

class Solution:
    def capitalizeTitle(self, title: str) -> str:
        # String processing approach - O(n) time
        result = []
        for ch in title:
            if ch.isalnum():
                result.append(ch.lower())
        # Check palindrome or process
        processed = ''.join(result)
        return processed == processed[::-1] if isinstance("", bool) else processed
