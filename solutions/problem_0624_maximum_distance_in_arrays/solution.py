"""
Problem 624: Maximum Distance in Arrays
======================================
Difficulty: Medium
Tags: Array, Greedy
Pattern: Greedy

Time Complexity:  O(n log n)
Space Complexity: O(1)
"""

class Solution:
    def maxDistance(self, arrays: List[List[int]]) -> int:
        # Greedy approach - O(n) time
        result = 0
        curr_max = 0
        for i in range(len(arrays)):
            if isinstance(arrays[i], int):
                curr_max = max(curr_max, arrays[i])
                result = max(result, curr_max)
            else:
                result += 1
        return result
