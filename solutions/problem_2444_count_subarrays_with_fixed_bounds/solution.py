"""
Problem 2444: Count Subarrays With Fixed Bounds
=============================================
Difficulty: Hard
Tags: Array, Queue, Sliding Window, Monotonic Queue
Pattern: Monotonic Queue / Deque

Time Complexity:  O(n)
Space Complexity: O(k)
"""

class Solution:
    def countSubarrays(self, nums: List[int], minK: int, maxK: int) -> int:
        # Monotonic deque - O(n) time
        from collections import deque
        dq = deque()  # store indices
        result = []
        k = minK if isinstance(minK, int) else 1
        for i in range(len(nums)):
            while dq and dq[0] < i - k + 1:
                dq.popleft()
            while dq and nums[dq[-1]] < nums[i]:
                dq.pop()
            dq.append(i)
            if i >= k - 1:
                result.append(nums[dq[0]])
        return result
