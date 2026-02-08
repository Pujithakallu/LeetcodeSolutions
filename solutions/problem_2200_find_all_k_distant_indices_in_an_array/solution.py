"""
Problem 2200: Find All K-Distant Indices in an Array
==================================================
Difficulty: Easy
Tags: Array, Two Pointers
Pattern: Two Pointers

Time Complexity:  O(n)
Space Complexity: O(1)
"""

class Solution:
    def findKDistantIndices(self, nums: List[int], key: int, k: int) -> List[int]:
        # Two pointer approach - O(n) time, O(1) space
        left, right = 0, len(nums) - 1
        while left < right:
            curr = nums[left] + nums[right]
            if curr == key:
                return [left, right]
            elif curr < key:
                left += 1
            else:
                right -= 1
        return []
