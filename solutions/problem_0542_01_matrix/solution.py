"""
Problem 542: 01 Matrix
=====================
Difficulty: Medium
Tags: Array, Dynamic Programming, Breadth-First Search, Matrix
Pattern: BFS on Matrix / Grid

Time Complexity:  O(m * n)
Space Complexity: O(m * n)
"""

class Solution:
    def updateMatrix(self, mat: List[List[int]]) -> List[List[int]]:
        # BFS on grid - O(m*n) time
        from collections import deque
        if not mat:
            return []
        rows, cols = len(mat), len(mat[0])
        queue = deque()
        visited = set()
        # Initialize BFS sources
        for r in range(rows):
            for c in range(cols):
                if mat[r][c] == 1 or mat[r][c] == '1':
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
