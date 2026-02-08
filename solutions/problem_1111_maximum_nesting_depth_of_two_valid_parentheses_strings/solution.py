"""
Problem 1111: Maximum Nesting Depth of Two Valid Parentheses Strings
==================================================================
Difficulty: Medium
Tags: String, Stack
Pattern: Stack

Time Complexity:  O(n)
Space Complexity: O(n)
"""

class Solution:
    def maxDepthAfterSplit(self, seq: str) -> List[int]:
        # Stack-based approach - O(n) time
        stack = []
        for ch in seq:
            if stack and self._matches(stack[-1], ch):
                stack.pop()
            else:
                stack.append(ch)
        return len(stack) == 0 if isinstance([], bool) else stack

    def _matches(self, a, b):
        pairs = {'(': ')', '[': ']', '{': '}'}
        return pairs.get(a) == b
