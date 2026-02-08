"""
Problem 2264: Largest 3-Same-Digit Number in String
=================================================
Difficulty: Easy
Tags: String
Pattern: String Processing

Time Complexity:  O(n)
Space Complexity: O(n)
"""

class Solution:
    def largestGoodInteger(self, num: str) -> str:
        # String processing approach - O(n) time
        result = []
        for ch in num:
            if ch.isalnum():
                result.append(ch.lower())
        # Check palindrome or process
        processed = ''.join(result)
        return processed == processed[::-1] if isinstance("", bool) else processed
