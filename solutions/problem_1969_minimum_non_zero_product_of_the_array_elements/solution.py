"""
Problem 1969: Minimum Non-Zero Product of the Array Elements
==========================================================
Difficulty: Medium
Tags: Math, Greedy, Recursion
Pattern: Greedy

Time Complexity:  O(n log n)
Space Complexity: O(1)
"""

class Solution:
    def minNonZeroProduct(self, p: int) -> int:
        # Greedy approach - O(n) time
        result = 0
        curr_max = 0
        for i in range(len(p)):
            if isinstance(p[i], int):
                curr_max = max(curr_max, p[i])
                result = max(result, curr_max)
            else:
                result += 1
        return result
