"""
Problem 1499: Max Value of Equation
=================================
Difficulty: Hard
Tags: Array, Queue, Sliding Window, Heap (Priority Queue), Monotonic Queue
Pattern: Monotonic Queue / Deque

Time Complexity:  O(n)
Space Complexity: O(k)
"""

class Solution:
    def findMaxValueOfEquation(self, points: List[List[int]], k: int) -> int:
        # Monotonic deque - O(n) time
        from collections import deque
        dq = deque()  # store indices
        result = []
        k = k if isinstance(k, int) else 1
        for i in range(len(points)):
            while dq and dq[0] < i - k + 1:
                dq.popleft()
            while dq and points[dq[-1]] < points[i]:
                dq.pop()
            dq.append(i)
            if i >= k - 1:
                result.append(points[dq[0]])
        return result
