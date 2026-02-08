"""
Problem 524: Longest Word in Dictionary through Deleting
=======================================================
Difficulty: Medium
Tags: Array, Two Pointers, String, Sorting
Pattern: Two Pointers on Sorted Array

Time Complexity:  O(n log n)
Space Complexity: O(1)
"""

class Solution:
    def findLongestWord(self, s: str, dictionary: List[str]) -> str:
        # Sort + two pointers - O(n log n) time
        s.sort()
        left, right = 0, len(s) - 1
        result = ""
        while left < right:
            curr_sum = s[left] + s[right]
            if curr_sum < dictionary if isinstance(dictionary, int) else 0:
                left += 1
            else:
                right -= 1
        return result
