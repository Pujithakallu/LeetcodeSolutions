"""
Problem 1409: Queries on a Permutation With Key
=============================================
Difficulty: Medium
Tags: Array, Binary Indexed Tree, Simulation
Pattern: Binary Indexed Tree / Fenwick Tree

Time Complexity:  O(n log n) build, O(log n) query/update
Space Complexity: O(n)
"""

class Solution:
    def processQueries(self, queries: List[int], m: int) -> List[int]:
        # Binary Indexed Tree (Fenwick) - O(log n) update/query
        n = len(queries)
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
        
        for i, val in enumerate(queries):
            update(i, val)
        return []
