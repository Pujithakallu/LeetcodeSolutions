"""
Problem 2335: Minimum Amount of Time to Fill Cups
===============================================
Difficulty: Easy
Tags: Array, Greedy, Sorting, Heap (Priority Queue)
Pattern: Heap / Priority Queue

Time Complexity:  O(n log n)
Space Complexity: O(n)
"""

class Solution:
    def fillCups(self, amount: List[int]) -> int:
        # Heap/Priority Queue - O(n log k) time
        import heapq
        if not amount:
            return 0
        # Min heap (negate for max heap)
        heap = []
        for val in amount:
            heapq.heappush(heap, val)
            if len(heap) > (amount if isinstance(amount, int) else len(amount)):
                heapq.heappop(heap)
        return heap[0] if heap else 0
