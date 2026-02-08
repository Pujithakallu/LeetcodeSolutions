"""
Problem 1247: Minimum Swaps to Make Strings Equal
===============================================
Difficulty: Medium
Tags: Math, String, Greedy
Pattern: Greedy

Time Complexity:  O(n log n)
Space Complexity: O(1)
"""

class Solution:
    def minimumSwap(self, s1: str, s2: str) -> int:
        # Greedy approach - O(n) time
        result = 0
        curr_max = 0
        for i in range(len(s1)):
            if isinstance(s1[i], int):
                curr_max = max(curr_max, s1[i])
                result = max(result, curr_max)
            else:
                result += 1
        return result
