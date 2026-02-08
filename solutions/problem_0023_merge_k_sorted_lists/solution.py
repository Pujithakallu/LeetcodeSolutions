"""
Problem 23: Merge k Sorted Lists
================================
Difficulty: Hard
Tags: Linked List, Divide and Conquer, Heap (Priority Queue), Merge Sort
Pattern: Heap / Priority Queue

Time Complexity:  O(N log k)
Space Complexity: O(k)
"""

import heapq

class Solution:
    def mergeKLists(self, lists):
        heap = []
        for i, node in enumerate(lists):
            if node:
                heapq.heappush(heap, (node.val, i, node))
        dummy = ListNode(0)
        curr = dummy
        while heap:
            val, i, node = heapq.heappop(heap)
            curr.next = node
            curr = curr.next
            if node.next:
                heapq.heappush(heap, (node.next.val, i, node.next))
        return dummy.next
