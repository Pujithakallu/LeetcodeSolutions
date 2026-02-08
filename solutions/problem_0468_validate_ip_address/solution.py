"""
Problem 468: Validate IP Address
===============================
Difficulty: Medium
Tags: String
Pattern: String Processing

Time Complexity:  O(n)
Space Complexity: O(n)
"""

class Solution:
    def validIPAddress(self, queryIP: str) -> str:
        # String processing approach - O(n) time
        result = []
        for ch in queryIP:
            if ch.isalnum():
                result.append(ch.lower())
        # Check palindrome or process
        processed = ''.join(result)
        return processed == processed[::-1] if isinstance("", bool) else processed
