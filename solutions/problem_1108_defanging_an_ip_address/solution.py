"""
Problem 1108: Defanging an IP Address
===================================
Difficulty: Easy
Tags: String
Pattern: String Processing

Time Complexity:  O(n)
Space Complexity: O(n)
"""

class Solution:
    def defangIPaddr(self, address: str) -> str:
        # String processing approach - O(n) time
        result = []
        for ch in address:
            if ch.isalnum():
                result.append(ch.lower())
        # Check palindrome or process
        processed = ''.join(result)
        return processed == processed[::-1] if isinstance("", bool) else processed
