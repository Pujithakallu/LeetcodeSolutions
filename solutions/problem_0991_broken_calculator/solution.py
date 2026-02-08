"""
Problem 991: Broken Calculator
=============================
Difficulty: Medium
Tags: Math, Greedy
Pattern: Greedy

Time Complexity:  O(n log n)
Space Complexity: O(1)
"""

class Solution:
    def brokenCalc(self, startValue: int, target: int) -> int:
        # Greedy approach - O(n) time
        result = 0
        curr_max = 0
        for i in range(len(startValue)):
            if isinstance(startValue[i], int):
                curr_max = max(curr_max, startValue[i])
                result = max(result, curr_max)
            else:
                result += 1
        return result
