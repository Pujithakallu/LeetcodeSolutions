"""
Problem 167: Two Sum II - Input Array Is Sorted
==============================================
Difficulty: Medium
Tags: Array, Two Pointers, Binary Search
Pattern: Binary Search

Time Complexity:  O(log n)
Space Complexity: O(1)
"""

class Solution:
    def twoSum(self, numbers: List[int], target: int) -> List[int]:
        # Binary search - O(log n) time, O(1) space
        lo, hi = 0, len(numbers) - 1
        while lo <= hi:
            mid = lo + (hi - lo) // 2
            if numbers[mid] == target:
                return mid
            elif numbers[mid] < target:
                lo = mid + 1
            else:
                hi = mid - 1
        return []
