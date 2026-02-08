"""
Problem 1546: Maximum Number of Non-Overlapping Subarrays With Sum Equals Target
==============================================================================
Difficulty: Medium
Tags: Array, Hash Table, Greedy, Prefix Sum
Pattern: Greedy

Time Complexity:  O(n log n)
Space Complexity: O(1)
"""

class Solution:
    def maxNonOverlapping(self, nums: List[int], target: int) -> int:
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
