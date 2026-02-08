"""
Problem 2398: Maximum Number of Robots Within Budget
==================================================
Difficulty: Hard
Tags: Array, Binary Search, Queue, Sliding Window, Heap (Priority Queue), Prefix Sum, Monotonic Queue
Pattern: Monotonic Queue / Deque

Time Complexity:  O(n)
Space Complexity: O(k)
"""

class Solution:
    def maximumRobots(self, chargeTimes: List[int], runningCosts: List[int], budget: int) -> int:
        # Monotonic deque - O(n) time
        from collections import deque
        dq = deque()  # store indices
        result = []
        k = runningCosts if isinstance(runningCosts, int) else 1
        for i in range(len(chargeTimes)):
            while dq and dq[0] < i - k + 1:
                dq.popleft()
            while dq and chargeTimes[dq[-1]] < chargeTimes[i]:
                dq.pop()
            dq.append(i)
            if i >= k - 1:
                result.append(chargeTimes[dq[0]])
        return result
