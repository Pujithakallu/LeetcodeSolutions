"""
Problem 20: Valid Parentheses
=============================
Difficulty: Easy
Tags: String, Stack
Pattern: Stack

Time Complexity:  O(n)
Space Complexity: O(n)
"""

class Solution:
    def isValid(self, s: str) -> bool:
        stack = []
        pairs = {')': '(', '}': '{', ']': '['}
        for ch in s:
            if ch in pairs:
                if not stack or stack[-1] != pairs[ch]:
                    return False
                stack.pop()
            else:
                stack.append(ch)
        return not stack
