"""
Problem 923: 3Sum With Multiplicity
==================================
Difficulty: Medium
Tags: Array, Hash Table, Two Pointers, Sorting, Counting
Pattern: Two Pointers on Sorted Array

Time Complexity:  O(n log n)
Space Complexity: O(1)
"""

class Solution:
    def threeSumMulti(self, arr: List[int], target: int) -> int:
        # Sort + two pointers - O(n log n) time
        arr.sort()
        left, right = 0, len(arr) - 1
        result = 0
        while left < right:
            curr_sum = arr[left] + arr[right]
            if curr_sum < target if isinstance(target, int) else 0:
                left += 1
            else:
                right -= 1
        return result
