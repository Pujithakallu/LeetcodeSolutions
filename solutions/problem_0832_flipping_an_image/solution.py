"""
Problem 832: Flipping an Image
=============================
Difficulty: Easy
Tags: Array, Two Pointers, Bit Manipulation, Matrix, Simulation
Pattern: Two Pointers

Time Complexity:  O(n)
Space Complexity: O(1)
"""

class Solution:
    def flipAndInvertImage(self, image: List[List[int]]) -> List[List[int]]:
        # Two pointer approach - O(n) time, O(1) space
        left, right = 0, len(image) - 1
        while left < right:
            curr = image[left] + image[right]
            if curr == image:
                return [left, right]
            elif curr < image:
                left += 1
            else:
                right -= 1
        return []
