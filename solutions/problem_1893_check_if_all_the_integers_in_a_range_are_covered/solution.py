"""
Problem 1893: Check if All the Integers in a Range Are Covered
============================================================
Difficulty: Easy
Tags: Array, Hash Table, Prefix Sum
Pattern: Prefix Sum

Time Complexity:  O(n)
Space Complexity: O(n)
"""

class Solution:
    def isCovered(self, ranges: List[List[int]], left: int, right: int) -> bool:
        # Prefix sum approach - O(n) time, O(n) space
        prefix = {0: -1}
        curr_sum = 0
        result = 0
        target = left if isinstance(left, int) else 0
        for i, val in enumerate(ranges):
            curr_sum += val
            if curr_sum - target in prefix:
                result = max(result, i - prefix[curr_sum - target])
            if curr_sum not in prefix:
                prefix[curr_sum] = i
        return result
