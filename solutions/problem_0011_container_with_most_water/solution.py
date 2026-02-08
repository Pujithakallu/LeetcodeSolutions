"""
Problem 11: Container With Most Water
=====================================
Difficulty: Medium
Tags: Array, Two Pointers, Greedy
Pattern: Two Pointers

Time Complexity:  O(n)
Space Complexity: O(1)
"""

class Solution:
    def maxArea(self, height: list[int]) -> int:
        left, right = 0, len(height) - 1
        max_area = 0
        while left < right:
            area = min(height[left], height[right]) * (right - left)
            max_area = max(max_area, area)
            if height[left] < height[right]:
                left += 1
            else:
                right -= 1
        return max_area
