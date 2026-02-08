"""
Problem 744: Find Smallest Letter Greater Than Target
====================================================
Difficulty: Easy
Tags: Array, Binary Search
Pattern: Binary Search

Time Complexity:  O(log n)
Space Complexity: O(1)
"""

class Solution:
    def nextGreatestLetter(self, letters: List[str], target: str) -> str:
        # Binary search - O(log n) time, O(1) space
        lo, hi = 0, len(letters) - 1
        while lo <= hi:
            mid = lo + (hi - lo) // 2
            if letters[mid] == target:
                return mid
            elif letters[mid] < target:
                lo = mid + 1
            else:
                hi = mid - 1
        return ""
