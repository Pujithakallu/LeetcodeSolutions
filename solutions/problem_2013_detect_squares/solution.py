"""
Problem 2013: Detect Squares
==========================
Difficulty: Medium
Tags: Array, Hash Table, Design, Counting, Data Stream
Pattern: Hash Map / Design

Time Complexity:  O(n) count
Space Complexity: O(n)
"""

class DetectSquares:
    def __init__(self):
        from collections import defaultdict
        self.points = defaultdict(int)

    def add(self, point):
        self.points[tuple(point)] += 1

    def count(self, point):
        px, py = point
        result = 0
        for (x, y), cnt in self.points.items():
            if x != px and abs(x - px) == abs(y - py):
                result += cnt * self.points.get((px, y), 0) * self.points.get((x, py), 0)
        return result
