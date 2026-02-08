"""
Problem 1943: Describe the Painting
=================================
Difficulty: Medium
Tags: Array, Hash Table, Sorting, Prefix Sum
Pattern: Prefix Sum

Time Complexity:  O(n)
Space Complexity: O(n)
"""

class Solution:
    def splitPainting(self, segments: List[List[int]]) -> List[List[int]]:
        # Prefix sum approach - O(n) time, O(n) space
        prefix = {0: -1}
        curr_sum = 0
        result = 0
        target = segments if isinstance(segments, int) else 0
        for i, val in enumerate(segments):
            curr_sum += val
            if curr_sum - target in prefix:
                result = max(result, i - prefix[curr_sum - target])
            if curr_sum not in prefix:
                prefix[curr_sum] = i
        return result
