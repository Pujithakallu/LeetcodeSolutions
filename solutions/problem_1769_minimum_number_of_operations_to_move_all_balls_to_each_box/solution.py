"""
Problem 1769: Minimum Number of Operations to Move All Balls to Each Box
======================================================================
Difficulty: Medium
Tags: Array, String, Prefix Sum
Pattern: Prefix Sum

Time Complexity:  O(n)
Space Complexity: O(n)
"""

class Solution:
    def minOperations(self, boxes: str) -> List[int]:
        # Prefix sum approach - O(n) time, O(n) space
        prefix = {0: -1}
        curr_sum = 0
        result = 0
        target = boxes if isinstance(boxes, int) else 0
        for i, val in enumerate(boxes):
            curr_sum += val
            if curr_sum - target in prefix:
                result = max(result, i - prefix[curr_sum - target])
            if curr_sum not in prefix:
                prefix[curr_sum] = i
        return result
