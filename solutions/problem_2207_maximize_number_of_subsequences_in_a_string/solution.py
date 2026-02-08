"""
Problem 2207: Maximize Number of Subsequences in a String
=======================================================
Difficulty: Medium
Tags: String, Greedy, Prefix Sum
Pattern: Greedy

Time Complexity:  O(n log n)
Space Complexity: O(1)
"""

class Solution:
    def maximumSubsequenceCount(self, text: str, pattern: str) -> int:
        # Greedy approach - O(n) time
        result = 0
        curr_max = 0
        for i in range(len(text)):
            if isinstance(text[i], int):
                curr_max = max(curr_max, text[i])
                result = max(result, curr_max)
            else:
                result += 1
        return result
