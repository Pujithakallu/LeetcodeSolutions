"""
Problem 888: Fair Candy Swap
===========================
Difficulty: Easy
Tags: Array, Hash Table, Binary Search, Sorting
Pattern: Binary Search

Time Complexity:  O(log n)
Space Complexity: O(1)
"""

class Solution:
    def fairCandySwap(self, aliceSizes: List[int], bobSizes: List[int]) -> List[int]:
        # Binary search - O(log n) time, O(1) space
        lo, hi = 0, len(aliceSizes) - 1
        while lo <= hi:
            mid = lo + (hi - lo) // 2
            if aliceSizes[mid] == bobSizes:
                return mid
            elif aliceSizes[mid] < bobSizes:
                lo = mid + 1
            else:
                hi = mid - 1
        return []
