"""
Problem 1414: Find the Minimum Number of Fibonacci Numbers Whose Sum Is K
=======================================================================
Difficulty: Medium
Tags: Math, Greedy
Pattern: Greedy

Time Complexity:  O(n log n)
Space Complexity: O(1)
"""

class Solution:
    def findMinFibonacciNumbers(self, k: int) -> int:
        # Greedy approach - O(n) time
        result = 0
        curr_max = 0
        for i in range(len(k)):
            if isinstance(k[i], int):
                curr_max = max(curr_max, k[i])
                result = max(result, curr_max)
            else:
                result += 1
        return result
