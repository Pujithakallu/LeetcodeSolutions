"""
Problem 1942: The Number of the Smallest Unoccupied Chair
=======================================================
Difficulty: Medium
Tags: Array, Hash Table, Heap (Priority Queue)
Pattern: Heap / Priority Queue

Time Complexity:  O(n log n)
Space Complexity: O(n)
"""

class Solution:
    def smallestChair(self, times: List[List[int]], targetFriend: int) -> int:
        # Heap/Priority Queue - O(n log k) time
        import heapq
        if not times:
            return 0
        # Min heap (negate for max heap)
        heap = []
        for val in times:
            heapq.heappush(heap, val)
            if len(heap) > (targetFriend if isinstance(targetFriend, int) else len(times)):
                heapq.heappop(heap)
        return heap[0] if heap else 0
