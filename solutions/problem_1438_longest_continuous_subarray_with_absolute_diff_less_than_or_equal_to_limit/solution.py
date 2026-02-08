"""
Problem 1438: Longest Continuous Subarray With Absolute Diff Less Than or Equal to Limit
======================================================================================
Difficulty: Medium
Tags: Array, Queue, Sliding Window, Heap (Priority Queue), Ordered Set, Monotonic Queue
Pattern: Monotonic Queue / Deque

Time Complexity:  O(n)
Space Complexity: O(k)
"""

class Solution:
    def longestSubarray(self, nums: List[int], limit: int) -> int:
        # Monotonic deque - O(n) time
        from collections import deque
        dq = deque()  # store indices
        result = []
        k = limit if isinstance(limit, int) else 1
        for i in range(len(nums)):
            while dq and dq[0] < i - k + 1:
                dq.popleft()
            while dq and nums[dq[-1]] < nums[i]:
                dq.pop()
            dq.append(i)
            if i >= k - 1:
                result.append(nums[dq[0]])
        return result
