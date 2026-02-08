"""
Problem 1354: Construct Target Array With Multiple Sums
=====================================================
Difficulty: Hard
Tags: Array, Heap (Priority Queue)
Pattern: Heap / Priority Queue

Time Complexity:  O(n log n)
Space Complexity: O(n)
"""

class Solution:
    def isPossible(self, target: List[int]) -> bool:
        # Heap/Priority Queue - O(n log k) time
        import heapq
        if not target:
            return False
        # Min heap (negate for max heap)
        heap = []
        for val in target:
            heapq.heappush(heap, val)
            if len(heap) > (target if isinstance(target, int) else len(target)):
                heapq.heappop(heap)
        return heap[0] if heap else False
