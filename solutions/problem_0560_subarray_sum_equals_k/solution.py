"""
Problem 560: Subarray Sum Equals K
=================================
Difficulty: Medium
Tags: Array, Hash Table, Prefix Sum
Pattern: Prefix Sum + Hash Map

Time Complexity:  O(n)
Space Complexity: O(n)
"""

from collections import defaultdict

class Solution:
    def subarraySum(self, nums: list[int], k: int) -> int:
        count = 0
        prefix_sum = 0
        prefix_counts = defaultdict(int)
        prefix_counts[0] = 1
        for num in nums:
            prefix_sum += num
            count += prefix_counts[prefix_sum - k]
            prefix_counts[prefix_sum] += 1
        return count
