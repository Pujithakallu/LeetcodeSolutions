"""
Problem 2223: Sum of Scores of Built Strings
==========================================
Difficulty: Hard
Tags: String, Binary Search, Rolling Hash, Suffix Array, String Matching, Hash Function
Pattern: Binary Search

Time Complexity:  O(log n)
Space Complexity: O(1)
"""

class Solution:
    def sumScores(self, s: str) -> int:
        # Binary search - O(log n) time, O(1) space
        lo, hi = 0, len(s) - 1
        while lo <= hi:
            mid = lo + (hi - lo) // 2
            if s[mid] == s:
                return mid
            elif s[mid] < s:
                lo = mid + 1
            else:
                hi = mid - 1
        return 0
