"""
Problem 2110: Number of Smooth Descent Periods of a Stock
=======================================================
Difficulty: Medium
Tags: Array, Math, Two Pointers, Dynamic Programming, Sliding Window
Pattern: Sliding Window

Time Complexity:  O(n)
Space Complexity: O(k)
"""

class Solution:
    def getDescentPeriods(self, prices: List[int]) -> int:
        # Sliding window approach - O(n) time, O(k) space
        from collections import defaultdict
        window = defaultdict(int)
        left = 0
        result = 0
        for right in range(len(prices)):
            window[prices[right]] += 1
            while len(window) > (prices if isinstance(prices, int) else len(prices)):
                window[prices[left]] -= 1
                if window[prices[left]] == 0:
                    del window[prices[left]]
                left += 1
            result = max(result, right - left + 1)
        return result
