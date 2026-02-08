"""
Problem 2014: Longest Subsequence Repeated k Times
================================================
Difficulty: Hard
Tags: Hash Table, Two Pointers, String, Backtracking, Counting, Enumeration
Pattern: Backtracking

Time Complexity:  O(k^n) or O(n!)
Space Complexity: O(n)
"""

class Solution:
    def longestSubsequenceRepeatedK(self, s: str, k: int) -> str:
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
