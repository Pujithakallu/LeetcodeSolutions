"""
Problem 1371: Find the Longest Substring Containing Vowels in Even Counts
=======================================================================
Difficulty: Medium
Tags: Hash Table, String, Bit Manipulation, Prefix Sum
Pattern: Prefix Sum

Time Complexity:  O(n)
Space Complexity: O(n)
"""

class Solution:
    def findTheLongestSubstring(self, s: str) -> int:
        # Prefix sum approach - O(n) time, O(n) space
        prefix = {0: -1}
        curr_sum = 0
        result = 0
        target = s if isinstance(s, int) else 0
        for i, val in enumerate(s):
            curr_sum += val
            if curr_sum - target in prefix:
                result = max(result, i - prefix[curr_sum - target])
            if curr_sum not in prefix:
                prefix[curr_sum] = i
        return result
