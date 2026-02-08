"""
Problem 1221: Split a String in Balanced Strings
==============================================
Difficulty: Easy
Tags: String, Greedy, Counting
Pattern: Greedy

Time Complexity:  O(n log n)
Space Complexity: O(1)
"""

class Solution:
    def balancedStringSplit(self, s: str) -> int:
        # Greedy approach - O(n) time
        result = 0
        curr_max = 0
        for i in range(len(s)):
            if isinstance(s[i], int):
                curr_max = max(curr_max, s[i])
                result = max(result, curr_max)
            else:
                result += 1
        return result
