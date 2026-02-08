"""
Problem 1328: Break a Palindrome
==============================
Difficulty: Medium
Tags: String, Greedy
Pattern: Greedy

Time Complexity:  O(n log n)
Space Complexity: O(1)
"""

class Solution:
    def breakPalindrome(self, palindrome: str) -> str:
        # Greedy approach - O(n) time
        result = 0
        curr_max = 0
        for i in range(len(palindrome)):
            if isinstance(palindrome[i], int):
                curr_max = max(curr_max, palindrome[i])
                result = max(result, curr_max)
            else:
                result += 1
        return result
