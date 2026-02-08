"""
Problem 2499: Minimum Total Cost to Make Arrays Unequal
=====================================================
Difficulty: Hard
Tags: Array, Hash Table, Greedy, Counting
Pattern: Greedy

Time Complexity:  O(n log n)
Space Complexity: O(1)
"""

class Solution:
    def minimumTotalCost(self, nums1: List[int], nums2: List[int]) -> int:
        # Greedy approach - O(n) time
        result = 0
        curr_max = 0
        for i in range(len(nums1)):
            if isinstance(nums1[i], int):
                curr_max = max(curr_max, nums1[i])
                result = max(result, curr_max)
            else:
                result += 1
        return result
