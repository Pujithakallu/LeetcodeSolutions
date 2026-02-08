"""
Problem 841: Keys and Rooms
==========================
Difficulty: Medium
Tags: Depth-First Search, Breadth-First Search, Graph Theory
Pattern: DFS / Graph

Time Complexity:  O(V + E)
Space Complexity: O(V)
"""

class Solution:
    def canVisitAllRooms(self, rooms: list[list[int]]) -> bool:
        visited = set([0])
        stack = [0]
        while stack:
            room = stack.pop()
            for key in rooms[room]:
                if key not in visited:
                    visited.add(key)
                    stack.append(key)
        return len(visited) == len(rooms)
