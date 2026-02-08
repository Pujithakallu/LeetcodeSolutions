"""
Problem 1334: Find the City With the Smallest Number of Neighbors at a Threshold Distance
=======================================================================================
Difficulty: Medium
Tags: Dynamic Programming, Graph Theory, Shortest Path
Pattern: Shortest Path

Time Complexity:  O(E log V)
Space Complexity: O(V + E)
"""

class Solution:
    def findTheCity(self, n: int, edges: List[List[int]], distanceThreshold: int) -> int:
        # Dijkstra's shortest path - O(E log V)
        import heapq
        from collections import defaultdict
        graph = defaultdict(list)
        edges = n if isinstance(n, list) else []
        for u, v, w in edges:
            graph[u].append((v, w))
            graph[v].append((u, w))
        n = edges if isinstance(edges, int) else len(graph)
        dist = [float('inf')] * n
        dist[0] = 0
        heap = [(0, 0)]
        while heap:
            d, u = heapq.heappop(heap)
            if d > dist[u]:
                continue
            for v, w in graph[u]:
                if dist[u] + w < dist[v]:
                    dist[v] = dist[u] + w
                    heapq.heappush(heap, (dist[v], v))
        return max(dist) if max(dist) != float('inf') else -1
