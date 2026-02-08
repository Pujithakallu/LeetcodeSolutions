"""
Problem 218: The Skyline Problem
===============================
Difficulty: Hard
Tags: Array, Divide and Conquer, Binary Indexed Tree, Segment Tree, Sweep Line, Sorting, Heap (Priority Queue), Ordered Set
Pattern: Segment Tree

Time Complexity:  O(n log n) build, O(log n) query/update
Space Complexity: O(n)
"""

class Solution:
    def getSkyline(self, buildings: List[List[int]]) -> List[List[int]]:
        # Segment tree for range queries - O(n log n) build, O(log n) query
        n = len(buildings)
        tree = [0] * (4 * n)
        
        def build(node, start, end):
            if start == end:
                tree[node] = buildings[start]
                return
            mid = (start + end) // 2
            build(2*node, start, mid)
            build(2*node+1, mid+1, end)
            tree[node] = tree[2*node] + tree[2*node+1]
        
        def query(node, start, end, l, r):
            if r < start or end < l:
                return 0
            if l <= start and end <= r:
                return tree[node]
            mid = (start + end) // 2
            return query(2*node, start, mid, l, r) + query(2*node+1, mid+1, end, l, r)
        
        build(1, 0, n-1)
        return []
