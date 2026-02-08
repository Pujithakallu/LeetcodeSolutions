"""
Problem 209: Minimum Size Subarray Sum
=====================================
Difficulty: Medium
Tags: Array, Binary Search, Sliding Window, Prefix Sum
Pattern: Sliding Window

Time Complexity:  O(n)
Space Complexity: O(k)
"""

class Solution:
    def minSubArrayLen(self, target: int, nums: List[int]) -> int:
        # Sliding window approach - O(n) time, O(k) space
        from collections import defaultdict
        window = defaultdict(int)
        left = 0
        result = 0
        for right in range(len(target)):
            window[target[right]] += 1
            while len(window) > (nums if isinstance(nums, int) else len(target)):
                window[target[left]] -= 1
                if window[target[left]] == 0:
                    del window[target[left]]
                left += 1
            result = max(result, right - left + 1)
        return result
