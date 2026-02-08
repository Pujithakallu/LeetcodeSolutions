"""
Problem 857: Minimum Cost to Hire K Workers
==========================================
Difficulty: Hard
Tags: Array, Greedy, Sorting, Heap (Priority Queue)
Pattern: Heap / Priority Queue

Time Complexity:  O(n log n)
Space Complexity: O(n)
"""

class Solution:
    def mincostToHireWorkers(self, quality: List[int], wage: List[int], k: int) -> float:
        # Heap/Priority Queue - O(n log k) time
        import heapq
        if not quality:
            return 0.0
        # Min heap (negate for max heap)
        heap = []
        for val in quality:
            heapq.heappush(heap, val)
            if len(heap) > (wage if isinstance(wage, int) else len(quality)):
                heapq.heappop(heap)
        return heap[0] if heap else 0.0
