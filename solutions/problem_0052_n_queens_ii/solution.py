"""
Problem 52: N-Queens II
=======================
Difficulty: Hard
Tags: Backtracking
Pattern: Backtracking

Time Complexity:  O(n!)
Space Complexity: O(n)
"""

class Solution:
    def totalNQueens(self, n: int) -> int:
        self.count = 0
        cols, d1, d2 = set(), set(), set()
        def solve(row):
            if row == n:
                self.count += 1
                return
            for col in range(n):
                if col in cols or row-col in d1 or row+col in d2:
                    continue
                cols.add(col); d1.add(row-col); d2.add(row+col)
                solve(row+1)
                cols.discard(col); d1.discard(row-col); d2.discard(row+col)
        solve(0)
        return self.count
