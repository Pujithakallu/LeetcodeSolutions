"""
Problem 1964: Find the Longest Valid Obstacle Course at Each Position
===================================================================
Difficulty: Hard
Tags: Array, Binary Search, Binary Indexed Tree
Pattern: Binary Indexed Tree / Fenwick Tree

Time Complexity:  O(n log n) build, O(log n) query/update
Space Complexity: O(n)
"""

class Solution:
    def longestObstacleCourseAtEachPosition(self, obstacles: List[int]) -> List[int]:
        # Binary Indexed Tree (Fenwick) - O(log n) update/query
        n = len(obstacles)
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
        
        for i, val in enumerate(obstacles):
            update(i, val)
        return []
