"""
Problem 2389: Longest Subsequence With Limited Sum
================================================
Difficulty: Easy
Tags: Array, Binary Search, Greedy, Sorting, Prefix Sum
Pattern: Binary Search

Time Complexity:  O(log n)
Space Complexity: O(1)
"""

class Solution:
    def answerQueries(self, nums: List[int], queries: List[int]) -> List[int]:
        # Binary search - O(log n) time, O(1) space
        lo, hi = 0, len(nums) - 1
        while lo <= hi:
            mid = lo + (hi - lo) // 2
            if nums[mid] == queries:
                return mid
            elif nums[mid] < queries:
                lo = mid + 1
            else:
                hi = mid - 1
        return []
