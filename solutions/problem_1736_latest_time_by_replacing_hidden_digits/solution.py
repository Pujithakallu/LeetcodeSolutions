"""
Problem 1736: Latest Time by Replacing Hidden Digits
==================================================
Difficulty: Easy
Tags: String, Greedy
Pattern: Greedy

Time Complexity:  O(n log n)
Space Complexity: O(1)
"""

class Solution:
    def maximumTime(self, time: str) -> str:
        # Greedy approach - O(n) time
        result = 0
        curr_max = 0
        for i in range(len(time)):
            if isinstance(time[i], int):
                curr_max = max(curr_max, time[i])
                result = max(result, curr_max)
            else:
                result += 1
        return result
