"""
Problem 347: Top K Frequent Elements
===================================
Difficulty: Medium
Tags: Array, Hash Table, Divide and Conquer, Sorting, Heap (Priority Queue), Bucket Sort, Counting, Quickselect
Pattern: Hash Map / Heap

Time Complexity:  O(n log k)
Space Complexity: O(n)
"""

from collections import Counter

class Solution:
    def topKFrequent(self, nums: list[int], k: int) -> list[int]:
        count = Counter(nums)
        return [x for x, _ in count.most_common(k)]
