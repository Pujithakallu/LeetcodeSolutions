"""
Problem 1584: Min Cost to Connect All Points
==========================================
Difficulty: Medium
Tags: Array, Union-Find, Graph Theory, Minimum Spanning Tree
Pattern: Prim's MST / Graph

Time Complexity:  O(n^2 log n)
Space Complexity: O(n^2)
"""

class Solution:
    def minCostConnectPoints(self, points: list[list[int]]) -> int:
        import heapq
        n = len(points)
        visited = set()
        heap = [(0, 0)]
        cost = 0
        while len(visited) < n:
            d, u = heapq.heappop(heap)
            if u in visited:
                continue
            visited.add(u)
            cost += d
            for v in range(n):
                if v not in visited:
                    dist = abs(points[u][0]-points[v][0]) + abs(points[u][1]-points[v][1])
                    heapq.heappush(heap, (dist, v))
        return cost
