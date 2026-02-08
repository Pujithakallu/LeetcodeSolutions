"""
Problem 1477: Find Two Non-overlapping Sub-arrays Each With Target Sum
====================================================================
Difficulty: Medium
Tags: Array, Hash Table, Binary Search, Dynamic Programming, Sliding Window
Pattern: Sliding Window

Time Complexity:  O(n)
Space Complexity: O(k)
"""

class Solution:
    def minSumOfLengths(self, arr: List[int], target: int) -> int:
        # Sliding window approach - O(n) time, O(k) space
        from collections import defaultdict
        window = defaultdict(int)
        left = 0
        result = 0
        for right in range(len(arr)):
            window[arr[right]] += 1
            while len(window) > (target if isinstance(target, int) else len(arr)):
                window[arr[left]] -= 1
                if window[arr[left]] == 0:
                    del window[arr[left]]
                left += 1
            result = max(result, right - left + 1)
        return result
