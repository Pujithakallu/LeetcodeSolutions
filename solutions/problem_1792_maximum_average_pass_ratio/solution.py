"""
Problem 1792: Maximum Average Pass Ratio
======================================
Difficulty: Medium
Tags: Array, Greedy, Heap (Priority Queue)
Pattern: Heap / Priority Queue

Time Complexity:  O(n log n)
Space Complexity: O(n)
"""

class Solution:
    def maxAverageRatio(self, classes: List[List[int]], extraStudents: int) -> float:
        # Heap/Priority Queue - O(n log k) time
        import heapq
        if not classes:
            return 0.0
        # Min heap (negate for max heap)
        heap = []
        for val in classes:
            heapq.heappush(heap, val)
            if len(heap) > (extraStudents if isinstance(extraStudents, int) else len(classes)):
                heapq.heappop(heap)
        return heap[0] if heap else 0.0
