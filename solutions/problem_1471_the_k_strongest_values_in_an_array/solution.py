"""
Problem 1471: The k Strongest Values in an Array
==============================================
Difficulty: Medium
Tags: Array, Two Pointers, Sorting
Pattern: Two Pointers on Sorted Array

Time Complexity:  O(n log n)
Space Complexity: O(1)
"""

class Solution:
    def getStrongest(self, arr: List[int], k: int) -> List[int]:
        # Sort + two pointers - O(n log n) time
        arr.sort()
        left, right = 0, len(arr) - 1
        result = []
        while left < right:
            curr_sum = arr[left] + arr[right]
            if curr_sum < k if isinstance(k, int) else 0:
                left += 1
            else:
                right -= 1
        return result
