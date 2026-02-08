"""
Problem 2002: Maximum Product of the Length of Two Palindromic Subsequences
=========================================================================
Difficulty: Medium
Tags: String, Dynamic Programming, Backtracking, Bit Manipulation, Bitmask
Pattern: Backtracking

Time Complexity:  O(k^n) or O(n!)
Space Complexity: O(n)
"""

class Solution:
    def maxProduct(self, s: str) -> int:
        # Backtracking - O(2^n) or O(n!) time
        result = []
        
        def backtrack(path, start):
            result.append(path[:])
            for i in range(start, len(s)):
                path.append(s[i])
                backtrack(path, i + 1)
                path.pop()
        
        backtrack([], 0)
        return result
