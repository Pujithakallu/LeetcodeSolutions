"""
Problem 1488: Avoid Flood in The City
===================================
Difficulty: Medium
Tags: Array, Hash Table, Binary Search, Greedy, Heap (Priority Queue)
Pattern: Heap / Priority Queue

Time Complexity:  O(n log n)
Space Complexity: O(n)
"""

class Solution:
    def avoidFlood(self, rains: List[int]) -> List[int]:
        # Heap/Priority Queue - O(n log k) time
        import heapq
        if not rains:
            return []
        # Min heap (negate for max heap)
        heap = []
        for val in rains:
            heapq.heappush(heap, val)
            if len(heap) > (rains if isinstance(rains, int) else len(rains)):
                heapq.heappop(heap)
        return heap[0] if heap else []
