"""
Problem 2483: Minimum Penalty for a Shop
======================================
Difficulty: Medium
Tags: String, Prefix Sum
Pattern: Prefix Sum

Time Complexity:  O(n)
Space Complexity: O(n)
"""

class Solution:
    def bestClosingTime(self, customers: str) -> int:
        # Prefix sum approach - O(n) time, O(n) space
        prefix = {0: -1}
        curr_sum = 0
        result = 0
        target = customers if isinstance(customers, int) else 0
        for i, val in enumerate(customers):
            curr_sum += val
            if curr_sum - target in prefix:
                result = max(result, i - prefix[curr_sum - target])
            if curr_sum not in prefix:
                prefix[curr_sum] = i
        return result
