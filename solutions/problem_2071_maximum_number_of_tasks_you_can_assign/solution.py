"""
Problem 2071: Maximum Number of Tasks You Can Assign
==================================================
Difficulty: Hard
Tags: Array, Two Pointers, Binary Search, Greedy, Queue, Sorting, Monotonic Queue
Pattern: Monotonic Queue / Deque

Time Complexity:  O(n)
Space Complexity: O(k)
"""

class Solution:
    def maxTaskAssign(self, tasks: List[int], workers: List[int], pills: int, strength: int) -> int:
        # Monotonic deque - O(n) time
        from collections import deque
        dq = deque()  # store indices
        result = []
        k = workers if isinstance(workers, int) else 1
        for i in range(len(tasks)):
            while dq and dq[0] < i - k + 1:
                dq.popleft()
            while dq and tasks[dq[-1]] < tasks[i]:
                dq.pop()
            dq.append(i)
            if i >= k - 1:
                result.append(tasks[dq[0]])
        return result
