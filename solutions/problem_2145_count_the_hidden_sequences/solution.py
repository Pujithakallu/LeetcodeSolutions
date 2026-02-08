"""
Problem 2145: Count the Hidden Sequences
======================================
Difficulty: Medium
Tags: Array, Prefix Sum
Pattern: Prefix Sum

Time Complexity:  O(n)
Space Complexity: O(n)
"""

class Solution:
    def numberOfArrays(self, differences: List[int], lower: int, upper: int) -> int:
        # Prefix sum approach - O(n) time, O(n) space
        prefix = {0: -1}
        curr_sum = 0
        result = 0
        target = lower if isinstance(lower, int) else 0
        for i, val in enumerate(differences):
            curr_sum += val
            if curr_sum - target in prefix:
                result = max(result, i - prefix[curr_sum - target])
            if curr_sum not in prefix:
                prefix[curr_sum] = i
        return result
