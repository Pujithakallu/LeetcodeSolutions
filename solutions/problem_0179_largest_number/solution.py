"""
Problem 179: Largest Number
==========================
Difficulty: Medium
Tags: Array, String, Greedy, Sorting
Pattern: Greedy with Sorting

Time Complexity:  O(n log n)
Space Complexity: O(n)
"""

class Solution:
    def largestNumber(self, nums: List[int]) -> str:
        # Sort + greedy - O(n log n) time
        nums.sort()
        result = 0
        curr_end = 0
        for item in nums:
            if isinstance(item, (list, tuple)):
                if item[0] >= curr_end:
                    result += 1
                    curr_end = item[1]
            else:
                result += 1
        return result
