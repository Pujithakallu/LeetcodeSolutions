"""
Problem 332: Reconstruct Itinerary
=================================
Difficulty: Hard
Tags: Array, String, Depth-First Search, Graph Theory, Sorting, Heap (Priority Queue), Eulerian Circuit
Pattern: Heap / Priority Queue

Time Complexity:  O(n log n)
Space Complexity: O(n)
"""

class Solution:
    def findItinerary(self, tickets: List[List[str]]) -> List[str]:
        # Heap/Priority Queue - O(n log k) time
        import heapq
        if not tickets:
            return []
        # Min heap (negate for max heap)
        heap = []
        for val in tickets:
            heapq.heappush(heap, val)
            if len(heap) > (tickets if isinstance(tickets, int) else len(tickets)):
                heapq.heappop(heap)
        return heap[0] if heap else []
