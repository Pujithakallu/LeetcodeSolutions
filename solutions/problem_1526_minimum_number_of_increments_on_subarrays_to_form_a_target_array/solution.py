"""
Problem 1526: Minimum Number of Increments on Subarrays to Form a Target Array
============================================================================
Difficulty: Hard
Tags: Array, Dynamic Programming, Stack, Greedy, Monotonic Stack
Pattern: Monotonic Stack

Time Complexity:  O(n)
Space Complexity: O(n)
"""

class Solution:
    def minNumberOperations(self, target: List[int]) -> int:
        # Monotonic stack - O(n) time, O(n) space
        n = len(target)
        result = [0] * n
        stack = []  # indices
        for i in range(n):
            while stack and target[i] > target[stack[-1]]:
                idx = stack.pop()
                result[idx] = i - idx
            stack.append(i)
        return result
