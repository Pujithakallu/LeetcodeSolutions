"""
Problem 2462: Total Cost to Hire K Workers
========================================
Difficulty: Medium
Tags: Array, Two Pointers, Heap (Priority Queue), Simulation
Pattern: Two Heaps / Greedy

Time Complexity:  O((k+c) log c)
Space Complexity: O(c)
"""

import heapq

class Solution:
    def totalCost(self, costs, k, candidates):
        n = len(costs)
        left_heap = []
        right_heap = []
        l, r = 0, n - 1
        for i in range(candidates):
            if l <= r:
                heapq.heappush(left_heap, (costs[l], l))
                l += 1
        for i in range(candidates):
            if l <= r:
                heapq.heappush(right_heap, (costs[r], r))
                r -= 1
        total = 0
        for _ in range(k):
            left_val = left_heap[0] if left_heap else (float('inf'), -1)
            right_val = right_heap[0] if right_heap else (float('inf'), -1)
            if left_val <= right_val:
                cost, idx = heapq.heappop(left_heap)
                total += cost
                if l <= r:
                    heapq.heappush(left_heap, (costs[l], l))
                    l += 1
            else:
                cost, idx = heapq.heappop(right_heap)
                total += cost
                if l <= r:
                    heapq.heappush(right_heap, (costs[r], r))
                    r -= 1
        return total
