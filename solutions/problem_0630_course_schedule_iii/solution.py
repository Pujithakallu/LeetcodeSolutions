"""
Problem 630: Course Schedule III
===============================
Difficulty: Hard
Tags: Array, Greedy, Sorting, Heap (Priority Queue)
Pattern: Heap / Priority Queue

Time Complexity:  O(n log n)
Space Complexity: O(n)
"""

class Solution:
    def scheduleCourse(self, courses: List[List[int]]) -> int:
        # Heap/Priority Queue - O(n log k) time
        import heapq
        if not courses:
            return 0
        # Min heap (negate for max heap)
        heap = []
        for val in courses:
            heapq.heappush(heap, val)
            if len(heap) > (courses if isinstance(courses, int) else len(courses)):
                heapq.heappop(heap)
        return heap[0] if heap else 0
