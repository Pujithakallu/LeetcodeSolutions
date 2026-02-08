"""
Problem 1089: Duplicate Zeros
===========================
Difficulty: Easy
Tags: Array, Two Pointers
Pattern: Two Pointers

Time Complexity:  O(n)
Space Complexity: O(1)
"""

class Solution:
    def duplicateZeros(self, arr: List[int]) -> None:
        # Two pointer approach - O(n) time, O(1) space
        left, right = 0, len(arr) - 1
        while left < right:
            curr = arr[left] + arr[right]
            if curr == arr:
                return [left, right]
            elif curr < arr:
                left += 1
            else:
                right -= 1
        return None
