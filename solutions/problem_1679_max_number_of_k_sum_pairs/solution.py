"""
Problem 1679: Max Number of K-Sum Pairs
=====================================
Difficulty: Medium
Tags: Array, Hash Table, Two Pointers, Sorting
Pattern: Hash Map / Two Sum Variant

Time Complexity:  O(n)
Space Complexity: O(n)
"""

class Solution:
    def maxOperations(self, nums: list[int], k: int) -> int:
        from collections import Counter
        count = Counter(nums)
        result = 0
        for num in list(count.keys()):
            comp = k - num
            if comp == num:
                result += count[num] // 2
            elif comp in count:
                pairs = min(count[num], count[comp])
                result += pairs
                count[num] -= pairs
                count[comp] -= pairs
        return result
