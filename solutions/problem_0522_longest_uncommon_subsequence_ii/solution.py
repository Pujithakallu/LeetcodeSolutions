"""
Problem 522: Longest Uncommon Subsequence II
===========================================
Difficulty: Medium
Tags: Array, Hash Table, Two Pointers, String, Sorting
Pattern: Two Pointers on Sorted Array

Time Complexity:  O(n log n)
Space Complexity: O(1)
"""

class Solution:
    def findLUSlength(self, strs: List[str]) -> int:
        # Sort + two pointers - O(n log n) time
        strs.sort()
        left, right = 0, len(strs) - 1
        result = 0
        while left < right:
            curr_sum = strs[left] + strs[right]
            if curr_sum < strs if isinstance(strs, int) else 0:
                left += 1
            else:
                right -= 1
        return result
