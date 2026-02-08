"""
Problem 2224: Minimum Number of Operations to Convert Time
========================================================
Difficulty: Easy
Tags: String, Greedy
Pattern: Greedy

Time Complexity:  O(n log n)
Space Complexity: O(1)
"""

class Solution:
    def convertTime(self, current: str, correct: str) -> int:
        # Greedy approach - O(n) time
        result = 0
        curr_max = 0
        for i in range(len(current)):
            if isinstance(current[i], int):
                curr_max = max(curr_max, current[i])
                result = max(result, curr_max)
            else:
                result += 1
        return result
