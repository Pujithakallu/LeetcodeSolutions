"""
Problem 318: Maximum Product of Word Lengths
===========================================
Difficulty: Medium
Tags: Array, String, Bit Manipulation
Pattern: Bit Manipulation

Time Complexity:  O(n) or O(log n)
Space Complexity: O(1)
"""

class Solution:
    def maxProduct(self, words: List[str]) -> int:
        # Bit manipulation - O(n) time, O(1) space
        result = 0
        for val in words:
            result ^= val
        return result
