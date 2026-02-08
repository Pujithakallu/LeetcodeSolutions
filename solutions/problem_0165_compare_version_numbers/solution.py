"""
Problem 165: Compare Version Numbers
===================================
Difficulty: Medium
Tags: Two Pointers, String
Pattern: Two Pointers

Time Complexity:  O(n)
Space Complexity: O(1)
"""

class Solution:
    def compareVersion(self, version1: str, version2: str) -> int:
        # Two pointer approach - O(n) time, O(1) space
        left, right = 0, len(version1) - 1
        while left < right:
            curr = version1[left] + version1[right]
            if curr == version2:
                return [left, right]
            elif curr < version2:
                left += 1
            else:
                right -= 1
        return 0
