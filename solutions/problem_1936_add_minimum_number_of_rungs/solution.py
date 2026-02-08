"""
Problem 1936: Add Minimum Number of Rungs
=======================================
Difficulty: Medium
Tags: Array, Greedy
Pattern: Greedy

Time Complexity:  O(n log n)
Space Complexity: O(1)
"""

class Solution:
    def addRungs(self, rungs: List[int], dist: int) -> int:
        # Greedy approach - O(n) time
        result = 0
        curr_max = 0
        for i in range(len(rungs)):
            if isinstance(rungs[i], int):
                curr_max = max(curr_max, rungs[i])
                result = max(result, curr_max)
            else:
                result += 1
        return result
