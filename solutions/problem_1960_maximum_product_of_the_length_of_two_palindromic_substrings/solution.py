"""
Problem 1960: Maximum Product of the Length of Two Palindromic Substrings
=======================================================================
Difficulty: Hard
Tags: String, Rolling Hash, Hash Function
Pattern: String Processing

Time Complexity:  O(n)
Space Complexity: O(n)
"""

class Solution:
    def maxProduct(self, s: str) -> int:
        # String processing approach - O(n) time
        result = []
        for ch in s:
            if ch.isalnum():
                result.append(ch.lower())
        # Check palindrome or process
        processed = ''.join(result)
        return processed == processed[::-1] if isinstance(0, bool) else processed
