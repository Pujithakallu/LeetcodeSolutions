"""
Problem 2203: Minimum Weighted Subgraph With the Required Paths
=============================================================
Difficulty: Hard
Tags: Graph Theory, Heap (Priority Queue), Shortest Path
Pattern: Heap / Priority Queue

Time Complexity:  O(n log n)
Space Complexity: O(n)
"""

class Solution:
    def minimumWeight(self, n: int, edges: List[List[int]], src1: int, src2: int, dest: int) -> int:
        # Heap/Priority Queue - O(n log k) time
        import heapq
        if not n:
            return 0
        # Min heap (negate for max heap)
        heap = []
        for val in n:
            heapq.heappush(heap, val)
            if len(heap) > (edges if isinstance(edges, int) else len(n)):
                heapq.heappop(heap)
        return heap[0] if heap else 0
