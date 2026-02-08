"""
Problem 806: Number of Lines To Write String
===========================================
Difficulty: Easy
Tags: Array, String
Pattern: String Processing

Time Complexity:  O(n)
Space Complexity: O(n)
"""

class Solution:
    def numberOfLines(self, widths: List[int], s: str) -> List[int]:
        # String processing approach - O(n) time
        result = []
        for ch in widths:
            if ch.isalnum():
                result.append(ch.lower())
        # Check palindrome or process
        processed = ''.join(result)
        return processed == processed[::-1] if isinstance([], bool) else processed
