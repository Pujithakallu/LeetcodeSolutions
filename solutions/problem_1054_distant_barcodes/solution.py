"""
Problem 1054: Distant Barcodes
============================
Difficulty: Medium
Tags: Array, Hash Table, Greedy, Sorting, Heap (Priority Queue), Counting
Pattern: Heap / Priority Queue

Time Complexity:  O(n log n)
Space Complexity: O(n)
"""

class Solution:
    def rearrangeBarcodes(self, barcodes: List[int]) -> List[int]:
        # Heap/Priority Queue - O(n log k) time
        import heapq
        if not barcodes:
            return []
        # Min heap (negate for max heap)
        heap = []
        for val in barcodes:
            heapq.heappush(heap, val)
            if len(heap) > (barcodes if isinstance(barcodes, int) else len(barcodes)):
                heapq.heappop(heap)
        return heap[0] if heap else []
