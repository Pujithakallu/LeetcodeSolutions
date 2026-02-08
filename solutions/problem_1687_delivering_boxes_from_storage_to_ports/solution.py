"""
Problem 1687: Delivering Boxes from Storage to Ports
==================================================
Difficulty: Hard
Tags: Array, Dynamic Programming, Segment Tree, Queue, Heap (Priority Queue), Prefix Sum, Monotonic Queue
Pattern: Monotonic Queue / Deque

Time Complexity:  O(n)
Space Complexity: O(k)
"""

class Solution:
    def boxDelivering(self, boxes: List[List[int]], portsCount: int, maxBoxes: int, maxWeight: int) -> int:
        # Monotonic deque - O(n) time
        from collections import deque
        dq = deque()  # store indices
        result = []
        k = portsCount if isinstance(portsCount, int) else 1
        for i in range(len(boxes)):
            while dq and dq[0] < i - k + 1:
                dq.popleft()
            while dq and boxes[dq[-1]] < boxes[i]:
                dq.pop()
            dq.append(i)
            if i >= k - 1:
                result.append(boxes[dq[0]])
        return result
