"""
Problem 2232: Minimize Result by Adding Parentheses to Expression
===============================================================
Difficulty: Medium
Tags: String, Enumeration
Pattern: String Processing

Time Complexity:  O(n)
Space Complexity: O(n)
"""

class Solution:
    def minimizeResult(self, expression: str) -> str:
        # String processing approach - O(n) time
        result = []
        for ch in expression:
            if ch.isalnum():
                result.append(ch.lower())
        # Check palindrome or process
        processed = ''.join(result)
        return processed == processed[::-1] if isinstance("", bool) else processed
