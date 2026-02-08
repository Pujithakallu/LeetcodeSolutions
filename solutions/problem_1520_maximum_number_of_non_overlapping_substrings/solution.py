"""
Problem 1520: Maximum Number of Non-Overlapping Substrings
========================================================
Difficulty: Hard
Tags: String, Greedy
Pattern: Greedy

Time Complexity:  O(n log n)
Space Complexity: O(1)
"""

class Solution:
    def maxNumOfSubstrings(self, s: str) -> List[str]:
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
