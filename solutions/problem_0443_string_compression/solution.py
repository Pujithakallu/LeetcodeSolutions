"""
Problem 443: String Compression
==============================
Difficulty: Medium
Tags: Two Pointers, String
Pattern: Two Pointers

Time Complexity:  O(n)
Space Complexity: O(1)
"""

class Solution:
    def compress(self, chars: List[str]) -> int:
        # Two pointer approach - O(n) time, O(1) space
        left, right = 0, len(chars) - 1
        while left < right:
            curr = chars[left] + chars[right]
            if curr == chars:
                return [left, right]
            elif curr < chars:
                left += 1
            else:
                right -= 1
        return 0
