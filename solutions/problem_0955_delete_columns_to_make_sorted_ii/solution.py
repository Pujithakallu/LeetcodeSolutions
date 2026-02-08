"""
Problem 955: Delete Columns to Make Sorted II
============================================
Difficulty: Medium
Tags: Array, String, Greedy
Pattern: Greedy

Time Complexity:  O(n log n)
Space Complexity: O(1)
"""

class Solution:
    def minDeletionSize(self, strs: List[str]) -> int:
        # Greedy approach - O(n) time
        result = 0
        curr_max = 0
        for i in range(len(strs)):
            if isinstance(strs[i], int):
                curr_max = max(curr_max, strs[i])
                result = max(result, curr_max)
            else:
                result += 1
        return result
