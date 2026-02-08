"""
Problem 532: K-diff Pairs in an Array
====================================
Difficulty: Medium
Tags: Array, Hash Table, Two Pointers, Binary Search, Sorting
Pattern: Hash Map

Time Complexity:  O(n)
Space Complexity: O(n)
"""

class Solution:
    def findPairs(self, nums: list[int], k: int) -> int:
        from collections import Counter
        counter = Counter(nums)
        result = 0
        for num in counter:
            if k == 0 and counter[num] > 1:
                result += 1
            elif k > 0 and num + k in counter:
                result += 1
        return result
