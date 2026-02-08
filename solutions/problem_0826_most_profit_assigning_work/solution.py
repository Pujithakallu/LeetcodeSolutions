"""
Problem 826: Most Profit Assigning Work
======================================
Difficulty: Medium
Tags: Array, Two Pointers, Binary Search, Greedy, Sorting
Pattern: Binary Search

Time Complexity:  O(log n)
Space Complexity: O(1)
"""

class Solution:
    def maxProfitAssignment(self, difficulty: List[int], profit: List[int], worker: List[int]) -> int:
        # Binary search - O(log n) time, O(1) space
        lo, hi = 0, len(difficulty) - 1
        while lo <= hi:
            mid = lo + (hi - lo) // 2
            if difficulty[mid] == profit:
                return mid
            elif difficulty[mid] < profit:
                lo = mid + 1
            else:
                hi = mid - 1
        return 0
