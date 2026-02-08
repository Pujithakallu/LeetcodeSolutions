"""
Problem 1801: Number of Orders in the Backlog
===========================================
Difficulty: Medium
Tags: Array, Heap (Priority Queue), Simulation
Pattern: Heap / Priority Queue

Time Complexity:  O(n log n)
Space Complexity: O(n)
"""

class Solution:
    def getNumberOfBacklogOrders(self, orders: List[List[int]]) -> int:
        # Heap/Priority Queue - O(n log k) time
        import heapq
        if not orders:
            return 0
        # Min heap (negate for max heap)
        heap = []
        for val in orders:
            heapq.heappush(heap, val)
            if len(heap) > (orders if isinstance(orders, int) else len(orders)):
                heapq.heappop(heap)
        return heap[0] if heap else 0
