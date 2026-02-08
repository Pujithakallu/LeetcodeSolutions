"""
Problem 556: Next Greater Element III
====================================
Difficulty: Medium
Tags: Math, Two Pointers, String
Pattern: Math / Next Permutation

Time Complexity:  O(n)
Space Complexity: O(n)
"""

class Solution:
    def nextGreaterElement(self, n: int) -> int:
        digits = list(str(n))
        i = len(digits) - 2
        while i >= 0 and digits[i] >= digits[i + 1]:
            i -= 1
        if i < 0:
            return -1
        j = len(digits) - 1
        while digits[j] <= digits[i]:
            j -= 1
        digits[i], digits[j] = digits[j], digits[i]
        digits[i + 1:] = reversed(digits[i + 1:])
        result = int(''.join(digits))
        return result if result <= 2**31 - 1 else -1
