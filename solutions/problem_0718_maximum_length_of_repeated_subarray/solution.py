"""
Problem 718: Maximum Length of Repeated Subarray
===============================================
Difficulty: Medium
Tags: Array, Binary Search, Dynamic Programming, Sliding Window, Rolling Hash, Hash Function
Pattern: Sliding Window

Time Complexity:  O(n)
Space Complexity: O(k)
"""

class Solution:
    def findLength(self, nums1: List[int], nums2: List[int]) -> int:
        # Sliding window approach - O(n) time, O(k) space
        from collections import defaultdict
        window = defaultdict(int)
        left = 0
        result = 0
        for right in range(len(nums1)):
            window[nums1[right]] += 1
            while len(window) > (nums2 if isinstance(nums2, int) else len(nums1)):
                window[nums1[left]] -= 1
                if window[nums1[left]] == 0:
                    del window[nums1[left]]
                left += 1
            result = max(result, right - left + 1)
        return result
