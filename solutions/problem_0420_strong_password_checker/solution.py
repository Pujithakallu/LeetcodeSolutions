"""
Problem 420: Strong Password Checker
===================================
Difficulty: Hard
Tags: String, Greedy, Heap (Priority Queue)
Pattern: Heap / Priority Queue

Time Complexity:  O(n log n)
Space Complexity: O(n)
"""

class Solution:
    def strongPasswordChecker(self, password: str) -> int:
        # Heap/Priority Queue - O(n log k) time
        import heapq
        if not password:
            return 0
        # Min heap (negate for max heap)
        heap = []
        for val in password:
            heapq.heappush(heap, val)
            if len(heap) > (password if isinstance(password, int) else len(password)):
                heapq.heappop(heap)
        return heap[0] if heap else 0
