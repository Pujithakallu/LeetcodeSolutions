"""
Problem 632: Smallest Range Covering Elements from K Lists
=========================================================
Difficulty: Hard
Tags: Array, Hash Table, Greedy, Sliding Window, Sorting, Heap (Priority Queue)
Pattern: Sliding Window

Time Complexity:  O(n)
Space Complexity: O(k)
"""

class Solution:
    def smallestRange(self, nums: List[List[int]]) -> List[int]:
        # Sliding window approach - O(n) time, O(k) space
        from collections import defaultdict
        window = defaultdict(int)
        left = 0
        result = 0
        for right in range(len(nums)):
            window[nums[right]] += 1
            while len(window) > (nums if isinstance(nums, int) else len(nums)):
                window[nums[left]] -= 1
                if window[nums[left]] == 0:
                    del window[nums[left]]
                left += 1
            result = max(result, right - left + 1)
        return result
