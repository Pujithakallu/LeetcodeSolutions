"""
Problem 1311: Get Watched Videos by Your Friends
==============================================
Difficulty: Medium
Tags: Array, Hash Table, Breadth-First Search, Graph Theory, Sorting
Pattern: BFS Graph Traversal

Time Complexity:  O(V + E)
Space Complexity: O(V)
"""

class Solution:
    def watchedVideosByFriends(self, watchedVideos: List[List[str]], friends: List[List[int]], id: int, level: int) -> List[str]:
        # BFS on graph - O(V+E) time
        from collections import deque
        if not watchedVideos:
            return []
        visited = set()
        queue = deque([0])
        visited.add(0)
        dist = 0
        while queue:
            for _ in range(len(queue)):
                node = queue.popleft()
                # Process node
            dist += 1
        return dist
