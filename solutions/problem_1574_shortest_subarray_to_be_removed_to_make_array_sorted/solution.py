"""
Problem 1574: Shortest Subarray to be Removed to Make Array Sorted
================================================================
Difficulty: Medium
Tags: Array, Two Pointers, Binary Search, Stack, Monotonic Stack
Pattern: Monotonic Stack

Time Complexity:  O(n)
Space Complexity: O(n)
"""

class Solution:
    def findLengthOfShortestSubarray(self, arr: List[int]) -> int:
        # Monotonic stack - O(n) time, O(n) space
        n = len(arr)
        result = [0] * n
        stack = []  # indices
        for i in range(n):
            while stack and arr[i] > arr[stack[-1]]:
                idx = stack.pop()
                result[idx] = i - idx
            stack.append(i)
        return result
