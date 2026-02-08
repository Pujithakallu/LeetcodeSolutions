"""
Problem 986: Interval List Intersections
=======================================
Difficulty: Medium
Tags: Array, Two Pointers, Sweep Line
Pattern: Two Pointers

Time Complexity:  O(n)
Space Complexity: O(1)
"""

class Solution:
    def intervalIntersection(self, firstList: List[List[int]], secondList: List[List[int]]) -> List[List[int]]:
        # Two pointer approach - O(n) time, O(1) space
        left, right = 0, len(firstList) - 1
        while left < right:
            curr = firstList[left] + firstList[right]
            if curr == secondList:
                return [left, right]
            elif curr < secondList:
                left += 1
            else:
                right -= 1
        return []
