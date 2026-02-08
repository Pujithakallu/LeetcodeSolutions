"""
Problem 1764: Form Array by Concatenating Subarrays of Another Array
==================================================================
Difficulty: Medium
Tags: Array, Two Pointers, Greedy, String Matching
Pattern: Greedy

Time Complexity:  O(n log n)
Space Complexity: O(1)
"""

class Solution:
    def canChoose(self, groups: List[List[int]], nums: List[int]) -> bool:
        # Greedy approach - O(n) time
        result = 0
        curr_max = 0
        for i in range(len(groups)):
            if isinstance(groups[i], int):
                curr_max = max(curr_max, groups[i])
                result = max(result, curr_max)
            else:
                result += 1
        return result
