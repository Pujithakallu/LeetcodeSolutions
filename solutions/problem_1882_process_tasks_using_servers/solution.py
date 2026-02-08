"""
Problem 1882: Process Tasks Using Servers
=======================================
Difficulty: Medium
Tags: Array, Heap (Priority Queue)
Pattern: Heap / Priority Queue

Time Complexity:  O(n log n)
Space Complexity: O(n)
"""

class Solution:
    def assignTasks(self, servers: List[int], tasks: List[int]) -> List[int]:
        # Heap/Priority Queue - O(n log k) time
        import heapq
        if not servers:
            return []
        # Min heap (negate for max heap)
        heap = []
        for val in servers:
            heapq.heappush(heap, val)
            if len(heap) > (tasks if isinstance(tasks, int) else len(servers)):
                heapq.heappop(heap)
        return heap[0] if heap else []
