"""
Problem 837: New 21 Game
=======================
Difficulty: Medium
Tags: Math, Dynamic Programming, Sliding Window, Probability and Statistics
Pattern: Sliding Window

Time Complexity:  O(n)
Space Complexity: O(k)
"""

class Solution:
    def new21Game(self, n: int, k: int, maxPts: int) -> float:
        # Sliding window approach - O(n) time, O(k) space
        from collections import defaultdict
        window = defaultdict(int)
        left = 0
        result = 0
        for right in range(len(n)):
            window[n[right]] += 1
            while len(window) > (k if isinstance(k, int) else len(n)):
                window[n[left]] -= 1
                if window[n[left]] == 0:
                    del window[n[left]]
                left += 1
            result = max(result, right - left + 1)
        return result
