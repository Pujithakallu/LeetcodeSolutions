"""
Problem 1338: Reduce Array Size to The Half
=========================================
Difficulty: Medium
Tags: Array, Hash Table, Greedy, Sorting, Heap (Priority Queue)
Pattern: Heap / Priority Queue

Time Complexity:  O(n log n)
Space Complexity: O(n)
"""

class Solution:
    def minSetSize(self, arr: List[int]) -> int:
        # Heap/Priority Queue - O(n log k) time
        import heapq
        if not arr:
            return 0
        # Min heap (negate for max heap)
        heap = []
        for val in arr:
            heapq.heappush(heap, val)
            if len(heap) > (arr if isinstance(arr, int) else len(arr)):
                heapq.heappop(heap)
        return heap[0] if heap else 0
