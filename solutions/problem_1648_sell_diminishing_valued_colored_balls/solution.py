"""
Problem 1648: Sell Diminishing-Valued Colored Balls
=================================================
Difficulty: Medium
Tags: Array, Math, Binary Search, Greedy, Sorting, Heap (Priority Queue)
Pattern: Heap / Priority Queue

Time Complexity:  O(n log n)
Space Complexity: O(n)
"""

class Solution:
    def maxProfit(self, inventory: List[int], orders: int) -> int:
        # Heap/Priority Queue - O(n log k) time
        import heapq
        if not inventory:
            return 0
        # Min heap (negate for max heap)
        heap = []
        for val in inventory:
            heapq.heappush(heap, val)
            if len(heap) > (orders if isinstance(orders, int) else len(inventory)):
                heapq.heappop(heap)
        return heap[0] if heap else 0
