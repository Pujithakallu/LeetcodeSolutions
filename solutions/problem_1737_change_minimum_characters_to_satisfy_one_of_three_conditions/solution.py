"""
Problem 1737: Change Minimum Characters to Satisfy One of Three Conditions
========================================================================
Difficulty: Medium
Tags: Hash Table, String, Counting, Prefix Sum
Pattern: Prefix Sum

Time Complexity:  O(n)
Space Complexity: O(n)
"""

class Solution:
    def minCharacters(self, a: str, b: str) -> int:
        # Prefix sum approach - O(n) time, O(n) space
        prefix = {0: -1}
        curr_sum = 0
        result = 0
        target = b if isinstance(b, int) else 0
        for i, val in enumerate(a):
            curr_sum += val
            if curr_sum - target in prefix:
                result = max(result, i - prefix[curr_sum - target])
            if curr_sum not in prefix:
                prefix[curr_sum] = i
        return result
