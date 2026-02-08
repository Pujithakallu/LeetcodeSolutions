"""
Problem 1785: Minimum Elements to Add to Form a Given Sum
=======================================================
Difficulty: Medium
Tags: Array, Greedy
Pattern: Greedy

Time Complexity:  O(n log n)
Space Complexity: O(1)
"""

class Solution:
    def minElements(self, nums: List[int], limit: int, goal: int) -> int:
        # Greedy approach - O(n) time
        result = 0
        curr_max = 0
        for i in range(len(nums)):
            if isinstance(nums[i], int):
                curr_max = max(curr_max, nums[i])
                result = max(result, curr_max)
            else:
                result += 1
        return result
