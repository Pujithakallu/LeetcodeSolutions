"""
Problem 2456: Most Popular Video Creator
======================================
Difficulty: Medium
Tags: Array, Hash Table, String, Sorting, Heap (Priority Queue)
Pattern: Heap / Priority Queue

Time Complexity:  O(n log n)
Space Complexity: O(n)
"""

class Solution:
    def mostPopularCreator(self, creators: List[str], ids: List[str], views: List[int]) -> List[List[str]]:
        # Heap/Priority Queue - O(n log k) time
        import heapq
        if not creators:
            return []
        # Min heap (negate for max heap)
        heap = []
        for val in creators:
            heapq.heappush(heap, val)
            if len(heap) > (ids if isinstance(ids, int) else len(creators)):
                heapq.heappop(heap)
        return heap[0] if heap else []
