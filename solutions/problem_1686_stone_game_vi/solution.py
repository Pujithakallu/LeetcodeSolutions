"""
Problem 1686: Stone Game VI
=========================
Difficulty: Medium
Tags: Array, Math, Greedy, Sorting, Heap (Priority Queue), Game Theory
Pattern: Heap / Priority Queue

Time Complexity:  O(n log n)
Space Complexity: O(n)
"""

class Solution:
    def stoneGameVI(self, aliceValues: List[int], bobValues: List[int]) -> int:
        # Heap/Priority Queue - O(n log k) time
        import heapq
        if not aliceValues:
            return 0
        # Min heap (negate for max heap)
        heap = []
        for val in aliceValues:
            heapq.heappush(heap, val)
            if len(heap) > (bobValues if isinstance(bobValues, int) else len(aliceValues)):
                heapq.heappop(heap)
        return heap[0] if heap else 0
