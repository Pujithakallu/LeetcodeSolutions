"""
Problem 1631: Path With Minimum Effort
====================================
Difficulty: Medium
Tags: Array, Binary Search, Depth-First Search, Breadth-First Search, Union-Find, Heap (Priority Queue), Matrix
Pattern: Dijkstra / Graph

Time Complexity:  O(mn log(mn))
Space Complexity: O(mn)
"""

import heapq

class Solution:
    def minimumEffortPath(self, heights):
        m, n = len(heights), len(heights[0])
        dist = [[float('inf')] * n for _ in range(m)]
        dist[0][0] = 0
        heap = [(0, 0, 0)]
        while heap:
            effort, r, c = heapq.heappop(heap)
            if r == m-1 and c == n-1:
                return effort
            if effort > dist[r][c]:
                continue
            for dr, dc in [(-1,0),(1,0),(0,-1),(0,1)]:
                nr, nc = r+dr, c+dc
                if 0 <= nr < m and 0 <= nc < n:
                    new_effort = max(effort, abs(heights[r][c] - heights[nr][nc]))
                    if new_effort < dist[nr][nc]:
                        dist[nr][nc] = new_effort
                        heapq.heappush(heap, (new_effort, nr, nc))
        return 0
