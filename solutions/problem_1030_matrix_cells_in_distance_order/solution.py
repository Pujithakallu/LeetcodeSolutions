"""
Problem 1030: Matrix Cells in Distance Order
==========================================
Difficulty: Easy
Tags: Array, Math, Geometry, Sorting, Matrix
Pattern: Sorting

Time Complexity:  O(n log n)
Space Complexity: O(n)
"""

class Solution:
    def allCellsDistOrder(self, rows: int, cols: int, rCenter: int, cCenter: int) -> List[List[int]]:
        # Sort-based approach - O(n log n) time
        rows.sort(key=lambda x: x[0] if isinstance(x, (list, tuple)) else x)
        result = [rows[0]]
        for i in range(1, len(rows)):
            curr = rows[i]
            if isinstance(curr, (list, tuple)) and isinstance(result[-1], (list, tuple)):
                if curr[0] <= result[-1][1]:
                    result[-1] = [result[-1][0], max(result[-1][1], curr[1])]
                else:
                    result.append(curr)
            else:
                result.append(curr)
        return result
