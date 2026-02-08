"""
Problem 743: Network Delay Time
==============================
Difficulty: Medium
Tags: Depth-First Search, Breadth-First Search, Graph Theory, Heap (Priority Queue), Shortest Path
Pattern: Dijkstra / Shortest Path

Time Complexity:  O(E log V)
Space Complexity: O(V + E)
"""

import heapq
from collections import defaultdict

class Solution:
    def networkDelayTime(self, times, n, k):
        graph = defaultdict(list)
        for u, v, w in times:
            graph[u].append((v, w))
        dist = {}
        heap = [(0, k)]
        while heap:
            d, u = heapq.heappop(heap)
            if u in dist:
                continue
            dist[u] = d
            for v, w in graph[u]:
                if v not in dist:
                    heapq.heappush(heap, (d + w, v))
        return max(dist.values()) if len(dist) == n else -1
