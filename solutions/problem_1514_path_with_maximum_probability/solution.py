"""
Problem 1514: Path with Maximum Probability
=========================================
Difficulty: Medium
Tags: Array, Graph Theory, Heap (Priority Queue), Shortest Path
Pattern: Dijkstra (Max Probability)

Time Complexity:  O(E log V)
Space Complexity: O(V + E)
"""

import heapq
from collections import defaultdict

class Solution:
    def maxProbability(self, n, edges, succProb, start_node, end_node):
        graph = defaultdict(list)
        for i, (a, b) in enumerate(edges):
            graph[a].append((b, succProb[i]))
            graph[b].append((a, succProb[i]))
        dist = [0.0] * n
        dist[start_node] = 1.0
        heap = [(-1.0, start_node)]
        while heap:
            neg_prob, u = heapq.heappop(heap)
            prob = -neg_prob
            if u == end_node:
                return prob
            if prob < dist[u]:
                continue
            for v, p in graph[u]:
                new_prob = prob * p
                if new_prob > dist[v]:
                    dist[v] = new_prob
                    heapq.heappush(heap, (-new_prob, v))
        return 0.0
