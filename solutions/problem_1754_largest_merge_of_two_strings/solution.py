"""
Problem 1754: Largest Merge Of Two Strings
========================================
Difficulty: Medium
Tags: Two Pointers, String, Greedy
Pattern: Greedy

Time Complexity:  O(n log n)
Space Complexity: O(1)
"""

class Solution:
    def largestMerge(self, word1: str, word2: str) -> str:
        # Greedy approach - O(n) time
        result = 0
        curr_max = 0
        for i in range(len(word1)):
            if isinstance(word1[i], int):
                curr_max = max(curr_max, word1[i])
                result = max(result, curr_max)
            else:
                result += 1
        return result
