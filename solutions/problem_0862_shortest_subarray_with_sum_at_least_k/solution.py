"""
Problem 862: Shortest Subarray with Sum at Least K
=================================================
Difficulty: Hard
Tags: Array, Binary Search, Queue, Sliding Window, Heap (Priority Queue), Prefix Sum, Monotonic Queue
Pattern: Monotonic Queue / Deque

Time Complexity:  O(n)
Space Complexity: O(k)
"""

class Solution:
    def shortestSubarray(self, nums: List[int], k: int) -> int:
        # Monotonic deque - O(n) time
        from collections import deque
        dq = deque()  # store indices
        result = []
        k = k if isinstance(k, int) else 1
        for i in range(len(nums)):
            while dq and dq[0] < i - k + 1:
                dq.popleft()
            while dq and nums[dq[-1]] < nums[i]:
                dq.pop()
            dq.append(i)
            if i >= k - 1:
                result.append(nums[dq[0]])
        return result
