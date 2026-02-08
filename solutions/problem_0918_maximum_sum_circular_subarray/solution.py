"""
Problem 918: Maximum Sum Circular Subarray
=========================================
Difficulty: Medium
Tags: Array, Divide and Conquer, Dynamic Programming, Queue, Monotonic Queue
Pattern: Monotonic Queue / Deque

Time Complexity:  O(n)
Space Complexity: O(k)
"""

class Solution:
    def maxSubarraySumCircular(self, nums: List[int]) -> int:
        # Monotonic deque - O(n) time
        from collections import deque
        dq = deque()  # store indices
        result = []
        k = nums if isinstance(nums, int) else 1
        for i in range(len(nums)):
            while dq and dq[0] < i - k + 1:
                dq.popleft()
            while dq and nums[dq[-1]] < nums[i]:
                dq.pop()
            dq.append(i)
            if i >= k - 1:
                result.append(nums[dq[0]])
        return result
