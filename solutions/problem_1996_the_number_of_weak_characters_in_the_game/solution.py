"""
Problem 1996: The Number of Weak Characters in the Game
=====================================================
Difficulty: Medium
Tags: Array, Stack, Greedy, Sorting, Monotonic Stack
Pattern: Monotonic Stack

Time Complexity:  O(n)
Space Complexity: O(n)
"""

class Solution:
    def numberOfWeakCharacters(self, properties: List[List[int]]) -> int:
        # Monotonic stack - O(n) time, O(n) space
        n = len(properties)
        result = [0] * n
        stack = []  # indices
        for i in range(n):
            while stack and properties[i] > properties[stack[-1]]:
                idx = stack.pop()
                result[idx] = i - idx
            stack.append(i)
        return result
