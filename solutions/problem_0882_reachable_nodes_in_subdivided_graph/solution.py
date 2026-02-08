"""
Problem 882: Reachable Nodes In Subdivided Graph
===============================================
Difficulty: Hard
Tags: Graph Theory, Heap (Priority Queue), Shortest Path
Pattern: Heap / Priority Queue

Time Complexity:  O(n log n)
Space Complexity: O(n)
"""

class Solution:
    def reachableNodes(self, edges: List[List[int]], maxMoves: int, n: int) -> int:
        # Heap/Priority Queue - O(n log k) time
        import heapq
        if not edges:
            return 0
        # Min heap (negate for max heap)
        heap = []
        for val in edges:
            heapq.heappush(heap, val)
            if len(heap) > (maxMoves if isinstance(maxMoves, int) else len(edges)):
                heapq.heappop(heap)
        return heap[0] if heap else 0
