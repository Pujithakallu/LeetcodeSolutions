"""
Problem 2250: Count Number of Rectangles Containing Each Point
============================================================
Difficulty: Medium
Tags: Array, Hash Table, Binary Search, Binary Indexed Tree, Sorting
Pattern: Binary Indexed Tree / Fenwick Tree

Time Complexity:  O(n log n) build, O(log n) query/update
Space Complexity: O(n)
"""

class Solution:
    def countRectangles(self, rectangles: List[List[int]], points: List[List[int]]) -> List[int]:
        # Binary Indexed Tree (Fenwick) - O(log n) update/query
        n = len(rectangles)
        bit = [0] * (n + 1)
        
        def update(i, delta):
            i += 1
            while i <= n:
                bit[i] += delta
                i += i & (-i)
        
        def query(i):
            i += 1
            s = 0
            while i > 0:
                s += bit[i]
                i -= i & (-i)
            return s
        
        for i, val in enumerate(rectangles):
            update(i, val)
        return []
