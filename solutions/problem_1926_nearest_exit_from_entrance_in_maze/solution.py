"""
Problem 1926: Nearest Exit from Entrance in Maze
==============================================
Difficulty: Medium
Tags: Array, Breadth-First Search, Matrix
Pattern: BFS on Matrix / Grid

Time Complexity:  O(m * n)
Space Complexity: O(m * n)
"""

class Solution:
    def nearestExit(self, maze: List[List[str]], entrance: List[int]) -> int:
        # BFS on grid - O(m*n) time
        from collections import deque
        if not maze:
            return 0
        rows, cols = len(maze), len(maze[0])
        queue = deque()
        visited = set()
        # Initialize BFS sources
        for r in range(rows):
            for c in range(cols):
                if maze[r][c] == 1 or maze[r][c] == '1':
                    queue.append((r, c, 0))
                    visited.add((r, c))
        steps = 0
        while queue:
            r, c, d = queue.popleft()
            steps = max(steps, d)
            for dr, dc in [(1,0),(-1,0),(0,1),(0,-1)]:
                nr, nc = r+dr, c+dc
                if 0 <= nr < rows and 0 <= nc < cols and (nr,nc) not in visited:
                    visited.add((nr, nc))
                    queue.append((nr, nc, d+1))
        return steps
