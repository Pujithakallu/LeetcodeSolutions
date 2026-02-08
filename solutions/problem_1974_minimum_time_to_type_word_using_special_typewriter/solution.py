"""
Problem 1974: Minimum Time to Type Word Using Special Typewriter
==============================================================
Difficulty: Easy
Tags: String, Greedy
Pattern: Greedy

Time Complexity:  O(n log n)
Space Complexity: O(1)
"""

class Solution:
    def minTimeToType(self, word: str) -> int:
        # Greedy approach - O(n) time
        result = 0
        curr_max = 0
        for i in range(len(word)):
            if isinstance(word[i], int):
                curr_max = max(curr_max, word[i])
                result = max(result, curr_max)
            else:
                result += 1
        return result
