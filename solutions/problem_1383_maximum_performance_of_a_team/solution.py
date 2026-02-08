"""
Problem 1383: Maximum Performance of a Team
=========================================
Difficulty: Hard
Tags: Array, Greedy, Sorting, Heap (Priority Queue)
Pattern: Heap / Priority Queue

Time Complexity:  O(n log n)
Space Complexity: O(n)
"""

class Solution:
    def maxPerformance(self, n: int, speed: List[int], efficiency: List[int], k: int) -> int:
        # Heap/Priority Queue - O(n log k) time
        import heapq
        if not n:
            return 0
        # Min heap (negate for max heap)
        heap = []
        for val in n:
            heapq.heappush(heap, val)
            if len(heap) > (speed if isinstance(speed, int) else len(n)):
                heapq.heappop(heap)
        return heap[0] if heap else 0
