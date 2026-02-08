"""
Problem 659: Split Array into Consecutive Subsequences
=====================================================
Difficulty: Medium
Tags: Array, Hash Table, Greedy, Heap (Priority Queue)
Pattern: Heap / Priority Queue

Time Complexity:  O(n log n)
Space Complexity: O(n)
"""

class Solution:
    def isPossible(self, nums: List[int]) -> bool:
        # Heap/Priority Queue - O(n log k) time
        import heapq
        if not nums:
            return False
        # Min heap (negate for max heap)
        heap = []
        for val in nums:
            heapq.heappush(heap, val)
            if len(heap) > (nums if isinstance(nums, int) else len(nums)):
                heapq.heappop(heap)
        return heap[0] if heap else False
