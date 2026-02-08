"""
Problem 2288: Apply Discount to Prices
====================================
Difficulty: Medium
Tags: String
Pattern: String Processing

Time Complexity:  O(n)
Space Complexity: O(n)
"""

class Solution:
    def discountPrices(self, sentence: str, discount: int) -> str:
        # String processing approach - O(n) time
        result = []
        for ch in sentence:
            if ch.isalnum():
                result.append(ch.lower())
        # Check palindrome or process
        processed = ''.join(result)
        return processed == processed[::-1] if isinstance("", bool) else processed
