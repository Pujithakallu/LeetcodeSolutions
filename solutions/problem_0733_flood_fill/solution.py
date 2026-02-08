"""
Problem 733: Flood Fill
======================
Difficulty: Easy
Tags: Array, Depth-First Search, Breadth-First Search, Matrix
Pattern: DFS / Graph

Time Complexity:  O(m*n)
Space Complexity: O(m*n)
"""

class Solution:
    def floodFill(self, image, sr, sc, color):
        orig = image[sr][sc]
        if orig == color:
            return image
        m, n = len(image), len(image[0])
        def dfs(r, c):
            if r < 0 or r >= m or c < 0 or c >= n or image[r][c] != orig:
                return
            image[r][c] = color
            dfs(r+1,c); dfs(r-1,c); dfs(r,c+1); dfs(r,c-1)
        dfs(sr, sc)
        return image
