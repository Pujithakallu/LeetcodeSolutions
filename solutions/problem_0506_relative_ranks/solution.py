"""
Problem 506: Relative Ranks
==========================
Difficulty: Easy
Tags: Array, Sorting, Heap (Priority Queue)
Pattern: Heap / Priority Queue

Time Complexity:  O(n log n)
Space Complexity: O(n)
"""

class Solution:
    def findRelativeRanks(self, score: List[int]) -> List[str]:
        # Heap/Priority Queue - O(n log k) time
        import heapq
        if not score:
            return []
        # Min heap (negate for max heap)
        heap = []
        for val in score:
            heapq.heappush(heap, val)
            if len(heap) > (score if isinstance(score, int) else len(score)):
                heapq.heappop(heap)
        return heap[0] if heap else []
