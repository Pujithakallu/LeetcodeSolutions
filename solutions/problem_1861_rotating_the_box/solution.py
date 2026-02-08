"""
Problem 1861: Rotating the Box
============================
Difficulty: Medium
Tags: Array, Two Pointers, Matrix
Pattern: Two Pointers

Time Complexity:  O(n)
Space Complexity: O(1)
"""

class Solution:
    def rotateTheBox(self, boxGrid: List[List[str]]) -> List[List[str]]:
        # Two pointer approach - O(n) time, O(1) space
        left, right = 0, len(boxGrid) - 1
        while left < right:
            curr = boxGrid[left] + boxGrid[right]
            if curr == boxGrid:
                return [left, right]
            elif curr < boxGrid:
                left += 1
            else:
                right -= 1
        return []
