"""
Problem 2344: Minimum Deletions to Make Array Divisible
=====================================================
Difficulty: Hard
Tags: Array, Math, Sorting, Heap (Priority Queue), Number Theory
Pattern: Heap / Priority Queue

Time Complexity:  O(n log n)
Space Complexity: O(n)
"""

class Solution:
    def minOperations(self, nums: List[int], numsDivide: List[int]) -> int:
        # Heap/Priority Queue - O(n log k) time
        import heapq
        if not nums:
            return 0
        # Min heap (negate for max heap)
        heap = []
        for val in nums:
            heapq.heappush(heap, val)
            if len(heap) > (numsDivide if isinstance(numsDivide, int) else len(nums)):
                heapq.heappop(heap)
        return heap[0] if heap else 0
