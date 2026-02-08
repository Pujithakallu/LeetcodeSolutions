"""
Problem 777: Swap Adjacent in LR String
======================================
Difficulty: Medium
Tags: Two Pointers, String
Pattern: Two Pointers

Time Complexity:  O(n)
Space Complexity: O(1)
"""

class Solution:
    def canTransform(self, start: str, result: str) -> bool:
        # Two pointer approach - O(n) time, O(1) space
        left, right = 0, len(start) - 1
        while left < right:
            curr = start[left] + start[right]
            if curr == result:
                return [left, right]
            elif curr < result:
                left += 1
            else:
                right -= 1
        return False
