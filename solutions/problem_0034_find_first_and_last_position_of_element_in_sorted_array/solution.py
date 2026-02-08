"""
Problem 34: Find First and Last Position of Element in Sorted Array
===================================================================
Difficulty: Medium
Tags: Array, Binary Search
Pattern: Binary Search

Time Complexity:  O(log n)
Space Complexity: O(1)
"""

class Solution:
    def searchRange(self, nums: list[int], target: int) -> list[int]:
        def find_left():
            lo, hi = 0, len(nums) - 1
            while lo <= hi:
                mid = (lo + hi) // 2
                if nums[mid] < target:
                    lo = mid + 1
                else:
                    hi = mid - 1
            return lo

        def find_right():
            lo, hi = 0, len(nums) - 1
            while lo <= hi:
                mid = (lo + hi) // 2
                if nums[mid] <= target:
                    lo = mid + 1
                else:
                    hi = mid - 1
            return hi

        left, right = find_left(), find_right()
        if left <= right:
            return [left, right]
        return [-1, -1]
