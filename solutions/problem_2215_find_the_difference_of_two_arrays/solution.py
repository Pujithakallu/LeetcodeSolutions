"""
Problem 2215: Find the Difference of Two Arrays
=============================================
Difficulty: Easy
Tags: Array, Hash Table
Pattern: Hash Set

Time Complexity:  O(n+m)
Space Complexity: O(n+m)
"""

class Solution:
    def findDifference(self, nums1, nums2):
        s1, s2 = set(nums1), set(nums2)
        return [list(s1 - s2), list(s2 - s1)]
