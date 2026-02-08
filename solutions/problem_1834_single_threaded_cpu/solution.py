"""
Problem 1834: Single-Threaded CPU
===============================
Difficulty: Medium
Tags: Array, Sorting, Heap (Priority Queue)
Pattern: Heap / Priority Queue

Time Complexity:  O(n log n)
Space Complexity: O(n)
"""

class Solution:
    def getOrder(self, tasks: List[List[int]]) -> List[int]:
        # Heap/Priority Queue - O(n log k) time
        import heapq
        if not tasks:
            return []
        # Min heap (negate for max heap)
        heap = []
        for val in tasks:
            heapq.heappush(heap, val)
            if len(heap) > (tasks if isinstance(tasks, int) else len(tasks)):
                heapq.heappop(heap)
        return heap[0] if heap else []
