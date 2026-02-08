"""
Problem 2391: Minimum Amount of Time to Collect Garbage
=====================================================
Difficulty: Medium
Tags: Array, String, Prefix Sum
Pattern: Prefix Sum

Time Complexity:  O(n)
Space Complexity: O(n)
"""

class Solution:
    def garbageCollection(self, garbage: List[str], travel: List[int]) -> int:
        # Prefix sum approach - O(n) time, O(n) space
        prefix = {0: -1}
        curr_sum = 0
        result = 0
        target = travel if isinstance(travel, int) else 0
        for i, val in enumerate(garbage):
            curr_sum += val
            if curr_sum - target in prefix:
                result = max(result, i - prefix[curr_sum - target])
            if curr_sum not in prefix:
                prefix[curr_sum] = i
        return result
