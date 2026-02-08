"""
Problem 525: Contiguous Array
============================
Difficulty: Medium
Tags: Array, Hash Table, Prefix Sum
Pattern: Prefix Sum + Hash Map

Time Complexity:  O(n)
Space Complexity: O(n)
"""

class Solution:
    def findMaxLength(self, nums: list[int]) -> int:
        count = 0
        max_len = 0
        map = {0: -1}
        for i, num in enumerate(nums):
            count += 1 if num == 1 else -1
            if count in map:
                max_len = max(max_len, i - map[count])
            else:
                map[count] = i
        return max_len
