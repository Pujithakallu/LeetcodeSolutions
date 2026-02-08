"""
Problem 787: Cheapest Flights Within K Stops
===========================================
Difficulty: Medium
Tags: Dynamic Programming, Depth-First Search, Breadth-First Search, Graph Theory, Heap (Priority Queue), Shortest Path
Pattern: Bellman-Ford (k stops)

Time Complexity:  O(k * E)
Space Complexity: O(V)
"""

class Solution:
    def findCheapestPrice(self, n, flights, src, dst, k):
        prices = [float('inf')] * n
        prices[src] = 0
        for _ in range(k + 1):
            temp = prices[:]
            for u, v, w in flights:
                if prices[u] != float('inf'):
                    temp[v] = min(temp[v], prices[u] + w)
            prices = temp
        return prices[dst] if prices[dst] != float('inf') else -1
