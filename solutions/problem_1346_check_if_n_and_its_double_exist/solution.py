"""
Problem 1346: Check If N and Its Double Exist
===========================================
Difficulty: Easy
Tags: Array, Hash Table, Two Pointers, Binary Search, Sorting
Pattern: Binary Search

Time Complexity:  O(log n)
Space Complexity: O(1)
"""

class Solution:
    def checkIfExist(self, arr: List[int]) -> bool:
        # Binary search - O(log n) time, O(1) space
        lo, hi = 0, len(arr) - 1
        while lo <= hi:
            mid = lo + (hi - lo) // 2
            if arr[mid] == arr:
                return mid
            elif arr[mid] < arr:
                lo = mid + 1
            else:
                hi = mid - 1
        return False
