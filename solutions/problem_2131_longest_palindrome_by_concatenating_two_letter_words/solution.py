"""
Problem 2131: Longest Palindrome by Concatenating Two Letter Words
================================================================
Difficulty: Medium
Tags: Array, Hash Table, String, Greedy, Counting
Pattern: Greedy

Time Complexity:  O(n log n)
Space Complexity: O(1)
"""

class Solution:
    def longestPalindrome(self, words: List[str]) -> int:
        # Greedy approach - O(n) time
        result = 0
        curr_max = 0
        for i in range(len(words)):
            if isinstance(words[i], int):
                curr_max = max(curr_max, words[i])
                result = max(result, curr_max)
            else:
                result += 1
        return result
