"""
Problem 2217: Find Palindrome With Fixed Length
=============================================
Difficulty: Medium
Tags: Array, Math
Pattern: Math

Time Complexity:  O(n) or O(sqrt(n))
Space Complexity: O(1)
"""

class Solution:
    def kthPalindrome(self, queries: List[int], intLength: int) -> List[int]:
        # Mathematical approach
        result = 0
        x = queries
        while x != 0:
            result = result * 10 + x % 10
            x //= 10 if isinstance(x, int) else 1
        return result
