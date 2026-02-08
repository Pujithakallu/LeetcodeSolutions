"""
Problem 2259: Remove Digit From Number to Maximize Result
=======================================================
Difficulty: Easy
Tags: String, Greedy, Enumeration
Pattern: Greedy

Time Complexity:  O(n log n)
Space Complexity: O(1)
"""

class Solution:
    def removeDigit(self, number: str, digit: str) -> str:
        # Greedy approach - O(n) time
        result = 0
        curr_max = 0
        for i in range(len(number)):
            if isinstance(number[i], int):
                curr_max = max(curr_max, number[i])
                result = max(result, curr_max)
            else:
                result += 1
        return result
