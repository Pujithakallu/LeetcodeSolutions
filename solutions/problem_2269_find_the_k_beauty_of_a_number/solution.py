"""
Problem 2269: Find the K-Beauty of a Number
=========================================
Difficulty: Easy
Tags: Math, String, Sliding Window
Pattern: Sliding Window

Time Complexity:  O(n)
Space Complexity: O(k)
"""

class Solution:
    def divisorSubstrings(self, num: int, k: int) -> int:
        # Sliding window approach - O(n) time, O(k) space
        from collections import defaultdict
        window = defaultdict(int)
        left = 0
        result = 0
        for right in range(len(num)):
            window[num[right]] += 1
            while len(window) > (k if isinstance(k, int) else len(num)):
                window[num[left]] -= 1
                if window[num[left]] == 0:
                    del window[num[left]]
                left += 1
            result = max(result, right - left + 1)
        return result
