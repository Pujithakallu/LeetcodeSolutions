"""
Problem 1705: Maximum Number of Eaten Apples
==========================================
Difficulty: Medium
Tags: Array, Greedy, Heap (Priority Queue)
Pattern: Heap / Priority Queue

Time Complexity:  O(n log n)
Space Complexity: O(n)
"""

class Solution:
    def eatenApples(self, apples: List[int], days: List[int]) -> int:
        # Heap/Priority Queue - O(n log k) time
        import heapq
        if not apples:
            return 0
        # Min heap (negate for max heap)
        heap = []
        for val in apples:
            heapq.heappush(heap, val)
            if len(heap) > (days if isinstance(days, int) else len(apples)):
                heapq.heappop(heap)
        return heap[0] if heap else 0
